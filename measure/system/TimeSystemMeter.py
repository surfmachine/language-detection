import os
import sys
sys.path.append(os.path.dirname(__file__))

from measure.StopWatch import StopWatch
from measure.system.AbstractSystemMeter import AbstractSystemMeter


class TimeSystemMeter(AbstractSystemMeter):

    def __init__(self):
        AbstractSystemMeter.__init__(self, "Time")
        self.stop_watch = StopWatch()


    def _start(self):
        self.stop_watch.start()


    def _stop(self):
        self.stop_watch.stop()
        return float(self.stop_watch.elapsed())
