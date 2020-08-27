import unittest
import pandas as pd
from libs.azuretextanalytics.AzureDataHandler import AzureDataHandler


class AzureDataHandlerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(AzureDataHandlerTest, self).__init__(*args, **kwargs)
        self.handler = AzureDataHandler()
        self.debug = True


    def test_create_document(self):
        documents = self.handler.create_document("Hello World", 11)
        self.assertEqual(1, len(documents['documents']))
        if self.debug:
            print("test_create_document:")
            print(documents)


    def test_create_documents(self):
        csv_file = "data/articles_test_10.csv"
        df = pd.read_csv(csv_file, sep=',')
        documents = self.handler.create_documents(df)
        self.assertEqual(10, len(documents['documents']))
        if self.debug:
            print("test_create_documents:")
            print(documents)


    def test_extract_result(self):
        response = self._create_response()
        result = self.handler.extract_result(response)
        self.assertEqual("de", result['language'])
        self.assertEqual(0.88, result['probability'])
        if self.debug:
            print("test_extract_result:")
            print(result)


    def test_extract_results(self):
        response = self._create_response()
        results = self.handler.extract_results(response)
        self.assertEqual(3, len(results))
        if self.debug:
            print("test_extract_results:")
            print(results)


    def _create_response(self):
        return {
            "documents": [
                {
                    "detectedLanguages": [
                        {
                            "iso6391Name": "de",
                            "name": "German",
                            "score": 0.88
                        }
                    ],
                    "id": "de:1"
                },
                {
                    "detectedLanguages": [
                        {
                            "iso6391Name": "fr",
                            "name": "French",
                            "score": 0.99
                        }
                    ],
                    "id": "fr:3"
                },
                {
                    "detectedLanguages": [
                        {
                            "iso6391Name": "it",
                            "name": "Italian",
                            "score": 1.0
                        }
                    ],
                    "id": "it:2"
                },
            ],
            "errors": []
        }
