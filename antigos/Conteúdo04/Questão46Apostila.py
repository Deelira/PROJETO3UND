'''
. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois 
informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular 
a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não 
são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser 
conforme o exemplo abaixo:
'''

atletas = []

while True:
    nome = input('Digite o seu nome: ')
    if nome.strip() == '':
        print('Programa encerrado')
        break
    saltos = []
    total = 0
    for i in range(1,6):
        salto = float(input(f'Distancia do {i}º salto: '))
        saltos.append(salto)
        total += int(salto)
    media_saltos = (total/(i))
    atletas.append([nome, saltos, media_saltos])
    
for atleta in atletas:
    
    saltos_atleta = atleta[1]
    media_saltos_atleta = atleta[2]
    
    print(f'Atleta: {atleta[0]}\n')
    print(f'Primeiro Salto: {atleta[1][0]}m')
    print(f'Segundo Salto: {atleta[1][1]}m')
    print(f'Terceiro Salto: {atleta[1][2]}m')
    print(f'Quarto Salto: {atleta[1][3]}m')
    print(f'Quinto Salto: {atleta[1][4]}m\n')
    maior_salto = max(saltos_atleta)
    pior_salto = min(saltos_atleta)
    print(f'Melhor Salto: {maior_salto}')
    print(f'Pior Salto: {pior_salto}')
    print(f'Média dos demais saltos: {media_saltos}\n')
    saltos_restantes = saltos_atleta.copy()
    saltos_restantes.remove(maior_salto)
    saltos_restantes.remove(pior_salto)
    media = sum(saltos_restantes) / len(saltos_restantes)
    print('Resultado final: ')
    print(f'{atleta[0]}: {media}m')