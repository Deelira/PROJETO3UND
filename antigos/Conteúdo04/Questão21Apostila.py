'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele
que é divisível somente por ele mesmo e por 1.
'''
primo = 0

while True:
    num = int(input('Digite o número desejado: '))

    for i in range (1, num + 1):
        resto = num % i

        if resto == 0:
            primo += 1

    if primo == 2:
        print(f'O número {num} é primo.')
    else:
        print(f'O número {num} não é primo. ')
    continuar = input('Deseja realizar o teste novamete? (S) (N) ').lower()
    if continuar == 'n':
        break
    elif continuar == 's':
        primo = 0
    else:
        print('Resposta Inválida!')