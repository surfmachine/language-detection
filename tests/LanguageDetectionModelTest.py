import unittest

from libs.ModelFactory import ModelFactory

class LanguageDetectionModelTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(LanguageDetectionModelTest, self).__init__(*args, **kwargs)
        self.models = ModelFactory().create();
        self.texts = {
            "de" : "Heute ist Mittwoch und das Wetter ist schön",
            "fr" : "Une reprise à petit feu pour les bars et restaurants en France",
            "it" : "Sarebbe troppo bello per essere vero",
            "en" : "War doesn't show who's right, just who's left"
        }
        self.debug = True


    def test_predict(self):
        for model in self.models:
            if (self.debug):
                print("Test prediction with:", model.library_name)
            for key in self.texts:
                text = self.texts[key]
                pred  = model.predict(text)
                if self.debug:
                    print(">", pred, [key==pred], ":", text)
                self.assertEqual(key, pred)


    def test_predict_probability(self):
        for model in self.models:
            if (self.debug):
                print("Test prediction_probability with:", model.library_name)

            if (not model.predict_probability_is_supported()):
                print("> The prediction_probability() methode is not supported by this model")
                continue

            for key in self.texts:
                text = self.texts[key]
                pred  = model.predict_probability(text)
                if self.debug:
                    print(">", pred, [key==pred['language']], ":", text)
                self.assertEqual(key, pred['language'])
                self.assertTrue(pred['probability'] >= 0.5)


