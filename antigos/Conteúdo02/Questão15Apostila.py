'''
 A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
nonagésimo termo.
'''
num = 1
num_ant = 1
soma = 0
n = int(input('Digite até qual termo você deseja gerar a sequência de fibonacci: '))

print(f'{num_ant}, {num}', end=', ')
for fibo in range (0, n):
    soma = num + num_ant
    num = num_ant
    num_ant = soma
    print(soma, end=', ')
