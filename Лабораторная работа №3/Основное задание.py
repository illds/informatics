import re
import random
eyes = ':;X8='
noses = ['-', '<', '-{', '<{']
mouths = '()O|\/P'

tests = []
for i in range(5):
    test = ''
    for j in range(random.randint(5, 10)):
        if random.randint(0,3) == 0:
            test += '8<{) '
        else:
            test += eyes[random.randint(0,4)]+noses[random.randint(0,3)]+mouths[random.randint(0,6)]+' '
    tests.append(test)

for testnumber in range(len(tests)):
    test = tests[testnumber]
    print(f"Тест №{testnumber+1}:\n{test}\nОтвет:")

    my_smiles = re.findall(r'8<\{\)', test)
    print(len(my_smiles))

    print('\nРучной подсчёт:')
    k = 0
    for i in range(len(test)-5, -1, -1):
        if test[i:i+4] == '8<{)':
            test = test[:i] + 'Here' + test[i:]
            k += 1
    print(k)
    print(test)
    print('~'*30)
