import os
import sys
import psutil
sys.path.append(os.path.dirname(__file__))

from measure.system.AbstractSystemMeter import AbstractSystemMeter


class CpuSystemMeter(AbstractSystemMeter):

    def __init__(self):
        AbstractSystemMeter.__init__(self, "CPU")
        self.process = None


    def _start(self):
        self.process = psutil.Process()
        self.process.cpu_percent(interval=None)


    def _stop(self):
        total_cpu = self.process.cpu_percent(interval=None)
        return format(round(total_cpu / psutil.cpu_count(), 2), '.2f')


