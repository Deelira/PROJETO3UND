'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o 
fatorial a números inteiros positivos e menores que 16.
'''
fatoriais = []
continuar = ''
while True:
    num = int(input('Digite o número o qual você deseja calcular o fatorial: '))
    stop = num

    if num > 0 and num < 16:
        for i in range (1, (stop+1)):
            fatorial = stop * i
            fatoriais.append(fatorial)
        print(fatoriais)

        continuar = input('Você deseja calcular o fatorial de um novo número? (S) ou (N) ').lower()
        
        if continuar == 'n':
            break
        elif continuar == 's':
            fatoriais.clear()
    else:
        print('Digite um número válido! ')