import os
import sys
import spacy
sys.path.append(os.path.dirname(__file__))

from spacy_langdetect import LanguageDetector
from libs.AbstractLanguageDetectionModel import AbstractLanguageDetectionModel


class LangDetectSpacyModel(AbstractLanguageDetectionModel):

    def __init__(self):
        AbstractLanguageDetectionModel.__init__(self, "LangDetectSpacy")
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)

    def predict(self, text):
        pred = self.nlp(text)
        return pred._.language["language"]

    def predict_probability(self, text):
        pred = self.nlp(text)
        lang  = pred._.language['language']
        score = pred._.language['score']
        return {"language": lang, "probability": score}
