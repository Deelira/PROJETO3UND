usuario = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
salario = float(input('Digite o seu salário: '))

perc_aumento = (idade // 10) * 5

salario = salario * (1 + (perc_aumento / 100))
#salario *= (1 + (perc_aumento / 100))

if idade > 50:
    salario = salario * 1.15

print(f'O seu salário após o ajuste é R${salario:.2f}')