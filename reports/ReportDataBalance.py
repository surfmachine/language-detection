import os
import sys
import pandas as pd
from reports.AbstractReport import AbstractReport

# Add modules to system path, needed when starting the script from the shell
# Furter details see: https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
PACKAGE_PARENT = '../'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

class ReportDataBalance(AbstractReport):
    """Report the balance of the test data.

    Sample Output
    -------------
    ReportDataBalance
                           AvgChars  AvgWords
    articles_de_1k.csv    117.28200  16.80600
    articles_fr_1k.csv    118.25300  19.59900
    articles_it_1k.csv    119.63500  19.00200
    articles_en_1k.csv    119.06300  20.23200
    articles_de_5k.csv    116.99020  16.98880
    articles_fr_5k.csv    112.96760  19.32420
    articles_it_5k.csv    119.23140  19.06840
    articles_en_5k.csv    118.84060  19.97280
    articles_de_10k.csv   116.72290  16.79550
    articles_fr_10k.csv   110.93580  18.47560
    articles_it_10k.csv   119.54950  19.15200
    articles_en_10k.csv   118.95020  19.95050
    articles_de_100k.csv  116.40556  16.75641
    articles_fr_100k.csv  116.93365  19.26814
    articles_it_100k.csv  119.58188  19.04569
    articles_en_100k.csv  118.85534  20.26543
    Time elapsed: 31.16 sec

    Report saved to: outcome/ReportDataBalance.csv
    """

    def __init__(self):
        AbstractReport.__init__(self, "ReportDataBalance", index_label="File")

    def eval(self, all=False):
        # init
        csv_files = self._load_csv_files(all)
        col_names = ['AvgChars', 'AvgWords']
        row_names = csv_files
        rows = []
        # calculate number of chars and words per csv file
        for i, csv_file in enumerate(csv_files):
            data = pd.read_csv(self.csv_path + csv_file, sep=',')
            total = len(data.index)
            chars = 0
            words = 0
            for idx, data_row in data.iterrows():
                text = data_row['content']
                chars = chars + len(text)
                words = words + len(text.split())
            # create and append result row
            row = [chars/total, words/total]
            rows.append(row)
        # create and return result
        df = pd.DataFrame(rows, row_names, col_names)
        return df


    def _load_csv_files(self, all):
        csv_files = [
            "articles_de_1k.csv",
            "articles_fr_1k.csv",
            "articles_it_1k.csv",
            "articles_en_1k.csv",
        ]
        if all:
            csv_files.append("articles_de_5k.csv")
            csv_files.append("articles_fr_5k.csv")
            csv_files.append("articles_it_5k.csv"),
            csv_files.append("articles_en_5k.csv")
            csv_files.append("articles_de_10k.csv")
            csv_files.append("articles_fr_10k.csv")
            csv_files.append("articles_it_10k.csv"),
            csv_files.append("articles_en_10k.csv")
            csv_files.append("articles_de_100k.csv")
            csv_files.append("articles_fr_100k.csv")
            csv_files.append("articles_it_100k.csv"),
            csv_files.append("articles_en_100k.csv")
        return csv_files


#
# Show report
#
report = ReportDataBalance()
report.show(all=False, save=False)
