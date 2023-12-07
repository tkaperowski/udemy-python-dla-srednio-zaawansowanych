listA = list(range(6))
listB = list(range(6))

listy = [(a, b) for a in listA for b in listB if a % 2 == 1 if b % 2 == 0]
print(listy)

gen = ((a, b) for a in listA for b in listB if a % 2 == 1 if b % 2 == 0)
print(gen) # generator to zapis jak generować elementy z listy, to nie dane a funkcja/sposób jak te dane wygenerować, zajmuje mniej pamięci niż te wieeelkie dane


print(next(gen)) #generuje 1szą wartość itd.
print(next(gen))
print('-'*30)

for x in gen:
    print(x)
print('/'*30)
for x in gen:
    print(x)
print('tu widać że generator się skończył, wygenerował wszystko co miał do zrobienia więc druga pętla for nic nie zwraca')

new_gen = ((a, b) for a in listA for b in listB if a % 2 == 1 if b % 2 == 0)
while True:
    print(next(new_gen))


