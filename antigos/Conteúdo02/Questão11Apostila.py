'''
Altere o programa anterior para mostrar no final a soma dos números
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

for inteiros in range((num1 + 1 ), (num2)):
    print(inteiros)
    
print(f'A soma dos números é {(num1 + num2)}')