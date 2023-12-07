import math



print(0/10)

argument_list = []
i = 0.0 #0 to int 0.0 to float, zmiennoprzecinkowa
while i < 10:
    argument_list.append(i)
    i += 0.1
    i = round(i,1)
print(len(argument_list), argument_list)

argument_list = []
for i in range(100):
    argument_list.append(i / 10)
print(len(argument_list), argument_list)

formula = input('Wprowadz wzór:\n')
x=0
wzor = '2*x'

for x in argument_list:
    print(eval(wzor))

formula = input("Please enter a formula, use 'x' as the argument: ")

for x in argument_list:
    print(x)
    print("{:3.1f} {:4.2f}".format(x, eval(formula)))