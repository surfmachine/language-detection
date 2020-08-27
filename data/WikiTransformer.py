import sys
import csv
from pathlib import Path

class WikiTransformer():
    """Transform and prepare Wiki data."""

    def __init__(self, min_doc_lines=10, max_content_size=120, max_articles=1000):
        self.min_doc_lines = min_doc_lines          # Skip articles with less than 10 lines of raw content (inkl. tags, header, emtpy lines)
        self.max_content_size = max_content_size    # Maximal size of the cleand and prepared article content
        self.max_articles = max_articles            # Maximal number of articles
        self.articles = []


    def read_file(self, path, file, encoding="utf-8"):
        path = Path(path)
        pf = path/file
        with open(pf, "r", encoding=encoding) as f:
            content = f.read()
        return content


    def transform(self, lang, docs, append=True):
        if (append == False):
            self.articles = []

        for doc in docs.split("</doc>"):
            raw_lines = doc.split("\n")

            # skip articles with less than min doc lines
            if (len(raw_lines) < self.min_doc_lines):
                continue

            # extract article
            content = ""
            first = True
            for raw_line in raw_lines:

                # remove leading and trailing blanks and skip empty lines
                line = raw_line.strip()
                if (len(line) == 0):
                    continue

                # parse doc attributes
                if ( line.startswith("<doc") ):
                    article_id = self._extraxt_attr(line, "id")
                    title = self._extraxt_attr(line, "title")
                    url = self._extraxt_attr(line, "url")
                    continue

                # skip title line
                if (line == title):
                    continue

                # clean content
                line = self._clean_content(line)

                # add content until MAX_SIZE is reached
                if (len(content) >= self.max_content_size):
                    break

                if first:
                    content = line
                    first = False
                else:
                    content = content + ' ' + line

            # create article and add to list
            if (len(content) != 0):
                article = {"id":article_id, "lang":lang, "url":url, "title":title, "content":content[:self.max_content_size]}
                self.articles.append(article)

            # check maximal article count
            if (len(self.articles) >= self.max_articles):
                break

        # return result
        return self.articles


    def write_csv(self, path, file, encoding="utf-8"):
        csv_columns = ["id", "lang", "url", "title", "content"]
        csv_file = Path(path)/file
        article = {}
        try:
            with open(csv_file, 'w', encoding=encoding, newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for article in self.articles:
                    writer.writerow(article)
        except: # catch all
            e = sys.exc_info()[0]
            print("Error  : {0}".format(e))
            print("Article: {0}".format(article) )


    def max_articles_reached(self):
        return (len(self.articles) >= self.max_articles)

    def _extraxt_attr(self, doc, attr):
        """Extract an attribute value from the text document.

        Sample:
        doc = '<doc id="1" url="https://de.wikipedia.org/wiki?curid=1" title="Alan Smithee">"'
        id_value =  extract_attr(doc, 'id')
        title_value = extract_attr(doc, 'title')
        """
        start = doc.index(attr) + len(attr) + 2
        end = doc.index('"', start)
        return doc[start:end]


    def _clean_content(self, line):
        # eliminate double quotes
        result = line.replace('"', '')
        # replace multi spaces with one (without a regex)
        result = ' '.join(result.split())[0:]
        # return cleaned content
        return result


