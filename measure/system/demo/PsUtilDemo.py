import sys
import os

# Add modules to system path, needed when starting the script from the shell
# Furter details see: https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
PACKAGE_PARENT = '../../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import psutil

from libs.ModelFactory import ModelFactory
from measure.ModelMeter import ModelMeter


# =============================================================================
# Explore some psutil commands.
# Further details see https://pypi.org/project/psutil.
# =============================================================================

print("------------------------------------------------------------------------")
print("CPU")
print("------------------------------------------------------------------------")

print("cpu_times")
res = psutil.cpu_times()
print(res)                            # scputimes(user=21397.859375, system=12034.5, idle=407200.515625, interrupt=1433.5, dpc=839.65625)
print("")


print("cpu_percent")
for x in range(3):
    res = psutil.cpu_percent(interval=1)
    print(res)
print("")


print("cpu_percent per cpu")
for x in range(3):
    res = psutil.cpu_percent(interval=1, percpu=True)
    print(res)
print("")


print("cpu_count")
res = psutil.cpu_count()
print(res)
print("")


print("cpu_count logical=False")
res = psutil.cpu_count(logical=False)
print(res)
print("")


print("------------------------------------------------------------------------")
print("Memory")
print("------------------------------------------------------------------------")

print("virtual_memory")
res = psutil.virtual_memory()
print(res)
print("")


print("swap_memory")
res = psutil.swap_memory()
print(res)
print("")


print("------------------------------------------------------------------------")
print("Test")
print("------------------------------------------------------------------------")

psutil.test()

print("------------------------------------------------------------------------")
print("CPU of current process")
print("------------------------------------------------------------------------")

print("p.cpu_percent")
p = psutil.Process()
print(p)
for x in range(3):
    res = p.cpu_percent(interval=1)
    print(res)

print("psutil.cpu_percent")
for x in range(3):
    res = psutil.cpu_percent(interval=1)
    print(res)

print("------------------------------------------------------------------------")
print("Analyse Modell")
print("------------------------------------------------------------------------")

models = ModelFactory().create()
meter = ModelMeter()
csv_path = "../../../data/transform/"
csv_file = "articles_all_1k.csv"

p = psutil.Process()
print(p)

for model in models:
    print(model.library_name)

    # init cpu_percent, result is meaningless
    res = p.cpu_percent(interval=None)
    print(res)

    meter.eval(model, csv_path + csv_file)

    # Note cpu_percent:
    # the returned value can be > 100.0 in case of a process running multiple threads on different CPU cores.
    res = p.cpu_percent(interval=None)
    print(res / psutil.cpu_count() )

