'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente
'''

quant_macas = float(input('Digite a quantidade de maças em kilos(kg): '))
quant_morangos = float(input('Digite a quantidade de morangos em kilos(kg): '))

if quant_morangos <= 5 and quant_morangos >= 0:
    valor_morangos = quant_morangos * 2.5
elif quant_morangos > 5:
    valor_morangos = quant_morangos * 2.2


if quant_macas <= 5 and quant_macas >= 0:
    valor_macas = quant_macas * 1.8
elif quant_macas > 5:
    valor_macas = quant_macas * 1.5


total_frutas = valor_macas + valor_morangos 

if total_frutas > 8 or total_frutas > 25:
    total_frutas = total_frutas  * 0.90
    print (f'Total a ser pago é R${total_frutas}')
else:
    print(f'Total a ser pago é R${total_frutas}')