'''
O nepa está precisando de um sistema que entreviste 50 alunos fazendo perguntas objetivas sim ou não.
Modele o sistema para listar apenas os alunos que possuam mais aderencia ao projeto.
'''

sim = 0

for i in range (50):
    nome = input('Digite o seu nome: ')
    questao1 = input('Você conhece as linguagens Java e Python? (Sim ou Não) ').lower()
    questao2 = input('Você tem disponibilidade de horário aos sábados e feriados? (Sim ou Não) ').lower()
    questao3 = input('Você tem experiência como desenvolvedor? (Sim ou Não) ').lower()
    questao4 = input('Você está formado ou graduando na área da computação? (Sim ou Não) ').lower()

    if questao1 == 'sim':
        sim += 1
    if questao2 == 'sim':
        sim += 1
    if questao3 == 'sim':
        sim += 1
    if questao4 == 'sim':
        sim += 1
    
    if sim >= 2:
        print(f'{nome}, você está apto a participar do projeto.')
    else:
        print(f'{nome}, você não está apto a participar do projeto.')