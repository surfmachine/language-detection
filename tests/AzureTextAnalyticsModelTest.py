import unittest
from libs.azuretextanalytics.AzureTextAnalyticsModel import AzureTextAnalyticsModel


class AzureTextAnalyticsModelTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(AzureTextAnalyticsModelTest, self).__init__(*args, **kwargs)
        self.model = AzureTextAnalyticsModel()
        self.debug = True


    def test_predict(self):
        result = self.model.predict("Hello World")
        self.assertEqual("en", result)
        if self.debug:
            print("test_predict:")
            print(result)


    def test_predict_probability_is_supported(self):
        result = self.model.predict_probability_is_supported()
        if self.debug:
            print("test_predict_probability_is_supported:")
            print(result)


    def test_predict_probability(self):
        result = self.model.predict_probability("Hello World")
        self.assertEqual("en", result['language'])
        self.assertEqual(1.0, result['probability'])
        if self.debug:
            print("test_predict_probability:")
            print(result)
