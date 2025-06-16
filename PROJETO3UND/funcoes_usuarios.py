'''
PACOTE UTILIZADO PARA FUNÇÕES DE USUÁRIO

VALIDAR SENHA, VALIDAR E-MAIL...
'''
import os 

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


def cadastrar_usuario(usuarios, arquivo_usuarios):

        nome = input('\nQual o seu nome? ').lower()
        if nome == 'voltar':
                menu = 'start'
                return 
        while not validar_nome(nome):
                nome = input('Qual o seu nome? ').lower()
        email_cadastro = input('Qual o seu email? ').lower()
        if email_cadastro == 'voltar':
                menu = 'start'
                return 
        while not validar_email(email_cadastro):
                email_cadastro = input('Qual o seu email? ').lower()
        senha = input('Você deve escolher uma senha com pelo menos 06 caracteres: ').lower()
        if senha == 'voltar':
                menu = 'start'
                return 
        confirmacao_de_senha = input('Digite a senha novamente: ')
        while not validar_senha(senha,confirmacao_de_senha):
                senha = input('Você deve escolher uma senha com pelo menos 06 caracteres: ').lower()
                confirmacao_de_senha = input('Digite a senha novamente: ')

        usuarios[email_cadastro] = {
                'nome': nome,
                'senha': senha,
                }
        with open(arquivo_usuarios, 'a') as f:
                linha = (f'{email_cadastro},{nome},{senha}\n')
                f.write(linha)

        print('\nTudo certo, cadastro efetuado com sucesso!\n')


def login(usuarios,menu):
        login = input('Vamos lá, digite o email cadastrado: ').lower()
        if login == 'voltar':
                menu = 'start'
                return 
        
        senha = input('Qual a senha? ').lower()
        if senha == 'voltar':
                menu = 'start'
                return 
        
        if login in usuarios and senha == usuarios[login]['senha']:
                print('Login realizado com sucesso!')
                return login
        else:    
                print('\nDesculpe, email ou senha inválidos.')


def cadastrar_carona(caronas,usuarios,login):
        print('\nDigite "voltar" para ser redirecionado ao menu')

        origem = input('\nQual a origem da sua carona? ').lower()
        if origem == 'voltar':
                menu = 'start'
                return 
        
        destino = input('Qual o destino? ').lower()
        if destino == 'voltar':
                menu = 'start'
                return 
        
        data_carona = input('Qual a data da carona? dd/mm/aaaa: ').lower()
        if data_carona == 'voltar':
                return
        
        if len(data_carona) < 9 or data_carona[2] != '/' and data_carona[5] != '/':
                print('\nFormato de data inválida!')
                return
        
        horario = input('Que horas você vai? (hh:mm) ').lower()
        if horario == 'voltar':
                return

        if len(horario) != 5 or  horario[2] != ':':
                print('Horário iválido!')
                return
        
        vagas = (input('Quantas vagas disponíveis em seu veículo? ')).lower()
        if vagas == 'voltar':
                return
        if not vagas.isdigit():
                print('\nErro: Digite apenas números válidos para vagas.')
                return
        
        valor_carona = (input('Qual o valor de cada vaga? ')).lower()
        if valor_carona == 'voltar':
                return
        valor_carona.replace(',','.')
        if not valor_carona.replace('.','',1).isdigit():
                print('\nErro: Digite apenas números válidos para valor.')
                return
        vagas = int(vagas)
        valor_carona = float(valor_carona)

        nova_carona = {
                        'Motorista' : usuarios[login]['nome'],
                        'Origem' : origem,
                        'Destino' : destino,
                        'Data' : data_carona,
                        'Horário' : horario,
                        'Vagas' : vagas,
                        'Valor' : valor_carona,
                        'Reservas' : dict()
                }
        if login not in caronas:
                caronas[login] = dict()
        id_carona = (f'carona{len(caronas[login]) + 1}')
        caronas[login][id_carona] = nova_carona
        print('\nNova carona cadastrada com sucesso!\n')
        return nova_carona

def listar_caronas(caronas):
        caronas_disponiveis = dict()
        for motorista in caronas:
                for id in caronas[motorista]:
                        if caronas[motorista][id]['Vagas'] > 0:
                                caronas_disponiveis = caronas[motorista]
                        if (len(caronas_disponiveis)) > 0:
                                for carona in caronas_disponiveis:
                                        print('\n')
                                        print(f'Motorista : {caronas_disponiveis[carona]['Motorista']}')
                                        print(f'Origem : {caronas_disponiveis[carona]['Origem']}')
                                        print(f'Destino : {caronas_disponiveis[carona]['Destino']}')
                                        print(f'Data : {caronas_disponiveis[carona]['Data']}')
                                        print(f'Hora : {caronas_disponiveis[carona]['Horário']}')
                                        print(f'Vagas : {caronas_disponiveis[carona]['Vagas']}')
                                        print(f'Valor R$: {caronas_disponiveis[carona]['Valor']}')
                                        print(f'Reservas: {caronas_disponiveis[carona]['Reservas']}')
                                        print(f'Para reservar vaga, anote o email do motorista: {motorista}')
                                        print('\n')
                        else:
                                print('\nInfelizmente não temos carona disponível no momento')

