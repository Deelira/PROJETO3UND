'''
 Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa
deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o
funcionamento, o estilo e o número de testes (divisões) executados.
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
        print(primos)
        print(f'Foram executadas {i} divisões')
    else:
        print(f'O número {num} não é primo. ')
    continuar = input('Deseja realizar o teste novamete? (S) (N) ').lower()
    if continuar == 'n':
        break
    elif continuar == 's':
        primo = 0
        primos.clear()
    else:
        print('Resposta Inválida!')