projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

zszyte = list(zip(projects, leaders)) #po zip trzeba od razu konwertować na liste bo inaczej zostanie wyczerpany obiekt zip np przez komendę print, ptzykład poniżej
slownik = dict(zip(projects, leaders))
print(zszyte)
print(slownik)
# zszyte = zip(projects, leaders)
# print(list(zszyte))
# print(list(zszyte)) #ten print da już pustą listę

for p, l in zszyte:
    print('The leader of', p, 'is', l)

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

potrojne = list(zip(projects, dates, leaders))
for l, d, p in potrojne:
    print('The leader of', f'"{p}"', 'started', d, 'is', p)


for e, (p, d, l) in enumerate(zip(projects, dates, leaders)):
    print(e, '- The leared of', f'"{p}" started', d, 'is', l)