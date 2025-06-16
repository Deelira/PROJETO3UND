'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
informar de qual numero ele deseja ver a tabuada. 
'''

num = int(input('Digite o número o qual você deseja saber a tabuada: '))
multi = 0

print(f'Tabuada de {num}: ')

for x in range(1, 11):
    multi = x
    resultado = num * x
    print(f'{num} X {x} = {resultado}')
