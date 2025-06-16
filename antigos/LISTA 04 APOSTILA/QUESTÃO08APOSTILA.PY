'''
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima
a idade e a altura na ordem inversa a ordem lida
'''

pessoa = []

for i in range(5):
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))

    pessoa.append([idade, altura])

pessoa.sort(reverse=True)

for i in pessoa:
    print(pessoa[i])