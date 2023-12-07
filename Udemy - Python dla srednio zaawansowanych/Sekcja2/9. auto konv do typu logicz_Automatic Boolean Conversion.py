# isOk = True
# isOk = 'True'
# isOk = -1
# isOk = 0
isOk = [0,1,0]
print("Variable isOk: ", isOk, type(isOk))
# if isOk:
if isOk[1]:
    print('TRUE')

with open(r'd:\udemy\services.txt') as f:
    line = f.readline()
    while(line):
        print(line, id(line))
        # print(line.upper())
        line = f.readline()
        print(line, id(line))

listOfErrors = []
print(listOfErrors, id(listOfErrors))
listOfErrors.append(1)
print(listOfErrors, id(listOfErrors))
print('Variable listOfErrors: ', listOfErrors, type(listOfErrors))
if len(listOfErrors) > 0:
    print('Errors!!!')



def DisplayOptions(listaOpcji, user_input):
    print('1 -', listaOpcji[0])
    print('2 -', listaOpcji[1])
    print('3 -', listaOpcji[2])
    user_input = input('Select option above or press enter to exit: ')
    return user_input

options = ['load data', 'export data', 'analyze & predict']
choice = 'x'

while choice:
    choice = DisplayOptions(options, choice)
    if choice:
        print(choice, 'choice ma true bo nie jest pusta')
        try:
            choice_num = int(choice)
            if 0 < choice_num <= len(options):
                print('wybrano:', options[choice_num-1], '\n')
            else:
                print('wybrano złą opcję\n')
        except:
            print('wprowadz liczbę!!!\n')

    else:
        print(choice, 'choice jest puste, ma false bo nic nie ma, baran wcisnal enter, koniec programu!!!')
