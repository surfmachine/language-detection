import time
from resource import *

# =============================================================================
# Explore some python resource commands.
# Further details see https://docs.python.org/3/library/resource.html.
#
# Note: This is a Unix Specific Services, does NOT work on Windows.
# =============================================================================

print("------------------------------------------------------------------------")
print("CPU")
print("------------------------------------------------------------------------")

# a non CPU-bound task
time.sleep(3)
print(getrusage(RUSAGE_SELF))

# a CPU-bound task
for i in range(10 ** 8):
    _ = 1 + 1
print(getrusage(RUSAGE_SELF))
