# Desenvolva um programa em python que leia o salario de um funcionario e aumente o salario em 15% caso ele receba 
# até 2 salarios minimos.
# Caso seja maior que 2 salarios, aumente 11%
# o valor do salario minimo tambem deve ser informado pelo usuario, para que ao final seja exibido o salario
#aumentado

salario_func = float(input("Digite o valor do seu salário: "))
salario_min = float(input("Digite o valor do salário mínimo atual: "))

if salario_func <= salario_min * (2):
    print(f'O salário atual é {salario_func:.2f}')
    salario_func = salario_func * 1.15
    print(f"O salário foi ajustado para {salario_func:.2f}")

if salario_func > salario_min * (2):
    print(f'O salário atual é {salario_func:.2f}')
    salario_func = salario_func * 1.11
    print(f"O salário foi ajustado para {salario_func:.2f}")
