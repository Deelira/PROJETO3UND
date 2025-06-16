'''
. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo
'''

valor_hora = float(input('Digite o valor da sua hora: '))
quant_horas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario = valor_hora * quant_horas

if salario <= 900 and salario > 0:
    perc_desconto = 0
elif salario > 900 and salario <= 1500:
    perc_desconto = 0.05
elif salario > 1500 and salario >= 2500:
    perc_desconto = 0.1
elif salario > 2500:
    perc_desconto = 0.2

inss = 3
inss_final = salario * 0.03
fgts = 11
fgts_final = salario * 0.11
desconto = salario * perc_desconto

desconto_total = desconto + inss_final + fgts_final
salario_liquido = salario - desconto_total

print(f'Salário Bruto: ( {valor_hora:.0f} * {quant_horas:.0f}                    : R$ ({salario:.2f})) ')
print(f'(-) IR ({perc_desconto}%)                              : R$ ({desconto:.2f}) ')
print(f'(-) INSS ({inss}%)                               : R$ ({inss_final:.2f})')
print(f'FGTS ({fgts}%)                                  : R$ ({fgts_final:.2f})')
print(f'Total de descontos                          : R$ ({desconto_total:.2f})')
print(f'Salário Líquido                             : R$ ({salario_liquido:.2f})')