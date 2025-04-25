'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a 
média calculada
'''

pessoas = 0
jovem = 0
adulta = 0
idosa = 0

while True:
    idade = int(input('Digite a sua idade: '))

    if idade >= 0 and idade <= 25:
        jovem += 1
    elif idade > 25 and idade <= 60:
        adulta += 1
    elif idade > 60:
        idosa += 1
    else:
        print('Idade inválida!')
    parar = input('Deseja adicionar outra idade? (S) (N)').lower()
    if parar == 'n':
        break

if jovem > adulta and jovem > idosa:
    print('A turma é jovem')
elif adulta > jovem and adulta > idosa:
    print('A turma é adulta')
elif idosa > jovem and idosa > adulta:
    print('A turma é idosa')
else:
    print('Houve um empate.')