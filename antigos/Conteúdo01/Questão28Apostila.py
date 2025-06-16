'''Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não
há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda
um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
preço total, tipo de pagamento, valor do desconto e valor a pagar.

'''

tipo = input('Qual o tipo de carne você está comprando: ').lower()
kilos = float(input('Digite a quantidade de carne em kilos(kg): '))
forma_pag = input('Qual a forma de pagamento? ').lower()

if tipo == 'file duplo' or tipo == 'filé duplo' and kilos <= 5:
    valor = kilos * 4.9
elif tipo == 'file duplo' or tipo == 'filé duplo' and kilos > 5:
    valor = kilos * 5.8
elif tipo == 'alcatra' and kilos <= 5:
    valor = kilos * 5.9
elif tipo == 'alcatra' and kilos > 5:
    valor = kilos * 6.8
elif tipo == 'picanha' and kilos <= 5:
    valor = kilos * 6.9
elif tipo == 'picanha' and kilos > 5:
    valor = kilos * 7.8

if forma_pag == 'cartao tabajara' or forma_pag == 'cartão tabajara' or forma_pag == 'cartaotabajara' or forma_pag == 'cartãotabajara':
    desconto = valor * 0.05
    valor_final = valor - desconto
else:
    desconto = 0
    valor_final = valor

print(f'Você está comprando ({kilos}KG) da carne ({tipo}), o valor total é ({valor:.2f})')
print(f'Você escolheu pagar com ({forma_pag}), recebeu o desconto de (R$ {desconto:.2f}) e pagará (R$ {valor_final:.2f})')