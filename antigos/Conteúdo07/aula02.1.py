atletas = []

def inserir_arquivo(nome):
    file = open('meusatletas.txt', 'a')
    file.write(nome + '\n')
    file.close()

def inserir_atleta():
        nome = input('Digite seu nome: ')
        atletas.append(nome)
        inserir_arquivo(nome)

op = 9
inserir_arquivo('Esses são meus atletas:')

while op != 0:
    print('----------------------MENU---------------------- \n')
    print('1- INSERIR ATLETA')
    print('2- REMOVER ATLETA')
    print('3- SALVAR ARQUIVO EM LISTA \n')

    op = int(input('Digite a opção desejada: '))

    if op == 1:
        inserir_atleta()

    elif op == 2:
        nome = input('Digite o nome para remover: ')
        if nome in atletas:
            atletas.remove(nome)
    elif op == 3:
        file = open('meusatletas.txt','w')
        for nome in atletas:
            file.write(nome + '\n')
        file.close()

