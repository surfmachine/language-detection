import unittest

from libs.ModelFactory import ModelFactory
from measure.ModelMeter import ModelMeter

class ModelMeterTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(ModelMeterTest, self).__init__(*args, **kwargs)
        self.debug = True


    def test_probs(self):
        # init
        csv_file = "data/articles_test_10.csv"
        model = ModelFactory().createLangDetect()
        meter = ModelMeter(debug=self.debug)
        # predict
        result = meter.eval_probs(model, csv_file)
        # check results
        self.assertEqual(10, len(result['probs']))
        self.assertEqual(10, len(result['hits']))
        if self.debug:
            print(model.library_name)
            print(result['probs'])
            print(result['hits'])