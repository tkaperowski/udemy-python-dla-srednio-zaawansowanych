ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = ((a, b) for a in ports for b in ports)
i = 0
# print(next(routes))
for a,b in routes: # też może być po tuplach: for x in routes
    print(a,b)
    i += 1

print(f'i = {i}')

routes = ((a, b) for a in ports for b in ports if a != b)
i = 0
for a, b in routes:
    print(a, b)
    i += 1
print('i = {}'.format(i))

routes = ((a,b) for a in ports for b in ports if a > b) # może byc < lub >, taki sam wynik daje
i=0
for a,b in routes:
    print(a,b)
    i+=1
print(f'i = {i}')
