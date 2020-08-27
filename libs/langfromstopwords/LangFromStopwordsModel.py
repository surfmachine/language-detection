import os
import sys
sys.path.append(os.path.dirname(__file__))

from libs.AbstractLanguageDetectionModel import AbstractLanguageDetectionModel
from libs.langfromstopwords.mobi.LangFromStopwords import LangFromStopwords

class LangFromStopwordsModel(AbstractLanguageDetectionModel):

    def __init__(self):
        AbstractLanguageDetectionModel.__init__(self, "LangFromStopwords")
        self.model = LangFromStopwords()

    def predict(self, text):
        return self.model.predict_single(text)

    def predict_probability(self, text):
        preds = self.model.predict_single(text, True)
        pred = preds[0]
        # evaluate highest probability
        if (len(preds) > 1):
            for p in preds:
                if p[1] > pred[1]:
                    pred = p
        # return result
        return {"language": pred[0], "probability": pred[1]}

