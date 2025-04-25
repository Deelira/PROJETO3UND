'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
n3 = float(input('Digite a sua terceira nota: '))

media = (n1 + n2 + n3) / 3
print (media)

if media > 0 and media < 7:
    print('Reprovado')
elif media >= 7 and media <= 9:
    print('Aprovado')
elif media == 10:
    print('Aprovado com Distinção')
