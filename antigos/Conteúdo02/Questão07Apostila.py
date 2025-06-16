'''
Escreva um programa que leia cinco números e exiba o maior entre eles.
'''

maior_lido = 0

for x in range(5):
    numero = int(input('Digite um número: '))
    if numero > maior_lido:
        maior_lido = numero

print(f'O maior número lido é {maior_lido}')