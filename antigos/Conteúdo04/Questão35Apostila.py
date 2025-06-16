'''
 Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre
1 e um número inteiro informado pelo usuário.
'''

contagem = 0
primos = []

num = int(input('Digite um número: '))

for j in range(1, num+1):
    for i in range(1, num+1):
        resto = num % i
        if resto == 0:
            contagem += 1
    if contagem == 2:
        primos.append(num)
    num -= 1
    contagem = 0

primos.sort()
print(primos)