def bucar_por_origem(caronas):
        encontrada = False
        origem_buscar = input('\nDigite a origem da sua carona: ').lower()
        destino_buscar = input('Agora digite o destino: ').lower()
        for motorista in caronas:
                for id in caronas[motorista]:
                        if caronas[motorista][id]['Origem'] == origem_buscar and caronas[motorista][id]['Destino'] == destino_buscar and caronas[motorista][id]['Vagas'] > 0:
                                encontrada = True
                                print('\n')
                                print(f'Carona encontrada, o motorista é {caronas[motorista][id]['Motorista']}')
                                print(f'Origem : {caronas[motorista][id]['Origem']}')
                                print(f'Destino : {caronas[motorista][id]['Destino']}')
                                print(f'Data : {caronas[motorista][id]['Data']}')
                                print(f'Hora : {caronas[motorista][id]['Horário']}')
                                print(f'Vagas : {caronas[motorista][id]['Vagas']}')
                                print(f'Valor R$: {caronas[motorista][id]['Valor']}')
                                print(f'Reservas: {caronas[motorista][id]['Reservas']}')
                                print(f'Para reservar vaga, anote o email do motorista: {motorista}')
                                print('\n')
        if not encontrada:
                print('\nInfelizmente não encontramos nenhuma carona compatível.')

def reservar_vaga(caronas,login,historico_passageiros,usuarios):
        print('\nDigite "voltar" para ser redirecionado ao menu\n')
        email_motorista = input('Digite o email do motorista o qual você deseja pegar carona: ').lower()
        if email_motorista == 'voltar':
                return
        data_carona_reservar = input('Digite a data da carona (dd/mm/aaaa):  ').lower()
        if data_carona_reservar == 'voltar':
                return
        if len(data_carona_reservar) < 9 or data_carona_reservar[2] != '/' and data_carona_reservar[5] != '/':
                        print('\nFormato de data inválida!')
        elif email_motorista in caronas:
                        for id in caronas[email_motorista]:
                                if data_carona_reservar == caronas[email_motorista][id]['Data']:
                                        if caronas[email_motorista][id]['Vagas'] > 0:
                                                reserva_id = (f'reserva{len(caronas[email_motorista][id]["Reservas"]) + 1}')
                                                caronas[email_motorista][id]['Reservas'][reserva_id] = usuarios[login]['nome']
                                                quantidade_de_vagas = caronas[email_motorista][id]['Vagas'] - 1
                                                caronas[email_motorista][id]['Vagas'] = quantidade_de_vagas
                                                if login not in historico_passageiros:
                                                        historico_passageiros[login] = dict()
                                                num_reserva_passageiro = len(historico_passageiros[login]) + 1
                                                historico_passageiros[login][num_reserva_passageiro] = [caronas[email_motorista][id]['Data'], caronas[email_motorista][id]['Motorista'], caronas[email_motorista][id]['Valor']]
                                                print('\nReserva efetuada com sucesso!')
                                                return
                                        else:
                                                print('\nQue pena, não há mais vagas!')
                                                return
        else:
                print('\nNenhuma carona oferecida por esse motorista!')
                return
        
def cancelar_reserva(caronas,login,usuarios):
        reserva_encontrada = False
        print('\nDigite "voltar" a qualquer momento para retornar ao menu')
        email_cancelar = input('Digite o email do motorista o qual você deseja cancelar carona: ').lower()
        if email_cancelar == 'voltar':
                return
        data_carona_cancelar = input('Digite a data da carona: (dd/mm/aaaa) ').lower()
        if data_carona_cancelar == 'voltar':
                return
        if len(data_carona_cancelar) < 9 or data_carona_cancelar[2] != '/' and data_carona_cancelar[5] != '/':
                print('\nFormato de data inválida!')
        else:
                if email_cancelar in caronas:
                        for id in caronas[email_cancelar]:
                                if data_carona_cancelar == caronas[email_cancelar][id]['Data']:
                                        for reserva in caronas[email_cancelar][id]['Reservas']:
                                                if caronas[email_cancelar][id]['Reservas'][reserva] == usuarios[login]['nome']:
                                                        reserva_encontrada = True
                                                        reserva_a_deletar = reserva
                        if reserva_encontrada:
                                caronas[email_cancelar][id]['Reservas'].pop(reserva_a_deletar)
                                caronas[email_cancelar][id]['Vagas'] += 1
                                print('\nReserva cancelada com sucesso!')
                        else:
                                print('\nVocê não tem reserva nessa carona!\n')
                                sub_menu = 'start'
                else:
                        print('Nenhuma carona oferecida por esse motorista!')
                        sub_menu = 'start'

