import os
import sys
sys.path.append(os.path.dirname(__file__))

from libs.AbstractLanguageDetectionModel import AbstractLanguageDetectionModel
from textblob import TextBlob


class TextBlobModel(AbstractLanguageDetectionModel):

    def __init__(self):
        AbstractLanguageDetectionModel.__init__(self, "TextBlob")

    def predict(self, text):
        blob = TextBlob(text)
        pred = blob.detect_language()
        return pred

    def predict_probability(self, text):
        raise NotImplementedError("The method is not supported by the TextBlob API.")


    def predict_probability_is_supported(self):
        return False
