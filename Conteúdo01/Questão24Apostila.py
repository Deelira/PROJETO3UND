'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.
'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
op = input('Qual operação você deseja realizar?').lower()

if op == 'adição' or op == 'soma' or op == 'adicao' or op == 'adiçao':
    resultado = num1 + num2
elif op == 'subtração' or op == 'subtracao':
    resultado = num1 - num2
elif op == 'divisão' or op == 'divisao':
    resultado = num1 / num2
elif op == 'multiplicação' or op == 'multiplicacao' or op == 'multiplicaçao':
    resultado = num1 * num2

resto = resultado % 2

if resto == 0:
    polaridade = 'Par'
else:
    polaridade = 'Ímpar'

if resultado >= 0:
    sinal = 'positivo'
else:
    sinal = 'negativo'

if resultado == round(resultado):
    numero = 'inteiro'
else:
    numero = 'decimal'

print(f'O resultado da operação é {resultado}, ele é um número {polaridade}, {sinal} e {numero}.')