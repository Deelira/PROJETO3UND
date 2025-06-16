'''
 Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número
negativo
'''
num = 1
ate_25 = 0
ate_50 = 0
ate_75 = 0
ate_100 = 0

while num > 0:
    num = int(input('Digite um número: '))
    if num > 0 and num <= 25:
        ate_25 += 1
    if num > 25 and num <= 50:
        ate_50 += 1
    if num > 50 and num <= 75:
        ate_75 += 1
    if num > 75 and num <= 100:
        ate_100 += 1

print(f'[0-25] = {ate_25}', end=', ')
print(f'[25-50] = {ate_50}', end=', ')
print(f'[50-75] = {ate_75}', end=', ')
print(f'[75-100] = {ate_100}', end=', ')