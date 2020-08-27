import os
import sys
sys.path.append(os.path.dirname(__file__))

class AbstractLanguageDetectionModel:
    """Common language detetcion interface for all library models.

    For each library a wrapper class will be written as subclass of this one. This way we have a common "interface" for all
    libraries to test. This approach is choosen since python has no real interfaces like Java or C-Sharp.
    """

    def __init__(self, library_name):
        self.library_name = library_name


    def predict(self, text):
        """Predict the language code for the given text.
        Args:
            text (str): The text to predict the language of.
        Returns:
            str: The language code (ISO-639-1)
        """
        raise NotImplementedError("The method is not implemented yet.")


    def predict_probability(self, text):
        """Predict the language code and the probability for the given text.
        Args:
            text (str): The text to predict the language of.
        Returns:
            dict: The language code (ISO-639-1) and the probability/score of the prediction.
                  Sample: {'language': 'de', 'probability': 0.935}
        """
        raise NotImplementedError("The method is not implemented yet.")


    def predict_probability_is_supported(self):
        """Indicate if the predict of the probability is supported by the model."""
        return True