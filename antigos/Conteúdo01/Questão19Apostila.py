#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
#do mesmo.

result = int(input('Digite um número: '))

if result > 0 and result < 1000:
    centenas = result // 100
    
    dezenas = result // 10
    resto = dezenas % 10
    
    unidades = result % dezenas
    
    print(f'{result} = {centenas} centenas, {resto} dezenas e {unidades} unidades')
else:
    print("Número inválido!")
