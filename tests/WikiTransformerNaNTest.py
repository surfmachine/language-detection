import sys
import unittest
import pandas as pd

class WikiTransformerNaNTest(unittest.TestCase):
    """Test the content of the generated CSV files. The conent must not be empty (NaN). """

    def __init__(self, *args, **kwargs):
        super(WikiTransformerNaNTest, self).__init__(*args, **kwargs)
        self.csv_files = [
            "../data/transform/articles_all_100k.csv",
            "../data/transform/articles_de_100k.csv",
            "../data/transform/articles_fr_100k.csv",
            "../data/transform/articles_it_100k.csv",
            "../data/transform/articles_en_100k.csv"
        ]
        self.debug = True


    def test_csv_content(self):
        for csv_file in self.csv_files:
            if (self.debug):
                print("Test for NaN content in file:", csv_file)
            df = pd.read_csv(csv_file, sep=',')
            for idx, row in df.iterrows():
                try:
                     text = row['content']
                     self.assertTrue(len(text) > 1)
                except:
                    if (self.debug):
                        print("Unexpected error:", sys.exc_info()[0])
                        print("idx ", idx)
                        print("id  ", row['id'])
                        print("lang", row['lang'])
                        print("url ", row['url'])
                        print("text", row['content'])
                    else:
                        raise
