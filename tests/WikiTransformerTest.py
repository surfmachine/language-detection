from pathlib import Path
import unittest
import os

from data.WikiTransformer import WikiTransformer


class WikiTransformerTest(unittest.TestCase):

    def test_default_max_content_size(self):
        wikiTransformer = WikiTransformer()
        self.assertEqual(120, wikiTransformer.max_content_size)


    def test_extraxt_attr(self):
        wikiTransformer = WikiTransformer()
        doc = '<doc id="7" url="https://de.wikipedia.org/wiki?curid=7" title="James Bond">"'
        # extract attributes
        id = wikiTransformer._extraxt_attr(doc, 'id')
        url = wikiTransformer._extraxt_attr(doc, 'url')
        title = wikiTransformer._extraxt_attr(doc, 'title')
        # check content
        self.assertEqual("7", id)
        self.assertEqual("https://de.wikipedia.org/wiki?curid=7", url)
        self.assertEqual("James Bond", title)


    def test_read_file(self):
        wikiTransformer = WikiTransformer()
        content = wikiTransformer.read_file("data", "wiki_test_read_file")
        self.assertEqual("Hello", content)


    def test_transform_article(self):
        wikiTransformer = WikiTransformer()
        docs = wikiTransformer.read_file("data", "wiki_test_article")
        # expect list of articles with 1 article
        articles = wikiTransformer.transform("de", docs)
        self.assertEqual(1, len(articles))
        # expect the following values
        article = articles[0]
        self.assertEqual("1", article["id"])
        self.assertEqual("de", article["lang"])
        self.assertEqual("Alan Smithee", article["title"])
        self.assertEqual(120, len(article["content"]))


    def test_transform_article_clean(self):
        wikiTransformer = WikiTransformer()
        docs = wikiTransformer.read_file("data", "wiki_test_article_clean")
        # expect list of articles with 1 article
        articles = wikiTransformer.transform("de", docs)
        self.assertEqual(1, len(articles))
        # expect the following values
        article = articles[0]
        content = article["content"]
        self.assertEqual("Line 1 Line 2 Line 3", content)


    def test_transform_article_max(self):
        wikiTransformer = WikiTransformer(max_articles=3)
        docs = wikiTransformer.read_file("data", "wiki_test_article_max")
        # expect list of articles with 3 articles
        articles = wikiTransformer.transform("de", docs)
        self.assertTrue(wikiTransformer.max_articles_reached())


    def test_transform_article_skip(self):
        wikiTransformer = WikiTransformer()
        docs = wikiTransformer.read_file("data", "wiki_test_article_skip")
        articles = wikiTransformer.transform("de", docs)
        self.assertEqual(1, len(articles))


    def test_article_nan(self):
        """Während der Messungen gab es CSV Einträge mit leeren Texten (NaN)

        Ursache sind <doc> Texte, bei denen im Inhalt der Titel 2x vorgekommt und kein weiterer Text existiert.
        Damit es keine NaN Einträge in den CSV Dateien gibt, wurden die Transformer Regelen wie folgt angepasst:
        > Artikle mit leeren Texten werden ignoriert, d.h. nicht weiter verarbeitet
        > Der vorliegende Test zeigt, dass der <doc> nicht weiter verarbeitet wird.
        """
        wikiTransformer = WikiTransformer()
        docs = wikiTransformer.read_file("data", "wiki_test_article_nan")
        articles = wikiTransformer.transform("it", docs)
        self.assertEqual(0, len(articles))


    def test_write_csv(self):
        wikiTransformer = WikiTransformer()
        path = "data"
        input_file = "wiki_test_write_csv"
        output_file = "wiki_test_write_csv.csv"
        # remove output file
        fn = Path(path)/output_file
        if os.path.exists(fn):
            os.remove(fn)
        # read file, transform articles and create csv file
        docs = wikiTransformer.read_file(path, input_file)
        articles = wikiTransformer.transform("de", docs)
        wikiTransformer.write_csv(path, output_file)
        # check if file exists
        self.assertTrue(os.path.exists(fn))
