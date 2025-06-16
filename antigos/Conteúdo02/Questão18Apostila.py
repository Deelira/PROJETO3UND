'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''
maior = 0
menor = 1000
soma = 0
num = int(input('Digite a quantidade de números que você deseja: '))

for i in range (1, (num+1)):
   
    if i > maior:
        maior = i
    
    if i < menor:
        menor = i

    soma = soma + i

print(f'O número maior entre eles é {maior}, o menor é {menor}. A soma entre eles é {soma}')