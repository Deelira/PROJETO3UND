
# criando dicionários

cadastros = dict()
caronas = dict()

# adicionando dados aos dicionários

cadastros['3deelira@gmail.com'] = {
                'nome': 'alisson lira',
                'senha': 'deelira123',
}
caronas['3deelira@gmail.com'] = {
                        'Carona1' : {
                        'Motorista' : 'Alisson Lira',
                        'Origem' : 'cajazeiras',
                        'Destino': 'joão pessoa',
                        'Data' : '20/06/2025',
                        'Horário': '16:30',
                        'Vagas' : 3,
                        'Valor' : 100.00,
                        'Reservas' : ''
                    }}
#Loop menu principal

menu = 99
while menu != 0:
    print('\n-------------------------- M E N U --------------------------\n')
    print('1 - CADASTRO DE USUÁRIO')
    print('2 - LOGIN')
    print('0 - SAIR')
    menu = int(input('\nDigite a opção desejada: '))
    
# cadastro de usuário

    while menu == 1:
        nome = input('\nDigite o seu nome completo: ').lower()
        nome_completo = False

        if len(nome) <= 6 or ' ' not in nome:
            print('\nPor favor, digite o seu nome completo!\n')
# perguntar o email novamente caso o usuário não utilize o caractere obrigatório
        else:
            nome_completo = True

        while nome_completo:
            email = input('Digite o seu e-mail: ').lower()

            if '@' and '.com' not in email:
                print('\nEmail inválido!\n')

            elif email in cadastros:
                print('\nEmail já cadastrado!\n')
                menu = 99
                break

            else:
                senha = input('Digite sua senha (mín. 6 caracteres): ').lower()

                if len(senha) < 6:
                    print('\nSenha inválida!')

                else:
                    cadastros[email] = {
                        'nome': nome,
                        'senha': senha,
                    }
                    print('\nCadastro efetuado com sucesso!')
                    menu = 99
                    break

# login

    while menu == 2:

        obrigatorio = False
        logado = False

        login = input('\nDigite o seu email: ').lower()

        if '@' and '.com' in login:
            obrigatorio = True
        
            if obrigatorio:
                senha_user = input('Digite a sua senha: ').lower()
                
                if login in cadastros and cadastros[login]['senha'] == senha_user:
                    print(f'\nSeja bem vindo, {cadastros[login]['nome']}')
                    logado = True
                else:
                    print('Email ou senha incorretos!')
                    menu = 99
                    break
        else:
            print('Email inválido!')

# se conseguiu efetuar login

        while logado == True:

            sub_menu = 99
            print('\n1 - CADASTRO DE CARONA')
            print('2 - LISTAR TODAS AS CARONAS')
            print('3 - BUSCAR CARONA POR ORIGEM E DESTINO')
            print('4 - RESERVAR VAGA EM CARONA')
            print('5 - CANCELAR RESERVA')
            print('6 - REMOVER CARONA')
            print('7 - MOSTRAR DETALHES DA CARONA')
            print('8 - MOSTRAR CARONAS CADASTRADAS')
            print('EXTRA ( A PENSAR )')
            print('10 - LOGOUT\n')
            sub_menu = int(input('Digite a opção desejada: '))

# loop sub menu

            while sub_menu != 0:

# cadastrar carona

                if sub_menu == 1:

                    origem = input('Digite a origem da sua viagem: ').lower()
                    destino = input('Digite o destino da sua viagem: ').lower()
                    data = input('Digite a data da sua viagem: ').lower()
                    horario = input('Digite o horário da sua viagem: ').lower()
                    vagas = int(input('Digite a quantidade de vagas disponíveis: '))
                    valor_passageiro = float(input('Digite o valor para cada passageiro: R$ '))           

                    nova_carona = {
                        'Motorista' : cadastros[login]['nome'],
                        'Origem' : origem,
                        'Destino': destino,
                        'Data' : data,
                        'Horário': horario,
                        'Vagas' : vagas,
                        'Valor' : valor_passageiro,
                        'Reservas' : ''
                    }
                    
                    if login not in caronas:
                        caronas[login] = {}
                        
                    id_carona = (f'carona{len(caronas[login]) + 1}')
                    caronas[login][id_carona] = nova_carona
                    print('\nCarona cadastrada com sucesso!\n')
                    break

# listar caronas

                elif sub_menu == 2:
                        print(caronas)
                        sub_menu = 99
                        break
                
# buscar caronas por origem e destino

                elif sub_menu == 3:
                    
                    origem_viagem = input('\nDigite a origem da carona: ').lower()
                    destino_viagem = input('Digite o destino da carona: ').lower()
                    carona_existente = False

                    for motorista in caronas:
                        lista_caronas = caronas[motorista]

                        for id_carona in lista_caronas:
                            carona = lista_caronas[id_carona]

                            if carona['Origem'] == origem_viagem and carona['Destino'] == destino_viagem:
                                print(f'\nCarona encontrada com: {motorista}')
                                print(f'Origem: {carona['Origem']}')
                                print(f'Destino: {carona['Destino']}')
                                print(f'Data: {carona['Data']}')
                                print(f'Horário: {carona['Horário']}')
                                print(f'Vagas: {carona['Vagas']}')
                                print(f'Valor: R$ {carona['Valor']:.2f}\n')
                                carona_existente = True

                    if not carona_existente:
                        print('Carona não encontrada!')

                    sub_menu = 99
                    break

