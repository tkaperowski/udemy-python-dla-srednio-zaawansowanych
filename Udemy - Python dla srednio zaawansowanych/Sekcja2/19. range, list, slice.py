for i in range(5, 10):
    print(i)

print('-'*30)
for i in range(20, 30, 2):
    print(i)

print('-'*30)
for i in range(10,5,-2):
    print(i)

lista = range(10) # to jest typ range od 0 do 10
print('lista: ', lista, type(lista))

lista2 = list(range(10)) # konwertowanie na typ lista
print('lista2: ', lista2, type(lista2), id(lista2))

print(lista2[5:7]) #od 5 do 7 i ostatni 7 pomijany
print(lista2[5:]) #od 5 do końca
print(lista2[:-1]) #bez ostatniego
print(lista2[-1]) #tylko ostatni
print(lista2[0:6:2])
print(lista2[-1:]) #lista z ostatnim elementem
print(lista2[-1:]) #lista z ostatnim elementem
print(lista2[-1:0:-1]) #odwraca, bo od końca -1, do początku 0 ale bez 0, i zmniejsza o -1
print(lista2[-1::-1]) #odwrócona całkowicie bez pomijania ostatniego czyli pierwszego

lista3 = lista2 #robi druga nazwe do tej samej zmiennej
print('lista3: ', lista3, type(lista3), id(lista3))
lista3.append(10)
print('lista2: ', lista2, type(lista2), id(lista2))
print('lista3: ', lista3, type(lista3), id(lista3))

lista4 = lista2.copy()
print('lista4', lista4, type(lista4), id(lista4))

lista10 = lista2[:] #robi kopię jak copy()
print(id(lista10))

isService = True

if isService == False:
    print('wynik if jest true')
else:
    print('wynik if jest false')
n=2
listax = lista3.copy()
listax = listax[:n]
print(listax)
