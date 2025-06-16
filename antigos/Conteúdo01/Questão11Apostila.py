salario = float(input('Digite o seu salário: '))

if salario > 0 and salario <= 280:
    aumento = salario * 0.2
    perc = 20
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    perc = 15
elif salario > 700 and salario <= 1500:
    aumento = salario * 0.1
    perc = 10
elif salario > 1500:
    aumento = salario * 0.05
    perc = 5
else:
    print('Digite um salário válido!')
    aumento = 0

# Exibir o resultado para o usuário:

if aumento > 0:
    print (f'Seu salário era {salario}')
    print (f'Você recebeu um aumento percentual de {perc}%')
    print (f'Isso corresponde a um aumento em reais de {aumento:.2f}')
    print (f'Seu salário final é {salario + aumento:.2f}')