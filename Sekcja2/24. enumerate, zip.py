workDays = [19, 21, 22, 25, 27]

enumerateDays = enumerate(workDays)
print(list(enumerateDays))

for pos, val in list(enumerate(workDays)):
    print('Position: ', pos, ' Value: ', val)

months = ['styczeń', 'luty', 'marzec', 'kwiecien', 'maj']

monthsDays = zip(months, workDays)
print(monthsDays)
print(list(monthsDays))


for pos, (month, days) in enumerate(zip(months, workDays)):
    print('Position:', pos, 'Month:', month, 'Days:', days)