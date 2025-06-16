'''
conjunto = unicidade, exclusividade dos itens , nao se repetem

'''
pessoas = set()

#dicionário
pessoas1 = {'rene':36, 'andre':81}

alunos = {'jose', 'maria', 'pedro', 'aline', 'maria'}

alunos.add('Jose')
for aluno in alunos:
    print(aluno)

'''

split para quebra uma string por determinado caractere, exemplo

'''

rua = input('rua: ')
quebrado = rua.split(' ')
print(quebrado)