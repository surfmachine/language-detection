import sys
import os
import pandas as pd

from libs.ModelFactory import ModelFactory
from measure.system.CpuSystemMeter import CpuSystemMeter
from measure.system.TimeSystemMeter import TimeSystemMeter
from measure.system.MemorySystemMeter import MemorySystemMeter
from reports.AbstractReport import AbstractReport

# Add modules to system path, needed when starting the script from the shell
# Furter details see: https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
PACKAGE_PARENT = '../'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

class ReportSystemPerformance(AbstractReport):
    """Report the system performance of the models.

    Sample Output
    -------------
    ReportSystemPerformance
                          Time    CPU  Memory Peak
    LangDetect            4.31   8.33       499253
    LangDetectSpacy      12.83   8.33      1336925
    LangFromStopwords     0.10   8.31       495957
    LangFromChars        65.28  17.18    282294433
    AzureTextAnalytics  146.70   1.18       594964
    Time elapsed: 700.58 sec

    Report saved to: outcome/ReportSystemPerformance.csv
    """

    def __init__(self):
        AbstractReport.__init__(self, "ReportSystemPerformance")
        self.model = None
        self.csv_file = "articles_all_1k.csv"


    def eval(self,all):
        # init
        models = ModelFactory().create(all_models=all);
        col_names = ['Time', 'CPU', 'Memory Peak']
        row_names = []
        rows = []
        # measure performance
        for self.model in models:
            print("> start evaluate", self.model.library_name, "...")
            # time
            meter = TimeSystemMeter()
            time = meter.measure(self._func)
            print("  > time", time)
            # cpu
            meter = CpuSystemMeter()
            cpu = meter.measure(self._func)
            print("  > cpu", cpu)
            # memory
            meter = MemorySystemMeter()
            memory = meter.measure(self._func)
            print("  > memory", memory)
            # add row
            row = [time, cpu, memory['peak']]
            row_names.append(self.model.library_name)
            rows.append(row)
        # create and return result
        df = pd.DataFrame(rows, row_names, col_names)
        return df


    def _func(self):
        df = pd.read_csv(self.csv_path + self.csv_file, sep=',')
        for idx, row in df.iterrows():
            text = row['content']
            self.model.predict(text)

#
# Show report
#
report = ReportSystemPerformance()
report.show(all=False, save=False)
