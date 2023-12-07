import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (10):
    argument_list.append(i/10)

print(argument_list)

results_list = []
for i in formulas_list:
    # results_list = []
    print(i)
    start = time.time()
    x = 0.1
    result = eval(i)
    print(result)

#
#     start = time.time()
#     for x in argument_list:
#         # print(x)
#         result = exec(i)
#         results_list.append(result)
# print(results_list)