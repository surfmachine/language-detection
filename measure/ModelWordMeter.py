from measure.WordProvider import WordProvider

class ModelWordMeter:
    """Model Word Meter to measure the prediction score per number or words in a sentence."""

    def __init__(self, max_nr_of_words=20, debug=False):
        self.max_nr_of_words = max_nr_of_words
        self.debug = debug
        self.errors = 0
        self.provider = WordProvider()


    def score_df(self, model, df):
        # init
        self.errors = 0
        scores= [0] * self.max_nr_of_words
        number_of_rows = len(df.index)
        # predict scores of each row
        for idx, row in df.iterrows():
            # init row data
            lang = row['lang']
            text = row['content']
            self.provider.load(text)
            # predict row scores per number of words
            for i in range(self.max_nr_of_words):
                nr_of_words = i+1
                t = self.provider.join(nr_of_words)
                score = self.predict(model, lang, t)
                scores[i] = scores[i] + score
        # calculate average scores per word
        for i in range(self.max_nr_of_words):
            scores[i] = scores[i] / number_of_rows
        # return result
        return scores


    def score(self, model, lang, text):
        # init
        self.errors = 0
        self.provider.load(text)
        scores= [0] * self.max_nr_of_words
        # predict for different number of words
        for i in range(self.max_nr_of_words):
            nr_of_words = i+1
            t = self.provider.join(nr_of_words)
            score = self.predict(model, lang, t)
            scores[i] = scores[i] + score
        # return scores per word
        return scores


    def predict(self, model, lang, text):
        try:
            pred = model.predict(text)
            if (pred == lang):
                return 1
        except:
            self.errors = self.errors + 1
            if self.debug:
                print("ModelWordMeter Error predicting: ", text)
        return 0