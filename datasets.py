# -*- coding: utf-8 -*-
"""
This module includes functions to retrieve datasets.
"""

# Author: Jael Zela <jael.ruiz@students.ic.unicamp.br>

import json
import io
from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation as signs
from nltk.corpus import stopwords as stopswords_corpus

stops = set(stopswords_corpus.words('english'))


class CategorizedDataset(object):

    def __init__(self, name, categories, encoding='utf8'):
        if name is None:
            raise AttributeError('File name is required.')

        self.__name = name
        self.__encoding = encoding
        self._categories = categories
        self._dataset = dict()
        self._load()

    def _load(self):
        with io.open(self.__name, 'r', encoding=self.__encoding) as data_file:
            data = json.load(data_file, encoding=self.__encoding)
            data_file.close()

        self._dataset = data


class G2CrowdDataset(CategorizedDataset):

    def __init__(self, name, categories, encoding='utf8'):
        super(G2CrowdDataset, self).__init__(name, categories, encoding=encoding)

    def raw(self, category):
        raw_text = []

        if category not in self._categories:
            return raw_text

        for review in self._dataset:
            if category in 'pos,positive':
                raw_text.append(review['like'])
            elif category in 'neg,negative':
                raw_text.append(review['dislike'])

        return raw_text

    def raw_sents(self, category):
        raw_text = []

        if category not in self._categories:
            return raw_text

        for review in self._dataset:
            if category in 'pos,positive':
                for sen in sent_tokenize(review['like']):
                    raw_text.append(sen)
            elif category in 'neg,negative':
                for sen in sent_tokenize(review['dislike']):
                    raw_text.append(sen)

        return raw_text

    def words(self, category, stopwords=True, punctuation=True):
        result = []

        if category not in self._categories:
            return result

        words_text = []
        for review in self._dataset:
            if category in 'pos,positive':
                words_text.append(word_tokenize(review['like']))
            elif category in 'neg,negative':
                words_text.append(word_tokenize(review['dislike']))

        result = words_text

        if not punctuation:
            words_text = result
            result = [word for word in words_text if word not in signs]

        if not stopwords:
            words_text = result
            result = [word for word in words_text if word.lower() not in stops]

        return result

    def sents(self, category, stopwords=True, punctuation=True):
        result = []

        if category not in self._categories:
            return result

        sents_text = []
        for review in self._dataset:
            if category in 'pos,positive':
                for sen in sent_tokenize(review['like']):
                    sents_text.append(word_tokenize(sen))
            elif category in 'neg,negative':
                for sen in sent_tokenize(review['dislike']):
                    sents_text.append(word_tokenize(sen))

        result = sents_text

        if not punctuation:
            sents_text = result
            result = [[word for word in sen if word not in signs] for sen in sents_text]

        if not stopwords:
            sents_text = result
            result = [[word for word in sen if word.lower() not in stops] for sen in sents_text]

        return result


g2crowd = G2CrowdDataset('g2crowd_reviews.json', ['pos', 'neg'])
