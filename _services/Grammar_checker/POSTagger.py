import os
from typing import List, Text, Tuple

import joblib

from sinling.sinhala.stemmer import SinhalaStemmer
from sinling.config import RESOURCE_PATH
from sinling.core import Tagger


class POSTagger(Tagger):
    def __init__(self):
        self._model = joblib.load("/home/vidula/Pictures/git lab/2021-063/sinhala_ocr_backend/_services/Grammar_checker/pos-tagger-crf-sinling.joblib",'r')
        self._stemmer = SinhalaStemmer()

    def predict(self, x: List[List[Text]]) -> List[List[Tuple[Text, Text]]]:
        features = [[self._word2features(ts, i) for i in range(len(ts))] for ts in x]
        pos_tags = self._model.predict(features)
        return [list(zip(x[ix], pos_tags[ix])) for ix in range(len(x))]

    def _word2features(self, sent, i):
        word = sent[i]
        stem, suff = self._stemmer.stem(word)
        features = {
            'bias': 1.0,
            word: True,
            f'STEM': stem,
            f'SUFF': suff,
            'len(word)': len(word),
            'word.isdigit()': word.isdigit(),
        }
        if i > 0:
            word_prev = sent[i - 1]
            features.update({
                f'-1:word': word_prev,
                '-1:word.isdigit()': word_prev.isdigit(),
            })
        else:
            features['BOS'] = True
        if i < len(sent) - 1:
            word_next = sent[i + 1]
            features.update({
                f'+1:word': word_next,
                '+1:word.isdigit()': word_next.isdigit(),
            })
        else:
            features['EOS'] = True
        return features