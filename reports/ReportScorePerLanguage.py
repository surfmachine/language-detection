import os
import sys
import pandas as pd
from libs.ModelFactory import ModelFactory
from measure.ModelMeter import ModelMeter
from reports.AbstractReport import AbstractReport

# Add modules to system path, needed when starting the script from the shell
# Furter details see: https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
PACKAGE_PARENT = '../'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

class ReportScorePerLanguage(AbstractReport):
    """Report the score of each model per language.

    Sample Output
    -------------
    ReportScorePerLanguage
                           de     fr     it     en
    LangDetect          0.978  0.997  0.990  0.994
    LangDetectSpacy     0.972  0.997  0.991  0.992
    LangFromStopwords   0.977  0.999  0.936  0.994
    LangFromChars       0.903  0.987  0.973  1.000
    AzureTextAnalytics  0.971  0.999  0.996  0.999
    Time elapsed: 857.40 sec

    Report saved to: outcome/ReportScorePerLanguage.csv
    """

    def __init__(self):
        AbstractReport.__init__(self, "ReportScorePerLanguage")
        self.models = ModelFactory().create();
        self.csv_files = [
            "articles_de_1k.csv",
            "articles_fr_1k.csv",
            "articles_it_1k.csv",
            "articles_en_1k.csv"
        ]


    def eval(self, all):
        # init
        models = self.load_models(all)
        col_names = ['de', 'fr', 'it', 'en']
        row_names = []
        rows = []
        # evaluate score
        meter = ModelMeter()
        for i, model in enumerate(models):
            print("> start evaluate", model.library_name, "...")
            row = []
            for csv_file in self.csv_files:
                score = meter.eval_score(model, self.csv_path + csv_file)
                row.append( score )
            row_names.append(model.library_name)
            rows.append(row)
        # create and return result
        df = pd.DataFrame(rows, row_names, col_names)
        return df


#
# Show report
#
report = ReportScorePerLanguage()
report.show(all=False, save=False)
