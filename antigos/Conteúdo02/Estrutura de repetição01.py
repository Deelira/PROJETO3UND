# Estrutura de repetição : for

quant = int(input('Quantos números você deseja somar? '))
soma = 0

for x in range (quant):
    numero = int(input('Digite um numero: '))
    soma = soma + numero

print(f'O resultado é {soma}')