'''
 Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
 mostrando uma mensagem de erro e voltando a pedir as informações.
'''
login = 1
senha = 1

while senha == login:
    login = input('Digite o seu login: ')
    senha = input('Digite o sua senha: ')
    
    if login == senha:
        print('------- Erro! Usuário e senham devem ser diferentes. Tente novamente -------')