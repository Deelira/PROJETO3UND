'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário,
conforme exemplo abaixo:
'''

num = int(input('Digite o número que deseja visualizar a tabuada: '))
inicio = int(input('Por qual número você deseja começar? '))
fim = int(input('Por qual número você deseja terminar? '))

if fim > inicio:
    for i in range(inicio, fim + 1):
        print(f'{num} x {i} = {num * i}')
else:
    print('Final menor que o início! \n Tente novamente')