'''
Você deverá desenvolver um programa que recebe como entrada um número binário (composto apenas por 0s e 1s) e converte 
esse valor para sua forma decimal (base 10). O binário é um sistema numérico de base 2. 
Cada dígito do número binário representa uma potência de 2, começando da direita para a esquerda 
(do menos significativo para o mais significativo).

'''

num_binario = input('Digite um num: ')
num_binario_reverso = num_binario[::-1]
num_decimal = 0
aux_potencia = 0

for n in num_binario_reverso:
    n = int(n)
    multi = 2 ** aux_potencia
    multi *= n
    num_decimal += multi
    aux_potencia += 1

print(f'Bin: {num_binario}')
print(num_decimal)
