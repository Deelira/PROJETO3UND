'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
seguintes dados:
a. Código da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio
'''

dados = [[1020, 1000, 10], [1030, 2000, 20], [1040, 5000, 50], [1050, 6000, 60], [1060, 1000, 20]]
maior_indice = 0
menor_indice = 5000000
city_maior_indice = 0
city_menor_indice = 5000000
soma = 0
acidentes = 0

for cidade in dados:

    if cidade[2] > maior_indice:
        maior_indice = cidade[2]
        city_maior_indice = cidade[0]
    if cidade[2] < menor_indice:
        menor_indice = cidade[2]
        city_menor_indice = cidade[0]
    soma = cidade[1] + soma

for a in dados:
    contagem = 0
    if a[1] < 2000:
        acidentes += a[2]
        contagem += 1

print(f'O maior indice de acidentes é {maior_indice} e pertende a cidade {city_maior_indice}')
print(f'O menor indice de acidentes é {menor_indice} e pertende a cidade {city_menor_indice}')
print(f'Total de veículos = {soma}')
print(f'A média de acidentes nas cidades com menos de 2000 veículos é de {acidentes/contagem}')