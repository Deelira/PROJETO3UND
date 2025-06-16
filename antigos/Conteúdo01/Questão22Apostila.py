''' Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da
divisão).
'''

num = int(input('Digite um número: '))

div = num % 2

if div == 0:
    print(f'O número {num} é um número par.')
else:
    print(f'O número {num} é um número ímpar    .')