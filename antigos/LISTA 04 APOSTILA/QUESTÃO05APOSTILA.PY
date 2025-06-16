'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores.
'''

numeros = []
pares = []
impares = []

for i in range(1,21):
    num = int(input(f'Digite o {i}º número: '))
    numeros.append(num)
    resto = num % 2

    if resto == 0:
        pares.append(num)
    elif resto == 1:
        impares.append(num)

print(numeros)
print(pares)
print(impares)