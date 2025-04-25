'''
 Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''

num = []
soma = 0
multiplicacao = 1

for i in range(1,6):
    numero = int(input(f'Digito o {i}º número: '))
    num.append(numero)
    soma += numero
    multiplicacao *= numero

print(f'A soma é {soma}, a multiplicação {multiplicacao} e a lista dos números é {num}')