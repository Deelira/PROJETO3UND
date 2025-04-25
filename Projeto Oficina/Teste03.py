
# criando uma lista para salvar os dados cadastrados

clientes = []
menu = 1

# loop para o menu

while menu != 0:
    print('\n---------------Menu---------------')
    print('\n1 - Cadastrar cliente')
    print('2 - Cadastrar serviço')
    print('3 - Buscar serviços')
    print('0 - Sair')

    menu = int(input('\nDigite a opção desejada: '))

# cadastro de clientes

    if menu == 1:
        nome = input('Digite o nome do cliente: ').lower()
        num = int(input('Digite o cpf do cliente: '))
        tel = int(input('Digite o telefone do cliente: '))

        cpf_existe = False
        
        for c in clientes:
            if c['cpf'] == num:
                cpf_existe = True
                break
            
        if not cpf_existe:
            novo_cliente = {
            'nome': nome,
            'cpf': num,
            'telefone': tel,
            'veiculo': '',
            'servicos': []
        }
            clientes.append(novo_cliente)
            print('\nCliente cadastrado com sucesso!')
        else:
            print('\nCliente ou CPF já cadastrados')

# cadastro de serviços

    elif menu == 2:
            cpf_cliente = int(input('Digite o cpf do cliente: '))

            cliente = None

            for c in clientes:
                if c['cpf'] == cpf_cliente:
                     cliente = c
                     break
            if cliente:
                cliente['veiculo'] = input('Digite o nome do veiculo: ').lower()
               
# loop para cadastro de serviços

                cad_servico = 's'
                while cad_servico == 's':
                    servico = input('Descreva o serviço realizado: ')
                    preco = float(input('Digite o valor do serviço: '))
                    cliente['servicos'].append({'descricao': servico, 'valor': preco})
                    cad_servico = input('Deseja cadastrar outro serviço? (S) (N) ').lower()
                
                print('\n--------------Orçamento--------------')
                print(f'\nCliente: {cliente['nome']}')
                print(f'CPF: {cliente['cpf']}')
                print(f'Telefone: {cliente['tel']}')
                print(f'Veículo: {cliente['veiculo']}')
                total = 0
                for s in cliente['servicos']:
                    print(f"- {s['descricao']}: R$ {s['valor']:.2f}")
                    total += s['valor']
                print(f'\nValor total: R$ {total:.2f}')
            else:
                print('\nCPF não cadastrado!')
# buscar serviços cadastrados

    elif menu == 3:
        cpf_servico = int(input('Digite o CPF do cliente para vizualizar o histórico de serviços: '))
        
        cliente = None

        for c in clientes:
            if c['cpf'] == cpf_servico:
                cliente = c
                break
        if cliente:
            print(f'\nOs serviços registrados desse cliente são: ' + '\n', cliente['servicos'])
        else:
            print('\nCPF não cadastrado!')