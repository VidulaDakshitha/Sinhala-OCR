import os
from typing import List, Text, Tuple

import joblib

from sinling.sinhala.stemmer import SinhalaStemmer
from sinling.config import RESOURCE_PATH
from sinling.core import Tagger
from sinling import SinhalaTokenizer

from _services.Grammar_checker.POSTagger import POSTagger
from _services.Grammar_checker.grammar_check import Grammer_predict


def grammer_main(word_string):
    try:
        tokenizer = SinhalaTokenizer()

        document = 'අපි අඹ කමු. ඇය අඹ කමු.'
        document2 = 'ඇය අඹ කමු.'

        tokenized_sentences = [tokenizer.tokenize(f'{ss}.') for ss in tokenizer.split_sentences(word_string)]

        tagger = POSTagger()

        pos_tags = tagger.predict(tokenized_sentences)

        result = []
        print(pos_tags)
        for j, tags in enumerate(pos_tags):
            try:
                subject = ""
                verb = ""
                print("tags")
                print(tags)
                for i, sent in enumerate(tags):
                    if sent[1] == "PRP":
                        subject = sent[0]
                    elif sent[1] == "VFM":
                        verb = sent[0]

                if subject != "" and verb != "":
                    print("---------------------------------------")
                    print("1)")

                    print(*tokenized_sentences[j], sep=" ");
                    print(tokenized_sentences[j])
                    print("")
                    result.append([tokenized_sentences[j],tags, Grammer_predict(subject, verb)])
            except Exception as ex:
                print("---------------------------------------")
                print("1)")

                print(*tokenized_sentences[j], sep=" ");
                print(tokenized_sentences[j])
                print("")
                result.append([tokenized_sentences[j], tags, -1])

        return result
    except Exception as ex:
        print(ex)
