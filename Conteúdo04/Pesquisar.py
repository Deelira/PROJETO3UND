'''
Pesquise sobre as funções

insert
sort
index

'''

# insert = insere um novo elemento na lista no indice que você desejar.

nomes = ['Iordan', 'Joao Pedro']

nomes.insert(2, 'Alisson')

print(nomes)

# sort

nomes.sort()

print(nomes)

nomes.sort(reverse=True)

print(nomes)

nomes.sort(key=len)

print(nomes)

# index

indice = nomes.index('Alisson')

print(f'O nome está na posição {indice} ')