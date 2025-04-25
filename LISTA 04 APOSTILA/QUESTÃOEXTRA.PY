'''
Desenvolva duas funcionalidades:

1 - encontrar a media dos valores das mensalidades cadastradas no sistema. o usuário informa o curso e o 
sistema exibe a media dos valores pagos pelos alunos
2 - Atualizar os dados de um usuário ( exceto matrícula)
'''


alunos = []
op = 99

while op != 0:
    print('------------Menu------------')
    print('1 - Cadastrar')
    print('2 - Remover Usuário')
    print('3 - Buscar Usuário')
    print('4 - Buscar Nome')
    print('5 - Média de Valores')
    print('6 - Atualizar Cadastro')

    op = int(input('Digite a opção desejada: '))

    if op == 1:
        nome = input('Digite seu nome: ').lower()
        matricula = input('Digite sua matrícula: ')
        curso = input('Digite seu curso: ').lower()
        mensalidade = float(input('Digite o valor da sua mensalidade: '))

        alunos.append([nome, matricula, curso, mensalidade])

    elif op == 2:
        matricula_remover = input('Digite a matrícula do aluno que deseja remover: ')
        indice = -1
        for i in range(len(alunos)):
            if matricula_remover == alunos[i][1]:
                indice = 1

        if indice != -1:
            alunos.pop(indice)
            print('Aluno removido com sucesso!')
        else:
            print('Aluno não encontrado')

    elif op == 3:
        for aluno in alunos:
            print(aluno)

    elif op == 4:
        num_alunos = len(alunos)

        if num_alunos > 0:
            nome_busca = input('Digite o nome para buscar: ').lower()
            for aluno in alunos:
                if nome_busca == aluno[0]:
                    print(f'Nome: {aluno[0]}')
                    print(f'Matrícula: {aluno[1]}')
                    print(f'Curso: {aluno[2]}')
                    print(f'Mensalidade: {aluno[3]}')
                print(' - ')

        else:
            print('Não há alunos cadastrados!')

    elif op == 5:
        contagem = 0
        soma = 0
        curso = input('Qual curso você deseja buscar a média de valores ? ')
        for c in alunos:
            if c[2] == curso:
                soma += c[3]
                contagem += 1
        media = soma / contagem
        print(f'A media de mensalidade do curso {curso} é {media}')

    elif op == 6:
        mat = (input('Digite a matrículo do aluno: '))

        for m in alunos:
            if mat == m[1]:
                ope = 's'
                while ope != 'n':
                    atualizar = input('Qual dado você deseja atualizar? (N) (C) (M) ').lower()
                    if atualizar == 'n':
                        nome = input('Digite o nome: ')
                        m[0] = nome
                    elif atualizar == 'c':
                        curso = input('Digite o curso: ')
                        m[2] = curso
                    elif atualizar == 'm':
                        mensal = int(input('Digite o vaor da mensalidade: '))
                        m[3] = mensal
                    print('Dado atualizado com sucesso!')
                    ope = input('Deseja alterar outro dado? (S) (N) ').lower()
            else:
                 print('Matricula não encontrada!')