def remover_carona(caronas,login,):
        carona_a_remover = False
        if login not in caronas or len(caronas[login]) < 1:
                print('\nVocê não tem nenhuma carona cadastrada!')
                return
        else:
                data_carona_remover = input('Digite a data da carona que deseja remover: (dd/mm/aaaa) ').lower()
                if len(data_carona_remover) < 9 or data_carona_remover[2] != '/' and data_carona_remover[5] != '/':
                        print('\nFormato de data inválida!')
                else:
                        lista_caronas = caronas[login]
                        for id in lista_caronas:
                                if caronas[login][id]['Data'] == data_carona_remover:
                                        carona_a_remover = True
                                if carona_a_remover:
                                        caronas[login].pop(id)
                                        print('\nCarona excluída com sucesso!')
                                        return
                                else:
                                        print('\nVocê não tem nenhuma carona cadastrada nesta data!')
                                        return
                                
def detalhar_carona(caronas,login):
        detalhar_encontrada = False
        email_a_detalhar = input('Digite o email do motorista o qual você deseja exibir a carona: ').lower()
        data_detalhar = input('Digite a data da carona: (dd/mm/aaaa) ').lower()
        if len(data_detalhar) < 9 or data_detalhar[2] != '/' and data_detalhar[5] != '/':
                print('\nFormato de data inválida!')
        else:
                if email_a_detalhar in caronas:
                        lista_caronas_motorista = caronas[email_a_detalhar]
                        for id in lista_caronas_motorista:
                                if caronas[email_a_detalhar][id]['Data'] == data_detalhar:
                                        detalhar_encontrada = True
                        if detalhar_encontrada:
                                print('\nCarona encontrada:\n')
                                print(f'Origem : {caronas[email_a_detalhar][id]['Origem']}')
                                print(f'Destino : {caronas[email_a_detalhar][id]['Destino']}')
                                print(f'Data : {caronas[email_a_detalhar][id]['Data']}')
                                print(f'Hora : {caronas[email_a_detalhar][id]['Horário']}')
                                print(f'Vagas : {caronas[email_a_detalhar][id]['Vagas']}')
                                print(f'Valor R$: {caronas[email_a_detalhar][id]['Valor']}')
                                print(f'Reservas: {caronas[email_a_detalhar][id]['Reservas']}\n')
                        else:
                                print('\nDesculpe, carona não encontrada!')

def caronas_cadastradas(caronas,login):
        if login in caronas:
                if len(caronas[login]) < 1:
                        print('\nVocê não tem nenhuma carona cadastrada!')
                else:
                        for id in caronas[login]:
                                print(f'\n{id}\n')
                                print(f'Origem : {caronas[login][id]['Origem']}')
                                print(f'Destino : {caronas[login][id]['Destino']}')
                                print(f'Data : {caronas[login][id]['Data']}')
                                print(f'Hora : {caronas[login][id]['Horário']}')
                                print(f'Vagas : {caronas[login][id]['Vagas']}')
                                print(f'Valor R$: {caronas[login][id]['Valor']}')
                                print(f'Reservas: {caronas[login][id]['Reservas']}\n')

def sac(sugestoes):
        print('\n========== SAC - Serviço de Atendimento ao Cliente ==========\n')
        print('1 - REPORTAR PROBLEMA COM A RESERVA')
        print('2 - REPORTAR PROBLEMA COM CARONA')
        print('3 - FAZER SUGESTÃO')
        print('4 - OUTROS')
        print('5 - VISUALIZAR SUAS SUGESTÕES\n')
        print('0 - VOLTAR\n')
        op = input('Digite a opção desejada: ').lower()
        if op == '1' or op == '2' or op == '3' or op == '4':
                if login not in sugestoes:
                        sugestoes[login] = []
                        opiniao = input('\nDescreva seu problema ou sugestão: ')
                        print('\nObrigado, sua opinião foi recebida e sera analisada pela nossa equipe.\n')
                        sugestoes[login].append({opiniao})
                elif op == '5':
                        if login in sugestoes:
                                print(sugestoes[login])
                        else:
                                print('\nVocê ainda não fez nenhuma sugestão')
                elif op == '0':
                        return
                
