import os
import sys
import tracemalloc
sys.path.append(os.path.dirname(__file__))

from measure.system.AbstractSystemMeter import AbstractSystemMeter


class MemorySystemMeter(AbstractSystemMeter):

    def __init__(self):
        AbstractSystemMeter.__init__(self, "Memory")
        self.snapshot = None


    def _start(self):
        tracemalloc.start()
        self.snapshot = tracemalloc.take_snapshot()


    def _stop(self):
        snapshot2 = tracemalloc.take_snapshot()
        current, peak = tracemalloc.get_traced_memory()
        stats = snapshot2.compare_to(self.snapshot, 'lineno')
        tracemalloc.stop()
        return {
            "current" : current,
            "peak"    : peak,
            "stats"   : stats
        }
