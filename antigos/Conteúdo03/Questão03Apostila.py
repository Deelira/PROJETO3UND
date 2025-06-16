'''
. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''

correto = 0
incorreto = 5
nome = ' '
caractere = 0
idade = 0
num = 0
sal = -1
sexo = ' '

while correto != incorreto:

    nome = input('Digite o seu nome: ')
    for i in nome:
        caractere += 1
    if caractere > 3:
        correto += 1

        idade = int(input('Digite o sua idade: '))
        if idade >= 0 and idade <= 150:
            correto += 1

            sal = float(input('Digite o seu salário: '))
            if sal >= 0:
                correto += 1

                sexo = input('Digite o seu sexo: (F) (M): ').lower()
                if sexo == 'f' or sexo == 'm':
                    correto += 1

                    civil = input('Digite qual o seu estado civil: (S) (C) (V) (D) ').lower()
                    if civil == 's' or civil == 'c' or civil == 'v' or civil == 'd':
                        correto += 1

                    else:
                        print('Estado Civil Inválido!')

                else:
                    print('Sexo Inválido!')

            else:
                print('Salário Inválido!')
        else:
            print('Idade Inválida!')
    else:
        print('Número de caracteres inválidos!')
        caractere = 0