'''
Faça um programa que leia 5 números e informe a soma e a média dos números
'''
num1 = 0

for x in range(5):
    num2 = int(input('Digite um número: '))
    num1 = num1 + num2

media = num1 / 5

print(f'A soma dos números é {num1}')
print(f'A média entre os números é: {media:.0f}')