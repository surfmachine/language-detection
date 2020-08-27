import os
import sys
import pandas as pd
from measure.ModelMeter import ModelMeter
from reports.AbstractReport import AbstractReport

# Add modules to system path, needed when starting the script from the shell
# Furter details see: https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
PACKAGE_PARENT = '../'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

class ReportScore(AbstractReport):
    """Report the score of sample texts and the elapsed time.

    Sample Output
    -------------
    ReportScore
                        Score  Total    Time
    LangDetect            986   1000    3.58
    LangDetectSpacy       985   1000   10.76
    LangFromStopwords     978   1000    0.09
    LangFromChars         952   1000   57.88
    AzureTextAnalytics    991   1000  135.20
    Time elapsed: 208.85 sec

    Report saved to: outcome/ReportScore.csv

    Sample Output 2
    ---------------
    ReportScore
                        Score  Total     Time
    LangDetect           9895  10000    30.21
    LangDetectSpacy      9894  10000   107.76
    LangFromStopwords    9793  10000     0.98
    LangFromChars        9641  10000   573.46
    AzureTextAnalytics   9893  10000  1272.41
    Time elapsed: 1986.26 sec
    """

    def __init__(self):
        AbstractReport.__init__(self, "ReportScore")
        self.meter = ModelMeter()
        self.csv_file = "articles_all_1k.csv"


    def eval(self, all):
        # init
        models = self.load_models(all)
        col_names = ['Score', 'Total', 'Time']
        row_names = []
        rows = []
        # predict
        for model in models:
            print("> start evaluate", model.library_name, "...")
            res = self.meter.eval(model, self.csv_path + self.csv_file)
            row = [res['score'], res['total'], res['time']]
            row_names.append(model.library_name)
            rows.append(row)
        # create and return result
        df = pd.DataFrame(rows, row_names, col_names)
        return df

#
# Show report
#
report = ReportScore()
report.show(all=False, save=False)
