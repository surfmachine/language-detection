import os
import sys
import pandas as pd

from libs.ModelFactory import ModelFactory
from measure.ModelWordMeter import ModelWordMeter
from reports.AbstractReport import AbstractReport

# Add modules to system path, needed when starting the script from the shell
# Furter details see: https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
PACKAGE_PARENT = '../'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

class ReportScorePerWord(AbstractReport):
    """Report the score of each model per number of words from 1 to 20.

    Sample Output
    -------------
    ReportScorePerWord
                        1      2      3      4   ...     17     18     19     20
    LangDetect          0.339  0.525  0.664  0.757  ...  0.983  0.986  0.984  0.985
    LangDetectSpacy     0.344  0.531  0.665  0.748  ...  0.984  0.984  0.985  0.984
    LangFromStopwords   0.308  0.505  0.625  0.704  ...  0.973  0.981  0.981  0.981
    LangFromChars       0.391  0.538  0.692  0.768  ...  0.945  0.949  0.947  0.948
    AzureTextAnalytics  0.566  0.754  0.847  0.888  ...  0.987  0.987  0.988  0.990
    [5 rows x 20 columns]

    Time elapsed: 3887.51 sec
    Report saved to: outcome/ReportScorePerWord.csv
    """

    def __init__(self):
        AbstractReport.__init__(self, "ReportScorePerWord")
        self.meter = ModelWordMeter()
        self.csv_file = "articles_all_1k.csv"


    def eval(self, all):
        # init
        models = ModelFactory().create(all_models=all);
        col_names = list(range(1, self.meter.max_nr_of_words+1))
        row_names = []
        rows = []
        # read test data
        data = pd.read_csv(self.csv_path + self.csv_file, sep=',')
        # predict scores per number of words for each model
        for i, model in enumerate(models):
            print("> start evaluate", model.library_name, "...")
            row = self.meter.score_df(model, data)
            row_names.append(model.library_name)
            rows.append(row)
        # create and return result
        df = pd.DataFrame(rows, row_names, col_names)
        return df


#
# Show report
#
report = ReportScorePerWord()
report.show(all=False, save=False)