def historico(historico_passageiros,login):
        if login in historico_passageiros:
                        for id in historico_passageiros[login]:
                                print(f'\n{historico_passageiros[login][id][0]}')
                                print(f'Motorista: {historico_passageiros[login][id][1]}')
                                print(f'Valor: {historico_passageiros[login][id][2]}')
        else:
                print('\nVocê ainda não pegou nenhuma carona!')


def deletar_conta(usuarios):
        confimarcao_de_exclusao = input('Sua conta será excluida permanentemente do nosso sistema, você tem certeza que deseja continuar? (s)(n) ').lower()
        if confimarcao_de_exclusao == 's':
                        print('\nSua conta foi deletada com sucesso!')
                        usuarios.pop(login)
                        logado = False
                        return
        else:
                        return
        

def logout():
        confimarcao_de_logout = input('Deseja realmente sair? (S)(N)')
        if confimarcao_de_logout == 'sim' or confimarcao_de_logout == 's':
                print('\nVocê foi desconectado.')
                return False, 'start'
        return


def importar_usuarios(usuarios):

        with open('E:\\Algorítimo e Lógica de programação\\Phyton\\usuarios\\usuarios.txt', 'r') as cadastros:
                for linha in cadastros:
                        email, nome, senha = linha.strip().split(',')
                        usuarios[email] = {
                                'nome': nome,
                                'senha': senha,
                        }
        print('\nUsuários importados com sucesso! \n')
        return 'start'

def relatorio_totalizador(caronas,login):
        if login not in caronas or not caronas[login]:
                print('Não há caronas cadastradas!')
                return
        
        total_geral = 0
        total = 0

        print(f'\n Olá, {login}, estas são suas caronas cadastradas:\n')
        for carona_id in caronas[login]:
                ocupado = len(caronas[login][carona_id]['Reservas'])
                disponiveis = caronas[login][carona_id]['Vagas'] - ocupado
                resultado = caronas[login][carona_id]['Valor'] * ocupado

                print(f'Carona: {carona_id}')
                print(f'Origem: {caronas[login][carona_id]['Origem']}')
                print(f'Destino: {caronas[login][carona_id]['Destino']}')
                print(f'Data: {caronas[login][carona_id]['Data']}')
                print(f'Horário: {caronas[login][carona_id]['Horário']}')
                print(f'Valor por vaga: R$ {caronas[login][carona_id]['Valor']}')
                print(f'Vagas totais: {caronas[login][carona_id]['Vagas']}')
                print(f'Vagas ocupadas: {ocupado}')
                print(f'Vagas restantes: {disponiveis}')
                print(f'Total a receber: R$ {total:.2f}')
                print('----------------------------------------')

                total_geral += total

        print(f'\nTotal a receber por caronas oferecidas: R$ {total_geral:.2f}\n')
        salvar_relatorio(caronas,login)

def salvar_relatorio(caronas,login):

        salvar = input('\nDeseja salvar o relatório? (S)(N) ').lower()

        pasta = r'E:\Algorítimo e Lógica de programação\Phyton\relatorio'
        if not os.path.exists(pasta):
                os.makedirs(pasta)

        if salvar == 's':
                total_geral = 0
                total = 0
                
                with open('E:\\Algorítimo e Lógica de programação\\Phyton\\relatorio\\relatio.txt', 'w') as arquivo:

                        arquivo.write(f'\n Olá, {login}, estas são suas caronas cadastradas:\n')
                        for carona_id in caronas[login]:
                                ocupado = len(caronas[login][carona_id]['Reservas'])
                                disponiveis = caronas[login][carona_id]['Vagas'] - ocupado
                                resultado = caronas[login][carona_id]['Valor'] * ocupado

                                arquivo.write(f'Carona: {carona_id}')
                                arquivo.write(f'Origem: {caronas[login][carona_id]['Origem']}')
                                arquivo.write(f'Destino: {caronas[login][carona_id]['Destino']}')
                                arquivo.write(f'Data: {caronas[login][carona_id]['Data']}')
                                arquivo.write(f'Horário: {caronas[login][carona_id]['Horário']}')
                                arquivo.write(f'Valor por vaga: R$ {caronas[login][carona_id]['Valor']}')
                                arquivo.write(f'Vagas totais: {caronas[login][carona_id]['Vagas']}')
                                arquivo.write(f'Vagas ocupadas: {ocupado}')
                                arquivo.write(f'Vagas restantes: {disponiveis}')
                                arquivo.write(f'Total a receber: R$ {total:.2f}')
                                arquivo.write('----------------------------------------')

                                total_geral += total

                        arquivo.write(f'\nTotal a receber por caronas oferecidas: R$ {total_geral:.2f}\n')
                        print('Relatório salvo com sucesso!')
                        