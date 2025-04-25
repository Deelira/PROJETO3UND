'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.
'''

temperaturas = []
maior = 0
menor = 100
opcao = 's'

while opcao != 'n':
    temperatura = float(input('Digite a temperatura: '))
    temperaturas.append(temperatura)
    if temperatura > maior:
        maior = temperatura
    elif temperatura < menor:
        menor = temperatura
    opcao = input('Você deseja registrar uma nova temperatura? (S) (N)').lower()
    
media = sum(temperaturas) / len(temperaturas)
print(f'A maior temperatura registrada foi {maior}')
print(f'A menor temperatura registrada foi {menor}')
print(f'A média de temperatura é de {media}')    