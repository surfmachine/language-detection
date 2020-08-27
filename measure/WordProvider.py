
class WordProvider():

    def __init__(self, *args, **kwargs):
        super(WordProvider, self).__init__(*args, **kwargs)
        self.tokens = None

    def load(self, text):
        self.tokens = text.split()

    def size(self):
        if (self.tokens == None):
            return 0
        return len(self.tokens)

    def range(self):
        return range(self.size()+1)

    def join(self, numberOfWords, separator=' '):
        return separator.join(self.tokens[:numberOfWords])