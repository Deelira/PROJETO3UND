'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
divisível.
'''

primo = 0
primos = []
while True:
    num = int(input('Digite o número desejado: '))

    for i in range (1, num + 1):
        resto = num % i

        if resto == 0:
            primo += 1
            primos.append(i)
    if primo == 2:
        print(f'O número {num} é primo.')
    else:
        print(f'O número {num} não é primo. ')
        print(f'Aqui está uma lista com os números divisíveis por {num} de 1 até ele mesmo: ')
        print(primos)
    continuar = input('Deseja realizar o teste novamete? (S) (N) ').lower()
    if continuar == 'n':
        break
    elif continuar == 's':
        primo = 0
        primos.clear()
    else:
        print('Resposta Inválida!')