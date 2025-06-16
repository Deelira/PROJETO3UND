'''
Você deverá criar um programa que receba como entrada um número inteiro positivo (em decimal) e o converta para sua representação em binário.

O sistema binário representa números utilizando apenas os dígitos 0 e 1. Para converter de decimal para binário, usamos divisões sucessivas por 2, registrando os restos de cada divisão.

'''

decimal = int(input('Digite um número: '))
binario = ''

while decimal > 0:
    resto = decimal % 2
    resto = str(resto)
    binario = (resto + binario)
    decimal = decimal // 2

print(f'Número decimal: {decimal}')
print(binario)