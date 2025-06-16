'''
 A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
valor seja maior que 500.
'''
num = 1
num_ant = 1
soma = 0
stop = 0

print(f'0, {num_ant}, {num}', end='')

for fibo in range (0, 91):

    if stop < 500:
        soma = num + num_ant
        num = num_ant
        num_ant = soma
        stop = soma
        print(f', {soma}', end='')