'''. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120
'''

num = int(input('Digite o número o qual você deseja calcular o fatorial: '))
stop = num

for i in range (1, (stop+1)):
    fatorial = stop * i
    print(fatorial, end=' ')