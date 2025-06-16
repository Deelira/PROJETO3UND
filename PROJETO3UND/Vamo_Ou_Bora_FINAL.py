import funcoes_usuarios

usuarios = dict()
caronas = dict()
sugestoes = dict()
historico_passageiros = dict()
menu_validos = ['0', '1', '2', '3', 'voltar', 'sair', 'start']
sub_menu_validos = ['0','1','2','3','4','5','6','7','8','9','10','11', '12','voltar','sair','start']
menu = 'start'
login = None
senha = None
arquivo_usuarios = 'E:\\Algorítimo e Lógica de programação\\Phyton\\usuarios\\usuarios.txt'

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
    print('3 - IMPORTAR USUARIOS', end='         ')
    print('0 - SAIR')
    print('\nSeja bem vindo ao Vamo ou Bora, o seu aplicativo de caronas!', end= ' ')
    menu = input('O que você deseja? ').lower()

    if menu not in menu_validos:
        print('Desculpe, digite uma opção válida!')
        menu = 'start'

    while menu == '1':
        funcoes_usuarios.cadastrar_usuario(usuarios, arquivo_usuarios)
        menu = '2'

    while menu == '2':
        login = funcoes_usuarios.login(usuarios,menu)

        if login is not None:
            logado = True
            while logado:
                sub_menu = 'start'
                print('\n================================================================')
                print(f"================ Seja bem vindo, {usuarios[login]['nome']} ==================")
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
                print('12 - RELATÓRIO TOTALIZADOR')
                print('0 - LOGOUT\n')
                print('\n================================================================')
                print('================================================================\n')
                sub_menu = (input('Digite a opção desejada: ')).lower()

                if sub_menu == '1':
                    funcoes_usuarios.cadastrar_carona(caronas,usuarios,login)

                if sub_menu == '2':
                    funcoes_usuarios.listar_caronas(caronas)

                if sub_menu == '3':
                    funcoes_usuarios.bucar_por_origem(caronas)

                if sub_menu == '4':
                    funcoes_usuarios.reservar_vaga(caronas,login,historico_passageiros,usuarios)

                if sub_menu == '5':
                    funcoes_usuarios.cancelar_reserva(caronas,login,usuarios)

                if sub_menu == '6':
                    funcoes_usuarios.remover_carona(caronas,login)

                if sub_menu == '7':
                    funcoes_usuarios.detalhar_carona(caronas,login)

                if sub_menu == '8':
                    funcoes_usuarios.caronas_cadastradas(caronas,login)

                if sub_menu == '9':
                    funcoes_usuarios.sac(sugestoes)

                if sub_menu == '10':
                    funcoes_usuarios.historico(historico_passageiros,login)

                if sub_menu == '11':
                    funcoes_usuarios.deletar_conta(usuarios)

                if sub_menu == '12':
                    funcoes_usuarios.relatorio_totalizador(caronas,login)

                if sub_menu == '0' or sub_menu == 'sair':
                    logado,menu = funcoes_usuarios.logout()
                
                if sub_menu not in sub_menu_validos:
                    print('\nDigite uma opção válida!')
        else:
            menu = 'start'

    if menu == '3':
        menu = funcoes_usuarios.importar_usuarios(usuarios)

    if menu == '0':
        print('\nValeu, até a próxima carona!')