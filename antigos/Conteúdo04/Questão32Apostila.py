'''
 Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve
ser conforme o exemplo abaixo:
'''

fatorial = []
total = 1

num = int(input('Digite um número: '))
print(f'Fatorial de: {num}')
print(num, '! =', num, end='.') 

for i in range(num-1, 0, -1):
    total = i * num
    num = total
    print(i, end='.')

print('=', total)