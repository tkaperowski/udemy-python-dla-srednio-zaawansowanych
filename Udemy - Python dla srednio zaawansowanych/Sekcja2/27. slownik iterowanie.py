workDays = [19, 21, 22, 21, 20, 22]
months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthDays = dict(zip(months, workDays))
print(monthDays)

# for key, value in months: # to zwróci błąd (not enough values to unpack) bo slownik ma jedną vartość key:value w odrużnieniu od listy która ma dwie wartości
for key in monthDays:
    print('Key is', key, 'value is', monthDays[key])

for value in monthDays.values():
    print(value)

for key in monthDays.keys():
    print(key)

for k, v in monthDays.items(): #items wyciąga parę klucz-wartosc
    print(k, v)