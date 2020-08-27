import tracemalloc
import math

from libs.ModelFactory import ModelFactory
from measure.ModelMeter import ModelMeter

# =============================================================================
# Explore some tracemalloc commands.
# Further details see https://docs.python.org/3/library/tracemalloc.html
# and https://docs.python.org/3/library/tracemalloc.html#display-the-top-10.
# =============================================================================

print("------------------------------------------------------------------------")
print("Display the top 10")
print("------------------------------------------------------------------------")

tracemalloc.start()

# run your application
for i in range(10 ** 4):
    _ = 1 + 1
for i in range(10 ** 4):
    _ = math.sqrt(100 / 25 * 3)


snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:10]:
    print(stat)

tracemalloc.stop()

print("------------------------------------------------------------------------")
print("Compare")
print("------------------------------------------------------------------------")

tracemalloc.start(5)  # save upto 5 stack frames

time1 = tracemalloc.take_snapshot()
ref = 'Sarah ' * 51200
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'lineno')
for stat in stats[:3]:
    print(stat)

tracemalloc.stop()

print("------------------------------------------------------------------------")
print("Analyse Modell")
print("------------------------------------------------------------------------")

models = ModelFactory().create()
meter = ModelMeter()
csv_path = "../../../data/transform/"
csv_file = "articles_all_1k.csv"

for model in models:
    tracemalloc.start()
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB before running model", model.library_name)

    snapshot1 = tracemalloc.take_snapshot()
    meter.eval(model, csv_path + csv_file)
    snapshot2 = tracemalloc.take_snapshot()

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB for model", model.library_name)

    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    print("[ Top 10 differences ]")
    for stat in top_stats[:10]:
        print(stat)

    tracemalloc.stop()
