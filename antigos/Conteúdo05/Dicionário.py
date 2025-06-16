'''
DICIONÁRIO / MAPA

PAR: CHAVE E VALOR

CHAVES SÃO ÚNICAS

NÃO TRABALHA COM ÍNDICE, NEM ORDEM

'''
# declara um dicionario vazio

pessoas = dict()

# adiciona ao dicionario 

pessoas['rene'] = 36
pessoas['calebe'] = 21

print(pessoas   )
# declarar um dicionário com valores

papas = {'francisco':88, 'joão paulo':83, 'bento16':89}

print(papas)

#percorrer um dicionario

for papa in papas:
    print(papa)

for papa in papas.values():
    print(papa)