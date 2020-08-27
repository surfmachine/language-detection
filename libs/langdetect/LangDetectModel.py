import os
import sys
sys.path.append(os.path.dirname(__file__))

from libs.AbstractLanguageDetectionModel import AbstractLanguageDetectionModel
from langdetect import detect
from langdetect import detect_langs


class LangDetectModel(AbstractLanguageDetectionModel):

    def __init__(self):
        AbstractLanguageDetectionModel.__init__(self, "LangDetect")

    def predict(self, text):
        return detect(text)

    def predict_probability(self, text):
        preds = detect_langs(text)
        pred = preds[0]
        # evaluate highest probability
        if (len(preds) > 1):
            for p in preds:
                if (p.prob > pred.prob):
                    pred = p
        # return result
        return {"language": pred.lang, "probability": pred.prob}

