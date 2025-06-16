'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes
'''

caracteres = []
consoantes = 0

for i in range (1, 11):
    letra = input(f'Digite a {i}ª letra: ').lower()
    
    if letra not in ['a', 'e', 'i', 'o', 'u']:
        consoantes += 1
        caracteres.append(letra)

print(f'Foram lidas {consoantes} consoantes.')