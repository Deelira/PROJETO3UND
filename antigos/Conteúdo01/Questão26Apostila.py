'''
 Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a. Álcool:
b. até 20 litros, desconto de 3% por litro
c. acima de 20 litros, desconto de 5% por litro
d. Gasolina:
e. até 20 litros, desconto de 4% por litro
f. acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

litros = float(input('Digite a quantidade de litros: '))
tipo = input('Você abasteceu Álcool ou Gasolina? (A/G)').lower()

if tipo == 'a' and litros <= 20:
    valor = (litros * 1.9) * 0.97
    
elif tipo == 'a' and litros > 20:
    valor = (litros * 1.9) * 0.95
    
elif tipo == 'g' and litros <= 20:
    valor = (litros * 2.5) * 0.96
    
elif tipo == 'g' and litros > 20:
    valor = (litros * 2.5) * 0.94
    
print (f'O valor a ser pago é {valor}')