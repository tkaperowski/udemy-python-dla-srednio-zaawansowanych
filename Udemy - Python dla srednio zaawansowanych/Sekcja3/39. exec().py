# exec przyjmuje wiele linijek, eval tylko jedną
var_x = 10

# source = 'var_x + 3' #nie zadziała dla exec bo on nie przyjmuje wyrażeń
source = 'var_x = 100'

result = exec(source)
print(result)
print(var_x)

# exec pozwala wykonać wiele lini kodu
print('x'*30)
x = 10
source = '''
for i in range(10):
    print('*'*i)
'''
result = exec(source)
print(result)

# można definiować nowe zmienne, zauważ że interpreter ich nie widzi i podlreśla bo dopiero się pojawią po wykonaniu kodu w exec
print('-'*30)
source = '''
new_var = 'zmienna nie widaoczna dla pythona, chyba że wykona kod w exec'
'''
result = exec(source)
print(new_var)


# można wykorzystywać funkcje input
print('-'*30)
source = '''
new_var2 = 100
'''
print(exec(source))
print(new_var2)
print(var_x)
result = input('Enter you formula: ') #tu prompty usera zna już zmienną new_var2, możesz wpisać new_var2 * 1000
print(eval(result))

#input zazwyczaj będzie pobierał kod z bazy danych lub pliku