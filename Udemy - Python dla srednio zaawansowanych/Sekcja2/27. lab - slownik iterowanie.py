banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
dict_denominations = {}
for r in banknotes_coins:
    dict_denominations[r] = 0

print(dict_denominations)

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1000
dict_denominations[2] += 1

print(dict_denominations)
for key in dict_denominations:
#{:6} szerokość liczby to 6 znaków, jeśli krotsza liczby to dodaje spacje z przodu, .2f to ilość miejsc po rpzecinku
    print('Denominate: {:6.2f} - amount {:5}'.format(key, dict_denominations[key]))

for k, v in dict_denominations.items():
    print(f'Denominate: {k:6.2f} - amount {v:5}')