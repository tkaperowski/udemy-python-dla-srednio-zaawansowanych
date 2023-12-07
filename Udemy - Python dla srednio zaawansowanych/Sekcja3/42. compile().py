import time

source = 'reportLine += 1'

reportLine = 0

start = time.time()
for i in range(10000):
    exec(source)
stop = time.time()
time_not_compiled = stop - start
print(time_not_compiled)
print(reportLine)

start = time.time()
sourceCompiled = compile(source, 'internal variable source', 'exec')
for i in range(10000):
    exec(sourceCompiled)
stop = time.time()
time_compiled = stop - start
print(reportLine)
print(time_compiled)