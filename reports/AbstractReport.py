import os
import sys
sys.path.append(os.path.dirname(__file__))

from libs.ModelFactory import ModelFactory
from measure.StopWatch import StopWatch

class AbstractReport:
    """Common report interface for all the reports.

    The class defines some common helper methods used by all reports.
    Further more it defines a common interface implemented by all reports.

    This approach is choosen since python has no real interfaces like Java or C-Sharp.
    """

    def __init__(self, report_name, index_label="Model"):
        self.report_name = report_name
        self.index_label = index_label
        self.csv_path = "../data/transform/"
        self.outcome_path = "outcome/"
        self.outcome_ext = ".csv"


    def eval(self, all=False):
        raise NotImplementedError("The method is not implemented yet.")

    def load_models(self, all):
        return ModelFactory().create(all_models=all)

    def show(self, all=False, save=False):
        print(self.report_name)
        sw = StopWatch()
        sw.start()
        df = self.eval(all)
        # print result and elapsed time
        print("\n")
        print(self.report_name)
        print(df)
        sw.stop()
        print("Time elapsed:", sw.elapsed(), "sec")
        if save:
            self.save_csv(df, self.index_label)


    def save_csv(self, df, index_label):
        file = self.outcome_path + self.report_name + self.outcome_ext
        df.to_csv(file, index_label=index_label)
        print("\nReport saved to:",file)

    def save_csv_file(self, df, index_label, file):
        df.to_csv(file, index_label=index_label)
        print("\nReport saved to:", file)
