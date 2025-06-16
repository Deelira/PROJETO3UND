'''
 Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto
e o número do aluno mais baixo, junto com suas alturas
'''

alunos = []
maior = 0
menor = 999
aluno_alto = 0
aluno_baixo = 999


for i in range(10):
    num = int(input('Digite o número: '))
    altura = float(input('Digite a altura: '))
    alunos.append([num, altura])

    if altura > maior:
        maior = altura
        aluno_alto = num
    if altura < menor:
        menor = altura
        aluno_baixo = num

print(f'O aluno mais alto é o {aluno_alto} Altura: {maior}')
print(f'O aluno mais baixo é o {aluno_baixo} Altura: {menor}')
