import unittest

from measure.WordProvider import WordProvider

class WordProviderTest(unittest.TestCase):

    def test(self):
        wp = WordProvider()
        wp.load("Hello World.")
        self.assertEqual("Hello", wp.join(1))
        self.assertEqual("Hello World.", wp.join(2))
        self.assertEqual("Hello World.", wp.join(99))

    def test_size(self):
        wp = WordProvider()
        self.assertEqual(0, wp.size())
        wp.load("One two three")
        self.assertEqual(3, wp.size())

    def test_range(self):
        wp = WordProvider()
        wp.load("One two three")
        for i in wp.range():
            self.assertTrue(i <= 3)
            if (i == 1):
                self.assertEqual("One", wp.join(i))
            if (i == 2):
                self.assertEqual("One two", wp.join(i))
            if (i == 3):
                self.assertEqual("One two three", wp.join(i))

