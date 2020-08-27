import pandas as pd

from measure.StopWatch import StopWatch


class ModelMeter:
    """Model Meter to measure the score and elapsed time of a model prediction."""

    def __init__(self, debug=False):
        self.debug = debug


    def eval_score(self, model, csv_file):
        result = self.eval(model, csv_file)
        return result['score'] / result['total']


    def eval(self, model, csv_file):
        # init
        if (self.debug):
            print("Evaluate {0} with {1}".format(model.library_name, csv_file))
        df = pd.read_csv(csv_file, sep=',')
        # init score
        total = len(df.index)
        score = 0
        # predict
        sw = StopWatch()
        sw.start()
        for idx, row in df.iterrows():
            lang = row['lang']
            text = row['content']
            pred = model.predict(text)
            if (lang == pred):
                score = score + 1
        sw.stop()
        # return result
        result = {
            "score" : score,
            "total" : total,
            "time"  : sw.elapsed()
        }
        if (self.debug):
            print(">", result)
        return result


    def eval_probs(self, model, csv_file):
        """ Evaluate the probability of the prediction and if the prediction (hit) was true or false.

        Args:
            model (LanguageDetectionModel): The model to evaluate.
            csv_file (File): The test data as comma separated file
        Returns:
            dict: {
                probs: List with the probabilities of each prediction
                hits:  List with the indications (hits of the prediction (True or False)
            }
        """
        # load data
        if (self.debug):
            print("Evaluate {0} probabilities with {1}".format(model.library_name, csv_file))
        df = pd.read_csv(csv_file, sep=',')
        # init
        row_count = len(df.index)
        probs = [0] * (row_count)
        hits  = [0] * (row_count)
        # predict
        for idx, row in df.iterrows():
            lang = row['lang']
            text = row['content']
            pred = model.predict_probability(text)
            probs[idx] = pred['probability']
            hits[idx]  = (lang == pred['language'])
        # return results
        return {
            "probs": probs,
            "hits" : hits
        }
