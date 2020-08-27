import unittest
import pandas as pd

from libs.ModelFactory import ModelFactory
from measure.ModelWordMeter import ModelWordMeter

class ModelWordMeterTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(ModelWordMeterTest, self).__init__(*args, **kwargs)
        self.debug = True


    def test_score(self):
        # init
        lang  = "de"
        text  = "Alan Smithee steht als Pseudonym für einen fiktiven Regisseur."
        max   = len(text.split())
        meter = ModelWordMeter(max_nr_of_words=max, debug=self.debug)
        model = ModelFactory().createLangDetect()
        # predict with 1..max words
        scores = meter.score(model, lang, text)
        # check result
        self.assertEqual(max, len(scores))
        self.assertEqual(0, meter.errors)
        # debug
        if (self.debug):
            print("Test Score:")
            print("- Text  ", text)
            print("- Scores", scores)
            print("- Errors", meter.errors)


    def test_score_with_error(self):
        lang = "it"
        text = "1861: L'unificazione d'Italia"
        max   = len(text.split())
        meter = ModelWordMeter(max_nr_of_words=max, debug=self.debug)
        model = ModelFactory().createLangDetect()
        # predict with 1..max words
        scores = meter.score(model, lang, text)
        # check result
        self.assertEqual(max, len(scores))
        self.assertEqual(1, meter.errors)
        # debug
        if (self.debug):
            print("Test Score with Error:")
            print("- Text  ", text)
            print("- Scores", scores)
            print("- Errors", meter.errors)


    def test_score_df(self):
        # init
        csv_file = "data/articles_test_10.csv"
        df = pd.read_csv(csv_file, sep=',')
        meter = ModelWordMeter(debug=self.debug)
        model = ModelFactory().createLangDetect()
        # predict scores per number of words
        scores = meter.score_df(model, df)
        # check result
        self.assertEqual(20, len(scores))
        self.assertEqual(0, meter.errors)
        # debug
        if (self.debug):
            print("Test Score DF:")
            print("- DF Len", len(df.index))
            print("- Scores", scores)
            print("- Errors", meter.errors)
