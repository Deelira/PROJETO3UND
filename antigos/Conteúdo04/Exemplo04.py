'''
Crie uma lista, adicione 3 nomes e percorra essa lista verificando se o nome inicia com a letra m, se sim,
exiba-o.
'''

nomes = []
nomes.append('maria')
nomes.append('joao')
nomes.append('marcio')

for n in nomes:
    if n[0] == 'm':
        print(n)