'''
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele
é ou não um número primo.
'''

num = int(input('Digite um número: '))
contagem = 0

for i in range(1, num+1):
    resto = num % i
    if resto == 0:
        contagem += 1
if contagem == 2:
    print('É um número primo')
else:
    print('Não é um número primo')