# myvar = "Hello"
# myvar2 = myvar
# print(myvar, myvar2)
# print("Print variable types:", type(myvar), type(myvar2))
# print("Are vaules the same?", myvar == myvar2)
# print("Is this the same variable?", myvar is myvar2)
# print("Print id's: ", id(myvar), id(myvar2)) #ten sam obiekt, ta sama pamięć wiec id takie same
#
# myvar2 = myvar+"NEW"
# print(myvar, myvar2)
# print("Print variable types:", type(myvar), type(myvar2))
# print("Are vaules the same?", myvar == myvar2)
# print("Is this the same variable?", myvar is myvar2)
# print("Print id's: ", id(myvar), id(myvar2)) #myvar2 jest innym obiektem, innym miejscem w pamieci
#
#
# myvar2 = myvar2[:-3] #remove laset 3 digits
# print(myvar, myvar2)
# print("Print variable types:", type(myvar), type(myvar2))
# print("Are vaules the same?", myvar == myvar2)
# print("Is this the same variable?", myvar is myvar2)
# print("Print id's: ", id(myvar), id(myvar2)) #myvar2 ma taką sama wartosc jak mayvar ale to już jest inna pamiec po modyfikacji

#lab
# a = b = c = 10
# print("Wartości zmiennych a, b i c:", a, b, c)
# print("Id amiennych a, b i c: ", id(a), id(b), id(c))
# a = 20
# print("Nowe wartosci zmiannych:", a, b, c)
# print("Nowe identyfikatory:", id(a), id(b), id(c) )

# a = b = c = [1, 2, 3] # a, b, c to wskazniki do komórki pamięci z listą
# print(a, b, c)
# print(id(a), id(b), id(c))
# a.append(4) # dodanie do istniejacej zmiennej nowego elementu, to jest ta sama zmienna, modyfikujemy element listy a nie listę więc id listy nie zmieni sie
# print(a, b, c)
# print(id(a), id(b), id(c))

x = 10
y = 10
print(id(x), id(y)) #optymalizator pythona daje im takie same id

y = y + 1 - 1
print(id(x), id(y)) #znowu to samo id dla prostego działania

y = y + 1234567890000 - 1234567890000
print(id(x), id(y))


t = [1,2,3]
print(t)
print(type(t))
print(id(t))
k = t + [5]
print(id(t))
print(id(k))