'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes
'''

cadastro = []
maior = 0
menor = 999
gordo = 0
magro = 999
indice_maior = 0
indice_menor = 0
indice_gordo = 0
indice_magro = 0

while True:
    codigo = int(input('Digite seu código: '))
    if codigo == 0:
        break
    else: 
        altura = float(input('Digite sua altura: '))
        peso = float(input('Digite o seu peso: '))
        cadastro.append([codigo, altura, peso])
        op = codigo

        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura
        if peso > gordo:
            gordo = peso
        if peso < magro:
            magro = peso

    

    for i in range(len(cadastro)):
        if maior == cadastro[i][1]:
            indice_maior = i
        if menor == cadastro[i][1]:
            indice_menor = i

        if gordo == cadastro[i][2]:
            indice_gordo = i
        if magro == cadastro[i][2]:
            indice_magro = i

soma = 0
soma_peso = 0

for j in range(len(cadastro)):
    soma = soma + cadastro[j][1]

for k in range(len(cadastro)):
    soma_peso = soma_peso + cadastro[k][2]

media_altura = soma / len(cadastro)
media_peso = soma_peso / len(cadastro)

print(f'O maior aluno é {cadastro[indice_maior]} \nO menor aluno é {cadastro[indice_menor]}')
print(f'O aluno mais pesado é {cadastro[indice_gordo]} \nO mais magro é {cadastro[indice_magro]}')
print(f'A média de peso dos alunos é {media_peso:.2f}')
print(f'A média de altura dos alunos é {media_altura:.2f}')