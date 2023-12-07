var_x = 10
password = "My secret password"

# source = 'var_x + 2'
# source = 'var_x = 2' nie zadziała dla eval bo nie można dawać przypisania (=)pętli itp dla eval

source = 'password'

globalllll = globals().copy() #skopiowanie zmiennych globalnych do zmiennej, to jest słownik
# del globalllll['password'] #usunięcie ze zmienych globalnych zmiennej 'password'

# results = eval(source, globals()) #drugi parametr eval to wskazanie zmiennych globalnych
results = eval(source, globalllll) #drugi parametr eval to wskazanie zmiennych globalnych

print(results)
print(globals())

print(__file__)

#/////////////////////////
#eval jest do prostych rzeczy, przyjmuje tylko wyrażenia do oszacowania
x = 10
result = eval('x + 5')
print(result)
result = eval('x < 20')
print(result)
