'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

maior = 0
menor = 1000
soma = 0

num = int(input('Digite a quantidade de números que você deseja: '))

if num > 0 and num < 1000:
    for i in range (1, (num+1)):
    
        if i > maior:
            maior = i
        
        if i < menor:
            menor = i

        soma = soma + i
    print(f'O número maior entre eles é {maior}, o menor é {menor}. A soma entre eles é {soma}')
else:
    print('Número inválido.')