# reservar vaga em carona

                elif sub_menu == 4:
                    obrigatorio = False
                    email_motorista = input('\nDigite o email do motorista cuja carona você deseja reservar: ').lower()
                    data_carona = input('Digite a data da carona: ').lower()

# confere se tem o caractere obrigatório

                    if '@' and '.com' in email_motorista:
                        obrigatorio = True

                    if obrigatorio == True:
                        viagem_existente = False

                        for motorista in caronas:
                            lista_caronas = caronas[motorista]

                            for id_carona in lista_caronas:
                                    carona = lista_caronas[id_carona]

                                    if email_motorista == motorista and carona['Data'] == data_carona:
                                        viagem_existente = True
                                    
                        if viagem_existente:
                            if carona['Vagas'] > 0 and login not in carona['Reservas'] and login != email_motorista:
                                    carona['Vagas'] -= 1
                                    carona['Reservas'] = login
                                    print('\nReserva efetuada com sucesso!')
                            elif login == email_motorista:
                                print('\nVocê é o motorista desta viagem, não pode reservar vaga!\n')
                            elif login in carona['Reservas']:
                                print('\nVocê já tem um reserva efetuada para esta viagem!\n')
                        else:
                            print('Viagem não encontrada!')

                        sub_menu = 99
                        break

                    else:
                        print('\nEmail ou data inválido!')
                        break

# cancelar reserva ( REFAZER )

                elif sub_menu == 5:

                    obrigatorio = False
                    email_cancelar = input('\nDigite o email do motorista cuja carona você deseja cancelar: ').lower()
                    data_cancelar = input('\nDigite a data da carona: ').lower()

                    if '@' and '.com' in email_cancelar:
                        obrigatorio = True

                    if obrigatorio == True:
                        reserva_encontrada = False

                        for motorista in caronas:
                            lista_caronas = caronas[motorista]

                            for id_carona in lista_caronas:
                                    carona = lista_caronas[id_carona]

                                    if email_cancelar == motorista and carona['Data'] == data_cancelar:
                                        reserva_encontrada = True

                        if reserva_encontrada:
                            if carona['Reservas'] == login:
                                carona['Vagas'] += 1                                
                                caronas[email_cancelar][id_carona].pop('Reservas')
                                print('\nReserva cancelada com sucesso!')
                                sub_menu = 99
                        
                        else:
                            print('Você não possui reserva nessa carona!')
                            sub_menu = 99
                        break

                    else:
                        print('\nEmail ou data inválido!')
                        break
                
# cancelar carona

                elif sub_menu == 6:
                    data_encontrada = False
                    cancelar = input('Digite a data da carona que deseja cancelar: ').lower()

                    if login in caronas:
                        lista_caronas_existentes = caronas[login]

                        for id_carona in lista_caronas_existentes:
                            if lista_caronas_existentes[id_carona]['Data'] == cancelar:
                                data_encontrada = True
                                break

                        if data_encontrada:
                            caronas[login].pop(id_carona)
                            print('\nCarona cancelada com sucesso!')
                            break
                        else:
                            print('\nCarona não encontrada!')
                    else:
                        print('\nVocê não tem carona cadastrada!')
                        break

# detalhes da carona

                elif sub_menu == 7:
                    
                    email_motorista = input('\nDigite o email do motorista: ').lower()
                    data_carona = input('Digite a data da carona: ').lower()
                    carona_existente = False

                    for motorista in caronas:
                        lista_caronas = caronas[motorista]

                        for id_carona in lista_caronas:
                            carona = lista_caronas[id_carona]

                            if carona['Data'] == data_carona and email_motorista == motorista:
                                print(f'\nCarona encontrada!\n')
                                print(f'Motorista: {carona['Motorista']}')
                                print(f'Origem: {carona['Origem']}')
                                print(f'Destino: {carona['Destino']}')
                                print(f'Data: {carona['Data']}')
                                print(f'Horário: {carona['Horário']}')
                                print(f'Vagas: {carona['Vagas']}')
                                print(f'Valor: R$ {carona['Valor']:.2f}\n')
                                print(f'Reservas: {carona['Reservas']}\n')
                                carona_existente = True

                    if not carona_existente:
                        print('Carona não encontrada!')

                    sub_menu = 99
                    break

# mostrar caronas do usuário logado

                elif sub_menu == 8:
                    if login in caronas:
                        print(caronas[login])
                    else:
                        print('\nNenhuma carona cadastrada!\n')
                    break
# logout
                elif sub_menu == 10:
                        print('\nVocê foi desconectado!\n')
                        logado = False
                        menu = 99
                        break

                else:
                    print('\nOpção inválida!')
                    break
    
    if menu == 0:
        print('\nVamo ou Bora agradece a preferência. \nAté a próxima carona!\n')
        break
    elif menu > 0 and menu != 99:
        print('\nOpção inválida!')