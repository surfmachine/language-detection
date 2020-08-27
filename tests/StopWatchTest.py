import unittest
import time
from measure.StopWatch import StopWatch

class StopWatchTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(StopWatchTest, self).__init__(*args, **kwargs)
        self.debug = True


    def test_none(self):
        sw = StopWatch()
        sw.start()
        self.assertEqual(None, sw.elapsed())


    def test_elapsed(self):
        # init
        sw = StopWatch()
        # test
        sw.start()
        time.sleep(3)
        sw.stop()
        # debug
        if (self.debug):
            print("Test StopWatch:")
            print("Start  ", sw.start_time)
            print("Stop   ", sw.stop_time)
            print("Elapsed", sw.elapsed())
        # check
        self.assertTrue(sw.stop_counter - sw.start_counter >= 2.9) # give some tolerance
