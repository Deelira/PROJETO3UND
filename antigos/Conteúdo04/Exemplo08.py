pessoas = ['casa', 'vida', 'casa']

print(pessoas.count('casa'))

quantidade = 0
busca = 'casa'
for item in pessoas:
    if item == busca:
        quantidade += 1