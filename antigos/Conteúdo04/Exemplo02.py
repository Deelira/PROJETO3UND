'''
Crie uma lista vazia e leia o nome de todos os alunos da sala, colocando cada nome dentro da lista.
Continue lendo até que seja digitado a palavra fim.
'''

nomes = []

while True:
    nome = input('Digite seu nome: ').lower()
    #acrescentar no final da lista
    if nome == 'fim':
        break
    nomes.append(nome)

print(f'Temos o total de {len(nomes)} pessoa(s) na lista. ')