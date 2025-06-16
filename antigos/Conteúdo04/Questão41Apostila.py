'''
. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor
dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
'''

divida = float(input('Digite o valor da dívida: R$ '))
juros = 10


print('Valor da dívida | Valor dos juros | Quantidade de parcelas | Valor da parcela')
print(f'R$ {divida:.2f}          0            1          R$ {divida}')

for i in range (3,13, 3):
    acrescimo = juros/100 + 1
    total = divida * acrescimo
    print(f'R$ {total:.2f}          {juros}          {i}          R$ {total/i:.2f}')
    juros += 5