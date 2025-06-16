'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.

'''
nota = 20

while nota != 'valido':
    nota = int(input('Digite uma nota: '))
    
    if nota >= 0 and nota <= 10:
        nota = 'valido'