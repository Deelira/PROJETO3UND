'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
números impares
'''

soma = 0
par = 0
impar = 0

for x in range(1, 11):
    num = int(input('Digite um numéro: '))
    soma = num + soma
    resto = num % 2
    if resto == 0:
        par = par + 1
    else:
        impar = impar + 1

print(f'A soma dos números é {soma}')
print(f'Entre eles, existem {par} número(s) par(es) e {impar} número(s) ímpar(es)')

