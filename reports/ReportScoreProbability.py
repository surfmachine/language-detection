import os
import sys
import pandas as pd

from libs.ModelFactory import ModelFactory
from reports.AbstractReport import AbstractReport
from measure.ModelMeter import ModelMeter
from measure.StopWatch import StopWatch

# Add modules to system path, needed when starting the script from the shell
# Furter details see: https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
PACKAGE_PARENT = '../'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

class ReportScoreProbability(AbstractReport):
    """Report the score probability per sample and the hits (if prediction is True or False) per sample.

    Sample Output
    -------------
    ReportScoreProbability

    Probabilities
                             0         1         2    ...       997       998       999
    LangDetect          0.999995  0.999996  0.999999  ...  0.999998  0.999996  0.999998
    LangDetectSpacy     0.999997  0.999998  0.999997  ...  0.999996  0.999995  0.999997
    LangFromStopwords   1.000000  0.700000  0.636364  ...  0.666667  0.625000  0.444444
    LangFromChars       0.999421  0.999902  0.995568  ...  0.999976  0.853367  0.997942
    AzureTextAnalytics  0.882353  1.000000  1.000000  ...  1.000000  1.000000  1.000000
    [5 rows x 1000 columns]

    Hits
                         0     1     2     3     4    ...   995   996   997   998   999
    LangDetect          True  True  True  True  True  ...  True  True  True  True  True
    LangDetectSpacy     True  True  True  True  True  ...  True  True  True  True  True
    LangFromStopwords   True  True  True  True  True  ...  True  True  True  True  True
    LangFromChars       True  True  True  True  True  ...  True  True  True  True  True
    AzureTextAnalytics  True  True  True  True  True  ...  True  True  True  True  True
    [5 rows x 1000 columns]

    Time elapsed: 219.37 sec
    Report saved to: outcome/ReportScoreProbabilityProbabilities.csv
    Report saved to: outcome/ReportScoreProbabilityHits.csv
    """

    def __init__(self):
        AbstractReport.__init__(self, "ReportScoreProbability")
        self.meter = ModelMeter()
        self.csv_file = "articles_all_1k.csv"


    def eval(self, all):
        # init
        models = ModelFactory().create(all_models=all)
        row_names = []
        probs = []
        hits  = []
        # predict
        for idx, model in enumerate(models):
            print("> start evaluate", model.library_name, "...")
            result = self.meter.eval_probs(model, self.csv_path + self.csv_file)
            row_names.append(model.library_name)
            probs.append(result['probs'])
            hits.append(result['hits'])
        # create df's
        col_names = list(range(len(probs[0])))
        df_probs = pd.DataFrame(probs, row_names, col_names)
        df_hits  = pd.DataFrame(hits, row_names, col_names)
        return {"df_probs":df_probs, "df_hits":df_hits}


    def show(self, all=False, save=False):
        print(self.report_name)
        sw = StopWatch()
        sw.start()
        result = self.eval(all)
        sw.stop()
        # print results and elapsed time
        print("\n")
        print(self.report_name)
        print("Probabilities")
        print(result['df_probs'])
        print("Hits")
        print(result['df_hits'])
        print("Time elapsed:", sw.elapsed(), "sec")
        if save:
            file = self.outcome_path + self.report_name + "Probabilities" + self.outcome_ext
            self.save_csv_file(result['df_probs'], self.index_label, file)
            file = self.outcome_path + self.report_name + "Hits" + self.outcome_ext
            self.save_csv_file(result['df_hits'], self.index_label, file)

#
# Show report
#
report = ReportScoreProbability()
report.show(all=False, save=False)
