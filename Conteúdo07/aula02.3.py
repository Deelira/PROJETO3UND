
arquivo = open('meusatletas.txt', 'r')
nomes = arquivo.readlines()
arquivo.close()

ind = nomes.index('odivio\n')
nomes[ind] = 'victor\n'

arquivo = open('meusatletas.txt' , 'w')
arquivo.writelines(nomes)

'''
ou

for nome in nomes:
    arquivo.write(nome)
    
'''
arquivo.close()