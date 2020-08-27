import unittest
import time

from measure.system.CpuSystemMeter import CpuSystemMeter
from measure.system.TimeSystemMeter import TimeSystemMeter
from measure.system.MemorySystemMeter import MemorySystemMeter

class SystemMeterTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(SystemMeterTest, self).__init__(*args, **kwargs)
        self.debug = True


    def test_cpu(self):
        meter = CpuSystemMeter()
        result = meter.measure(self._func)
        self.assertTrue(float(result) > 0)
        if self.debug:
            print("Test CPU")
            print(result)


    def test_time(self):
        meter = TimeSystemMeter()
        result = meter.measure(self._func_time)
        self.assertTrue(result >= 1.2)
        if self.debug:
            print("Test Time")
            print(result)


    def test_memory(self):
        meter = MemorySystemMeter()
        result = meter.measure(self._func)
        self.assertTrue(result['current'] > 1000)
        self.assertTrue(result['peak'] > 1000)
        self.assertTrue(len(result['stats']) > 3)
        if self.debug:
            print("Test Memory")
            print(result)


    def _func(self):
        for i in range(10 ** 6):
            _dummy = 1 + 1

    def _func_time(self):
        time.sleep(1.2)
