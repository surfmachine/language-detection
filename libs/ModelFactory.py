import os
import sys
sys.path.append(os.path.dirname(__file__))

from libs.azuretextanalytics.AzureTextAnalyticsModel import AzureTextAnalyticsModel
from libs.langfromchars.LangFromCharsModel import LangFromCharsModel
from libs.langdetect.LangDetectModel import LangDetectModel
from libs.langdetectspacy.LangDetectSpacyModel import LangDetectSpacyModel
from libs.langfromstopwords.LangFromStopwordsModel import LangFromStopwordsModel
from libs.textblob.TextBlobModel import TextBlobModel

class ModelFactory():

    def create(self, all_models=False):
        models = [
            LangDetectModel(),
            LangDetectSpacyModel(),
        ]
        if all_models:
            models.append(LangFromStopwordsModel())
            models.append(LangFromCharsModel())
            models.append(AzureTextAnalyticsModel())
        return models


    def createAzureTextAnalytics(self):
        return AzureTextAnalyticsModel()

    def createLangFromStopwords(self):
        return LangFromStopwordsModel()

    def createLangFromChars(self):
        return LangFromCharsModel()

    def createLangDetect(self):
        return LangDetectModel()

    def createLangDetectSpacy(self):
        return LangDetectSpacyModel()

    def createTextBlobModel(self):
        return TextBlobModel()
