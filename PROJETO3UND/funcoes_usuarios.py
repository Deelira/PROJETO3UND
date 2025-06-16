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


def cadastrar_carona(caronas,usuarios,login,arquivo_caronas):
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

        salvar_caronas(caronas, arquivo_caronas)

        print('\nNova carona cadastrada com sucesso!\n')
        return nova_carona

def salvar_caronas(caronas, arquivo_caronas):
        with open(arquivo_caronas, 'w', encoding='utf-8') as f:
                for email_motorista in caronas:
                        for id_carona in caronas[email_motorista]:
                                c = caronas[email_motorista][id_carona]

                                reservas_str = ""
                                for email_res in c['Reservas']:
                                        nome_res = c['Reservas'][email_res]
                                        reservas_str += f"{email_res}:{nome_res};"

                                reservas_str = reservas_str.rstrip(';')
                                linha = f"{email_motorista},{c['Motorista']},{c['Origem']},{c['Destino']},{c['Data']},{c['Horário']},{c['Vagas']},{c['Valor']},{reservas_str}\n"
                                f.write(linha)

def listar_caronas(arquivo_caronas):
        caronas = importar_caronas(arquivo_caronas)
        encontrou_carona = False

        for motorista in caronas:
                caronas_do_motorista = caronas[motorista]
                for id_carona in caronas_do_motorista:
                        dados = caronas_do_motorista[id_carona]
                        if dados['Vagas'] > 0:
                                encontrou_carona = True
                                print('\n==================== CARONA DISPONÍVEL ====================')
                                print(f'Motorista : {dados["Motorista"]}')
                                print(f'Origem : {dados["Origem"]}')
                                print(f'Destino : {dados["Destino"]}')
                                print(f'Data : {dados["Data"]}')
                                print(f'Horário : {dados["Horário"]}')
                                print(f'Vagas : {dados["Vagas"]}')
                                print(f'Valor R$: {dados["Valor"]:.2f}')
                                if len(dados['Reservas']) > 0:
                                        print(f'Reservas: {dados["Reservas"]}')
                                print(f'Email do motorista para reserva: {motorista}')
                                print('============================================================\n')

        if not encontrou_carona:
                print('\nInfelizmente não há caronas disponíveis no momento.\n')    

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

def reservar_vaga(caronas, login, usuarios, arquivo_caronas):
        print('\nDigite "voltar" a qualquer momento para retornar ao menu')

        email_motorista = input('Digite o email do motorista para reservar a carona: ').lower()
        if email_motorista == 'voltar':
                return

        data_carona = input('Digite a data da carona: (dd/mm/aaaa) ').lower()
        if data_carona == 'voltar':
                return

        if len(data_carona) < 9 or data_carona[2] != '/' or data_carona[5] != '/':
                print('\nFormato de data inválida!')
                return

        if email_motorista not in caronas:
                print('Nenhuma carona oferecida por esse motorista!')
                return

        carona_encontrada = None
        for id_carona in caronas[email_motorista]:
                c = caronas[email_motorista][id_carona]
                if c['Data'] == data_carona:
                        carona_encontrada = c
                        break

        if carona_encontrada is None:
                print('Nenhuma carona encontrada nessa data para esse motorista.')
                return

        if carona_encontrada['Vagas'] <= 0:
                print('Não há vagas disponíveis nessa carona.')
                return

        email_usuario = login
        nome_usuario = usuarios[login]['nome']

        reservas_dict = carona_encontrada.get('Reservas', {})
        if not isinstance(reservas_dict, dict):
                reservas_dict = {}

        if email_usuario in reservas_dict:
                print('Você já tem uma reserva nesta carona.')
                return

        reservas_dict[email_usuario] = nome_usuario
        carona_encontrada['Reservas'] = reservas_dict

        carona_encontrada['Vagas'] -= 1

        print('Reserva feita com sucesso!')

        salvar_caronas(caronas,arquivo_caronas)


