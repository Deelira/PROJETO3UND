'''
FAÇA UM PROGRAMA QUE LEIA UM VETOOR DE 5 NÚMEROS INTEIROS E MOSTRE-OS
'''

NUMBERS = []

for i in range (6):
    num = int(input(f'Digite o {i}º número: '))
    NUMBERS.append(num)
    
print(NUMBERS)