import funcoes_usuarios

usuarios = dict()
caronas = dict()
sugestoes = dict()
historico_passageiros = dict()
menu_validos = ['0', '1', '2','voltar','sair','start']
sub_menu_validos = ['0','1','2','3','4','5','6','7','8','9','10','11','voltar','sair','start']
menu = 'start'
login = None
senha = None

usuarios['3deelira@gmail.com'] = {
                'nome': 'alisson lira',
                'senha': 'deelira123',
}
caronas['3deelira@gmail.com'] = {
                        'Carona1' : {
                        'Motorista' : 'alisson lira',
                        'Origem' : 'cajazeiras',
                        'Destino': 'joão pessoa',
                        'Data' : '20/06/2025',
                        'Horário': '16:30',
                        'Vagas' : 3,
                        'Valor' : 100.00,
                        'Reservas' : dict()
                    }}
caronas['jeff@gmail.com'] = {
                        'Carona1' : {
                        'Motorista' : 'jefferson lira',
                        'Origem' : 'cajazeiras',
                        'Destino': 'joão pessoa',
                        'Data' : '20/06/2025',
                        'Horário': '18:30',
                        'Vagas' : 3,
                        'Valor' : 100.00,
                        'Reservas' : dict()
                    }}

while menu == 'start':
    print('\n \n======================== M E N U ========================\n')
    print('\n1 - CADASTRAR USUÁRIO', end='         ')
    print('2 - LOGIN', end='         ')
    print('0 - SAIR')
    print('\nSeja bem vindo ao Vamo ou Bora, o seu aplicativo de caronas!', end= ' ')
    menu = input('O que você deseja? ').lower()

    if menu not in menu_validos:
        print('Desculpe, digite uma opção válida!')
        menu = 'start'

    while menu == '1':
        funcoes_usuarios.cadastrar_usuario(usuarios)
        menu = '2'

    while menu == '2':
        funcoes_usuarios.login(login,senha)
        while logado:
            sub_menu = 'start'
            print('\n================================================================')
            print(f'================ Seja bem vindo, {usuarios[login]['nome']} ==================')
            print('================================================================')
            print('\n1 - CADASTRAR CARONA')
            print('2 - LISTAR TODAS AS CARONAS')
            print('3 - BUSCAR CARONA POR ORIGEM E DESTINO')
            print('4 - RESERVAR VAGA EM CARONA')
            print('5 - CANCELAR RESERVA EM CARONA')
            print('6 - REMOVER CARONA')
            print('7 - MOSTRAR DETALHES DE UMA CARONA')
            print('8 - MOSTRAR CARONAS CADASTRADAS')
            print('9 - SERVIÇO DE ATENDIMENTO AO CLIENTE')
            print('10 - HISTÓRICO DE CARONAS')
            print('11 - DELETAR CONTA')
            print('0 - LOGOUT\n')
            print('\n================================================================')
            print('================================================================\n')
            sub_menu = (input('Digite a opção desejada: ')).lower()

            while sub_menu == '1':
                print('\nDigite "voltar" para ser redirecionado ao menu')
                origem = input('\nQual a origem da sua carona? ').lower()
                if origem == 'voltar':
                    sub_menu = 'start'
                    break
                destino = input('Qual o destino? ').lower()
                if destino == 'voltar':
                    sub_menu = 'start'
                    break
                data_carona = input('Qual a data da carona? dd/mm/aaaa: ').lower()
                if data_carona == 'voltar':
                    sub_menu = 'start'
                    break
                if len(data_carona) < 9 or data_carona[2] != '/' and data_carona[5] != '/':
                    print('\nFormato de data inválida!')
                else:
                    horario = input('Que horas você vai? (hh:mm) ').lower()
                    if horario[2] != ':' and len(horario) != 5:
                        print('Horário iválido!')
                    else:
                        vagas = int(input('Quantas vagas disponíveis em seu veículo? '))
                        valor_carona = float(input('Qual o valor de cada vaga? '))
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
                        sub_menu = 'start'
                        break

            if sub_menu == '2':
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

            elif sub_menu == '3':
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

            while sub_menu == '4':
                print('\nDigite "voltar" para ser redirecionado ao menu\n')
                email_motorista = input('Digite o email do motorista o qual você deseja pegar carona: ').lower()
                if email_motorista == 'voltar':
                    sub_menu = 'start'
                    break
                data_carona_reservar = input('Digite a data da carona (dd/mm/aaaa):  ').lower()
                if data_carona_reservar == 'voltar':
                    sub_menu = 'start'
                    break
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
                                print('\nReserva efetuada com sucesso!')
                                if login not in historico_passageiros:
                                    historico_passageiros[login] = dict()
                                num_reserva_passageiro = len(historico_passageiros[login]) + 1
                                historico_passageiros[login][num_reserva_passageiro] = [caronas[email_motorista][id]['Data'], caronas[email_motorista][id]['Motorista'], caronas[email_motorista][id]['Valor']]
                            else:
                                print('\nQue pena, não há mais vagas!')
                            sub_menu = 'start'
                            break
                else:
                    print('\nNenhuma carona oferecida por esse motorista!')

            if sub_menu == '5':
                reserva_encontrada = False
                print('\nDigite "voltar" a qualquer momento para retornar ao menu')
                email_cancelar = input('Digite o email do motorista o qual você deseja cancelar carona: ').lower()
                if email_cancelar == 'voltar':
                    sub_menu = 'start'
                    break
                data_carona_cancelar = input('Digite a data da carona: (dd/mm/aaaa) ').lower()
                if data_carona_cancelar == 'voltar':
                    sub_menu = 'start'
                    break
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
                                            break
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

            if sub_menu == '6':
                carona_a_remover = False
                if login not in caronas or len(caronas[login]) < 1:
                        sub_menu = 'start'
                        print('\nVocê não tem nenhuma carona cadastrada!')
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
                                sub_menu = 'start'
                            else:
                                print('\nVocê não tem nenhuma carona cadastrada nesta data!')
                                sub_menu = 'start'

            if sub_menu == '7':
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

            if sub_menu == '8':
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

            if sub_menu == '9':
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
                    sub_menu = 'start'

            if sub_menu == '10':
                if login in historico_passageiros:
                    for id in historico_passageiros[login]:
                        print(f'\n{historico_passageiros[login][id][0]}')
                        print(f'Motorista: {historico_passageiros[login][id][1]}')
                        print(f'Valor: {historico_passageiros[login][id][2]}')
                else:
                    print('\nVocê ainda não pegou nenhuma carona!')

            if sub_menu == '11':
                confimarcao_de_exclusao = input('Sua conta será excluida permanentemente do nosso sistema, você tem certeza que deseja continuar? (s)(n) ').lower()
                if confimarcao_de_exclusao == 's':
                    print('\nSua conta foi deletada com sucesso!')
                    usuarios.pop(login)
                    logado = False
                    menu = 'start'
                    break
                else:
                    sub_menu = 'start'
                    break

            if sub_menu == '0' or sub_menu == 'sair':
                print('\nVocê foi desconectado.')
                logado = False
                menu = 'start'
                break

            if sub_menu not in sub_menu_validos:
                print('\nDigite uma opção válida!')

    if menu == '0':
        print('\nValeu, até a próxima carona!')