def cancelar_reserva(caronas, login, usuarios, arquivo_caronas):
        print('\nDigite "voltar" para cancelar a operação.')
        email_motorista = input('Digite o email do motorista para cancelar reserva: ').lower()
        if email_motorista == 'voltar':
                return

        data_carona = input('Digite a data da carona (dd/mm/aaaa): ')
        if data_carona == 'voltar':
                return

        if email_motorista not in caronas:
                print('\nMotorista não encontrado.')
                return

        carona_encontrada = None
        for id_carona in caronas[email_motorista]:
                c = caronas[email_motorista][id_carona]
                if c['Data'] == data_carona:
                        carona_encontrada = c
                        break

        if carona_encontrada is None:
                print('\nCarona não encontrada na data indicada.')
                return

        nome_usuario = usuarios[login]['nome']

        reservas = carona_encontrada['Reservas']

        # Verifica se é dict ou str sem usar isinstance
        if type(reservas) == dict:
                reservas_lista = []
                for email, nome in reservas.items():
                        reservas_lista.append(f"{email}:{nome}")
        elif type(reservas) == str:
                if reservas.strip() == '':
                        reservas_lista = []
                else:
                        reservas_lista = reservas.strip().split()
        else:
                reservas_lista = []

        reserva_para_remover = None
        for reserva in reservas_lista:
                partes = reserva.split(':')
                if len(partes) == 2 and partes[1] == nome_usuario:
                        reserva_para_remover = reserva
                        break

        if reserva_para_remover is None:
                print('\nVocê não tem reserva nessa carona!')
                return

        reservas_lista.remove(reserva_para_remover)

        # Montar a string reservas sem usar join
        reservas_str = ''
        for r in reservas_lista:
                reservas_str += r + ' '

        # Retirar espaço extra no final
        reservas_str = reservas_str.strip()

        carona_encontrada['Reservas'] = reservas_str
        carona_encontrada['Vagas'] += 1

        print('\nReserva cancelada com sucesso!')

        with open(arquivo_caronas, 'w') as f:
                for motorista in caronas:
                        for id_c in caronas[motorista]:
                                c = caronas[motorista][id_c]
                                linha = f"{motorista},{c['Motorista']},{c['Origem']},{c['Destino']},{c['Data']},{c['Horário']},{c['Vagas']},{c['Valor']},{c['Reservas']}\n"
                                f.write(linha)

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

        pasta_usuarios = 'E:\\Algorítimo e Lógica de programação\\Phyton\\usuarios'
        if not os.path.exists(pasta_usuarios):
                os.makedirs(pasta_usuarios)

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

        pasta_relatorio = 'E:\\Algorítimo e Lógica de programação\\Phyton\\relatorio'
        if not os.path.exists(pasta_relatorio):
                os.makedirs(pasta_relatorio)

        if salvar == 's':
                total_geral = 0
                total = 0
                
                with open('E:\\Algorítimo e Lógica de programação\\Phyton\\relatorio\\relatorio.txt', 'a') as arquivo:

                        arquivo.write(f'\n Olá, {login}, estas são suas caronas cadastradas:\n')
                        for carona_id in caronas[login]:
                                ocupado = len(caronas[login][carona_id]['Reservas'])
                                disponiveis = caronas[login][carona_id]['Vagas'] - ocupado
                                resultado = caronas[login][carona_id]['Valor'] * ocupado

                                arquivo.write(f'Carona: {carona_id}\n')
                                arquivo.write(f'Origem: {caronas[login][carona_id]['Origem']}\n')
                                arquivo.write(f'Destino: {caronas[login][carona_id]['Destino']}\n')
                                arquivo.write(f'Data: {caronas[login][carona_id]['Data']}\n')
                                arquivo.write(f'Horário: {caronas[login][carona_id]['Horário']}\n')
                                arquivo.write(f'Valor por vaga: R$ {caronas[login][carona_id]['Valor']}\n')
                                arquivo.write(f'Vagas totais: {caronas[login][carona_id]['Vagas']}\n')
                                arquivo.write(f'Vagas ocupadas: {ocupado}\n')
                                arquivo.write(f'Vagas restantes: {disponiveis}\n')
                                arquivo.write(f'Total a receber: R$ {total:.2f}\n')
                                arquivo.write('----------------------------------------\n')

                                total_geral += total

                        arquivo.write(f'Total a receber por caronas oferecidas: R$ {total_geral:.2f}\n')
                        print('Relatório salvo com sucesso!')

def importar_caronas(arquivo_caronas):
        import os
        caronas = dict()
        pasta_caronas = 'E:\\Algorítimo e Lógica de programação\\Phyton\\caronas'

        if os.path.exists(pasta_caronas):
                with open(arquivo_caronas, 'r') as f:
                        for linha in f:
                                partes = linha.strip().split(',')

                                if len(partes) < 9:
                                        continue

                                email = partes[0]
                                nome = partes[1]
                                origem = partes[2]
                                destino = partes[3]
                                data = partes[4]
                                horario = partes[5]
                                vagas = int(partes[6])
                                valor = float(partes[7])
                                reservas_str = partes[8].strip()

                                reservas = {}
                                if reservas_str:
                                        pares = reservas_str.split("|")
                                        for par in pares:
                                                if ':' in par:
                                                        email_res, nome_res = par.split(":")
                                                        reservas[email_res] = nome_res

                                nova_carona = {
                                'Motorista': nome,
                                'Origem': origem,
                                'Destino': destino,
                                'Data': data,
                                'Horário': horario,
                                'Vagas': vagas,
                                'Valor': valor,
                                'Reservas': reservas
                                }

                                if email not in caronas:
                                        caronas[email] = dict()

                                id_carona = f'carona{len(caronas[email]) + 1}'
                                caronas[email][id_carona] = nova_carona

        else:
                print('Arquivo de caronas não encontrado. Será criado ao cadastrar uma nova carona.')

        return caronas