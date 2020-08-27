import os
import sys
sys.path.append(os.path.dirname(__file__))

from libs.AbstractLanguageDetectionModel import AbstractLanguageDetectionModel
from libs.langfromchars.mobi.LangFromChars import LangFromChars


class LangFromCharsModel(AbstractLanguageDetectionModel):

    def __init__(self):
        AbstractLanguageDetectionModel.__init__(self, "LangFromChars")
        self.model = LangFromChars()


    def predict(self, text):
        pred = self.model.predict(text)
        return pred[0]


    def predict_probability(self, text):
        pred = self.model.predict_language_with_propa(text)
        return {"language": pred[0], "probability": pred[1]}
