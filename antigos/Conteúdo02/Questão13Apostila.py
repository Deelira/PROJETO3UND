'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
número. Não utilize a função de potência da linguagem.
'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
resultado = num1

for x in range(1, num2):
    calc = num1 * resultado
    num1 = calc
    
print(f'O resultado é ({calc})')