ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = []

for a in ports:
    for b in ports:
        if a != b:
            routes.append((a,b))

#to samo by list comprehension
routes = [(a, b) for a in ports for b in ports if a != b]
print(routes)

for a in ports:
    for b in ports:
        if a < b:
            print(a, 'jest mniejsze od', b)


routes = [(a, b) for a in ports for b in ports if a != b]
print(routes)

if a < b:
    print(a, 'jest mniejsze od', b)