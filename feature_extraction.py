# -*- coding: utf-8 -*-
"""
This module includes functions to extract features from text.
"""

# Author: Jael Zela <jael.ruiz@students.ic.unicamp.br>

import sys
import treetaggerwrapper as ttw
from nltk.tokenize import word_tokenize
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures, NgramAssocMeasures
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder, QuadgramCollocationFinder
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer


tagger = ttw.TreeTagger(TAGLANG='en')


def bigram_feats(text, score_fn=BigramAssocMeasures.pmi, n_best=200):
    bigram_finder = BigramCollocationFinder.from_words(text)
    n_grams = bigram_finder.nbest(score_fn, n_best)
    return dict([(n_gram, True) for n_gram in n_grams])


def trigram_feats(text, score_fn=TrigramAssocMeasures.pmi, n_best=200):
    trigram_finder = TrigramCollocationFinder.from_words(text)
    n_grams = trigram_finder.nbest(score_fn, n_best)
    return dict([(n_gram, True) for n_gram in n_grams])


def quadgram_feats(text, score_fn=NgramAssocMeasures.pmi, n_best=200):
    #n_grams = list(ngrams(characters, n)) + list(ngrams(characters, n-1)) + list(ngrams(characters, n-2))
    quadgram_finder = QuadgramCollocationFinder.from_words(text)
    n_grams = quadgram_finder.nbest(score_fn, n_best)
    return dict([(n_gram, True) for n_gram in n_grams])


def multigram_feats(text):
    grams = bigram_character_feats(text)
    grams.update(trigram_character_feats(text))
    grams.update(quadgram_character_feats(text))
    return grams


def bag_of_words(words):
    return dict([(word, True) for word in words])


def tokenize(text):
    tokens = word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems


def build_tfidf(documents):
    docs = []
    for doc in documents:
        docs.append(' '.join(doc))

    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfidf.fit_transform(docs)
    return tfidf


def tf_idf(words, tfidf):
    text = ' '.join(words)
    response = tfidf.transform([text])
    feature_names = tfidf.get_feature_names()
    return dict([(feature_names[col], response[0, col]) for col in response.nonzero()[1]])


def part_of_speech(words):
    tags = []
    t_tags = ttw.make_tags(tagger.tag_text(unicode(' '.join(words))), exclude_nottags=True)
    for tag in t_tags:
        tags.append((tag.lemma, tag.pos))
    return dict([(tag, True) for tag in tags])


def feature_eval(featxs, words, **params):
    features = dict()

    for featx in featxs:
        if featx.__name__ == 'tf_idf' and params['tfidf'] is not None:
            features.update(featx(words, params['tfidf']))
        else:
            features.update(featx(words))

    return features


def feature_extraction(featxs, datasets, stopwords=True, punctuation=True):
    possents = []
    negsents = []

    for dataset in datasets:
        possents += dataset.sents('pos', stopwords=stopwords, punctuation=punctuation)
        negsents += dataset.sents('neg', stopwords=stopwords, punctuation=punctuation)

    possents = possents[:len(negsents)]

    print 'Sentences'
    print 'positive:', len(possents), 'negative:', len(negsents)

    print '\nSettings'
    print 'stopwords:', stopwords, 'punctuation:', punctuation
    sys.stdout.write('features: ')
    tfidf = None
    for feat in featxs:
        sys.stdout.write(feat.__name__ + ', ')
        sys.stdout.flush()
        if feat.__name__ == 'tf_idf':
            tfidf = build_tfidf(possents + negsents)

    print '\n\nProcessing'
    print 'pos features'
    posfeats = [(feature_eval(featxs, sen, tfidf=tfidf), 'pos') for sen in possents]
    print 'neg features'
    negfeats = [(feature_eval(featxs, sen, tfidf=tfidf), 'neg') for sen in negsents]

    return posfeats, negfeats