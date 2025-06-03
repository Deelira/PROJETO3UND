'''
PACOTE UTILIZADO PARA FUNÇÕES DE USUÁRIO

VALIDAR SENHA, VALIDAR E-MAIL...
'''

def menu(menu):
        print('\n \n======================== M E N U ========================\n')
        print('\n1 - CADASTRAR USUÁRIO', end='         ')
        print('2 - LOGIN', end='         ')
        print('0 - SAIR')
        print('\nSeja bem vindo ao Vamo ou Bora, o seu aplicativo de caronas!', end= ' ')
        menu = input('O que você deseja? ').lower()
        while menu.isalpha():
                menu = input('O que você deseja? ').lower()
        while int(menu) < 0 or int(menu) > 2:
                menu = input('O que você deseja? ').lower()
        return True


def validar_nome(nome):
        nome = nome.strip()
        partes = nome.split()
        if len(partes) < 2:
                return False
        for parte in partes:
                if not parte.isalpha():
                        return False
        return True


def validar_data(data):
        dia = int(data.split('/')[0])
        mes = int(data.split('/')[1])
        ano = int(data.split('/')[2])
        if dia <= 0 or dia > 31:
                return False
        if mes <= 0 or mes > 12:
                return False
        if ano < 1900 or ano > 2025:
                return False
        return True


def verificar_cpf(cpf:str):
        cpf = cpf.replace('.','')
        cpf = cpf.replace('-','')
        if len(cpf) == 11:
                return True
        else:
                return False


def validar_email(email_cadastro):
        if '@' not in email_cadastro or len(email_cadastro) < 7 or ('gmail' not in email_cadastro and 'hotmail' not in email_cadastro and 'icloud' not in email_cadastro and 'outlook' not in email_cadastro and 'yahoo' not in email_cadastro and 'mail' not in email_cadastro and 'protonmail' not in email_cadastro):
                return False
        else:
                return True


def validar_senha(senha, confirmacao_de_senha):
        if senha != confirmacao_de_senha or len(senha) < 6:
                return False
        else:
                return True


def cadastrar_usuario(usuarios):
        nome = input('\nQual o seu nome? ').lower()
        while not validar_nome(nome):
                nome = input('Qual o seu nome? ').lower()
        email_cadastro = input('Qual o seu email? ').lower()
        while not validar_email(email_cadastro):
                email_cadastro = input('Qual o seu email? ').lower()
        senha = input('Você deve escolher uma senha com pelo menos 06 caracteres: ').lower()
        confirmacao_de_senha = input('Digite a senha novamente: ')
        while not validar_senha(senha,confirmacao_de_senha):
                senha = input('Você deve escolher uma senha com pelo menos 06 caracteres: ').lower()
                confirmacao_de_senha = input('Digite a senha novamente: ')

        arquivo_usuarios = open('E:\\Algorítimo e Lógica de programação\\Phyton\\USUÁRIOS\\usuarios.txt', 'a')
        usuarios[email_cadastro] = {
                'nome': nome,
                'senha': senha,
                }
        arquivo_usuarios.write(usuarios)
        print('\nTudo certo, cadastro efetuado com sucesso!\n')


def login(login,senha):
        logado = False
        login = input('Vamos lá, digite o email cadastrado: ').lower()
        if login == 'voltar':
                menu = 'start'
        senha = input('Qual a senha? ').lower()
        if login in usuarios and senha == usuarios[login]['senha']:
                logado = True
        else:    
                print('Desculpe, email ou senha inválidos.\n \nTente novamente ou digite "voltar" para voltar ao menu inicial.')