'''
Faça um algorítmo que receba um numéro e exiba se ele é primo ou não é:
'''

n = int(input('Digite o número desejado: '))
primo = 0

for i in range (1, n+1):
    resto = n % i

    if resto == 0:
        primo += 1

if primo == 2:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')