import torch
from kobart import get_kobart_tokenizer
from transformers.models.bart import BartForConditionalGeneration
import pandas as pd
import collections
import re
import nltk
import scoring
import six
from six.moves import map
from six.moves import range

import datetime
from tqdm.contrib import tzip
from datasets import load_metric

"""Computes rouge scores between two text blobs.

Implementation replicates the functionality in the original ROUGE package. See:

Lin, Chin-Yew. ROUGE: a Package for Automatic Evaluation of Summaries. In
Proceedings of the Workshop on Text Summarization Branches Out (WAS 2004),
Barcelona, Spain, July 25 - 26, 2004.

Default options are equivalent to running:
ROUGE-1.5.5.pl -e data -n 2 -a settings.xml

Or with use_stemmer=True:
ROUGE-1.5.5.pl -m -e data -n 2 -a settings.xml

In these examples settings.xml lists input files and formats.
"""


class RougeScorer(scoring.BaseScorer):
    """Calculate rouges scores between two blobs of text.

    Sample usage:
    scorer = RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score('The quick brown fox jumps over the lazy dog',
                          'The quick brown dog jumps on the log.')
    """

    def __init__(self, rouge_types, use_stemmer=False, split_summaries=False):
        """Initializes a new RougeScorer.

        Valid rouge types that can be computed are:
          rougen (e.g. rouge1, rouge2): n-gram based scoring.
          rougeL: Longest common subsequence based scoring.

        Args:
          rouge_types: A list of rouge types to calculate.
          use_stemmer: Bool indicating whether Porter stemmer should be used to
            strip word suffixes to improve matching.
          split_summaries: whether to add newlines between sentences for rougeLsum
        Returns:
          A dict mapping rouge types to Score tuples.
        """
        
        self.rouge_types = rouge_types
        self._stemmer = porter.PorterStemmer() if use_stemmer else None
        self._split_summaries = split_summaries

    def score(self, target, prediction, tokenizer):
        """Calculates rouge scores between the target and prediction.

        Args:
          target: Text containing the target (ground truth) text.
          prediction: Text containing the predicted text.
        Returns:
          A dict mapping each rouge type to a Score object.
        Raises:
          ValueError: If an invalid rouge type is encountered.
        """

        # Pre-compute target tokens and prediction tokens for use by different
        # types, except if only "rougeLsum" is requested.
        target_tokens = tokenizer.tokenize(ref)
        prediction_tokens = tokenizer.tokenize(output)
        result = {}

        for rouge_type in self.rouge_types:
            if rouge_type == "rougeL":
                # Rouge from longest common subsequences.
                scores = _score_lcs(target_tokens, prediction_tokens)
            elif re.match(r"rouge[0-9]$", six.ensure_str(rouge_type)):
                # Rouge from n-grams.
                n = int(rouge_type[5:])
                if n <= 0:
                    raise ValueError("rougen requires positive n: %s" % rouge_type)
                target_ngrams = _create_ngrams(target_tokens, n)
                prediction_ngrams = _create_ngrams(prediction_tokens, n)
                scores = _score_ngrams(target_ngrams, prediction_ngrams)
            else:
                raise ValueError("Invalid rouge type: %s" % rouge_type)
            result[rouge_type] = scores
        
        return result


def _create_ngrams(tokens, n):
    """Creates ngrams from the given list of tokens.

    Args:
    tokens: A list of tokens from which ngrams are created.
    n: Number of tokens to use, e.g. 2 for bigrams.
    Returns:
    A dictionary mapping each bigram to the number of occurrences.
    """

    ngrams = collections.Counter()
    for ngram in (tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)):
        ngrams[ngram] += 1
    return ngrams


def _score_lcs(target_tokens, prediction_tokens):
    """Computes LCS (Longest Common Subsequence) rouge scores.

    Args:
    target_tokens: Tokens from the target text.
    prediction_tokens: Tokens from the predicted text.
    Returns:
    A Score object containing computed scores.
    """

    if not target_tokens or not prediction_tokens:
        return scoring.Score(precision=0, recall=0, fmeasure=0)

    # Compute length of LCS from the bottom up in a table (DP appproach).
    lcs_table = _lcs_table(target_tokens, prediction_tokens)
    lcs_length = lcs_table[-1][-1]

    precision = lcs_length / len(prediction_tokens)
    recall = lcs_length / len(target_tokens)
    fmeasure = scoring.fmeasure(precision, recall)

    return scoring.Score(precision=precision, recall=recall, fmeasure=fmeasure)


def _lcs_table(ref, can):
    """Create 2-d LCS score table."""
    rows = len(ref)
    cols = len(can)
    lcs_table = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if ref[i - 1] == can[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
    return lcs_table



def _score_ngrams(target_ngrams, prediction_ngrams):
    """Compute n-gram based rouge scores.

    Args:
    target_ngrams: A Counter object mapping each ngram to number of
      occurrences for the target text.
    prediction_ngrams: A Counter object mapping each ngram to number of
      occurrences for the prediction text.
    Returns:
    A Score object containing computed scores.
    """

    intersection_ngrams_count = 0
    for ngram in six.iterkeys(target_ngrams):
        intersection_ngrams_count += min(target_ngrams[ngram],
                                 prediction_ngrams[ngram])
    target_ngrams_count = sum(target_ngrams.values())
    prediction_ngrams_count = sum(prediction_ngrams.values())

    precision = intersection_ngrams_count / max(prediction_ngrams_count, 1)
    recall = intersection_ngrams_count / max(target_ngrams_count, 1)
    fmeasure = scoring.fmeasure(precision, recall)

    return scoring.Score(precision=precision, recall=recall, fmeasure=fmeasure)



if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = BartForConditionalGeneration.from_pretrained('./kobart_summary/abs_v1')
    model.to(device)
    tokenizer = get_kobart_tokenizer()
    
    test_df = pd.read_csv('./data/test_v1.csv')
    preds, scores = [], []
    scorer = RougeScorer(['rouge1', 'rouge2'])
    for text, ref in tzip(test_df['original'],test_df['ext']):
        text = text.replace('\n', '')
        input_ids = tokenizer.encode(text)
        input_ids = torch.tensor(input_ids)
        input_ids = input_ids.unsqueeze(0)
        input_ids = input_ids.to(device)
        output = model.generate(input_ids, eos_token_id=1, max_length=512, num_beams=5)
        output = tokenizer.decode(output[0], skip_special_tokens=True)
        preds.append(output)
        score = scorer.score(ref, text, tokenizer)
        scores.append(score)
    test_df['preds'] = preds
    test_df['scores'] = scores
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    test_df.to_csv(f'./predictions/pred_abs_v1_{date}.csv')