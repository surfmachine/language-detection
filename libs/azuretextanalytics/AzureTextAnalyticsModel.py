import os
import sys
import uuid
import requests
sys.path.append(os.path.dirname(__file__))

from libs.azuretextanalytics.Environment import Environment
from libs.azuretextanalytics.AzureDataHandler import AzureDataHandler
from libs.AbstractLanguageDetectionModel import AbstractLanguageDetectionModel

class AzureTextAnalyticsModel(AbstractLanguageDetectionModel):

    def __init__(self):
        AbstractLanguageDetectionModel.__init__(self, "AzureTextAnalytics")
        self.env = Environment()
        self.handler = AzureDataHandler()


    def predict(self, text):
        result = self._call_service(text)
        return result['language']


    def predict_probability(self, text):
        result = self._call_service(text)
        return result


    def _call_service(self, text):
        # prepare request
        headers = self._create_headers()
        body = self.handler.create_document(text)
        url = self.env.getAzureTextAnalyticsServiceUrl()
        # call service
        request = requests.post(url, headers=headers, json=body)
        # extract response
        response = request.json()
        result = self.handler.extract_result(response)
        # return result
        return result


    def _create_headers(self):
        subscription_key = self.env.getAzureCognitiveServiceKey()
        xclient_trace_id = str(uuid.uuid4())
        headers = {
            'Content-type': 'application/json',
            'Ocp-Apim-Subscription-Key': subscription_key,
            'X-ClientTraceId': xclient_trace_id
        }
        return headers
