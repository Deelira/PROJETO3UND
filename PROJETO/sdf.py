cadastros = {}
cadastros['3deelira@gmail.com'] = {
                'nome': 'alisson lira',
                'senha': 'deelira123',
}

print(cadastros)




for motorista in caronas:
                            lista_viagens = caronas[motorista]
                            
                        for viagem in lista_viagens:
                            if email_cancelar == motorista and viagem['Data'] == data_carona:
                                viagem_existente = True

                        if viagem_existente:
                            num_vagas = viagem['Vagas']
                            if num_vagas >= 0:
                                num_vagas += 1
                                viagem['Vagas'] = num_vagas
                                caronas[email_motorista] -= [{'Reserva': login }]
                                print('\nReserva cancelada com sucesso!')