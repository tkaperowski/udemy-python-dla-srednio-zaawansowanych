instructions = ['say hello', 'say how are you', 'abort', 'ask for money', 'say thank you', 'say bye']
instructionsApproved = []

for inst in instructions:
    print('Adding instruction to robot: ', inst)
    instructionsApproved.append(inst)
    if inst == 'abort':
        print('Aborting!!!')
        instructionsApproved.clear()
        break

else: # else wykona się tylko gdy pętla nie zostanie przerwana przez brak
    print('Following actions will be taken: ', instructionsApproved)


print('-'*30)
instructionsApproved.clear()

i = 0
while i < len(instructions):
    print('Adding instruction to robot: ', instructions[i])
    instructionsApproved.append(instructions[i])

    if instructions[i] == 'abort':
        print('Aborting!!!')
        instructionsApproved.clear()
        break
    i += 1
else:       # dla while i for tak samo sie zachowuje else: jeśłi wystąpił break to nie ma elsa (podobna do goto, nie używaj goto!!!)
    print('Following actions will be taken: ', instructionsApproved)