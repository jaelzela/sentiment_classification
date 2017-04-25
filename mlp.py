# -*- coding: utf-8 -*-
"""
This module includes functions to evaluate a NaiveBayesClassifier.
"""

# Author: Jael Zela <jael.ruiz@students.ic.unicamp.br>

import json
from feature_extraction import bigram_feats, bag_of_words, tf_idf, feature_extraction, build_tfidf
from validation import cross_validation
from datasets import g2crowd


def evaluate_classifier(featxs, datasets):

    posfeats, negfeats = feature_extraction(featxs, datasets, stopwords=False, punctuation=False)

    print '\ncross validation MLP'
    print cross_validation(posfeats, negfeats, folds=5, classifier='mlp_nn')


if __name__ == "__main__":
    evaluate_classifier([bigram_feats], [g2crowd])
