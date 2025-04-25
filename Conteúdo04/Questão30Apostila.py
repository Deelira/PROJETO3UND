'''
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um
sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1
até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
'''
valor_pao = float(input('Digite o preço atual do pão: R$ '))
print(f'\nPreço do Pão: R$ {valor_pao}')
print('Panificadora Pão de Ontem - Tabela de preços\n')

for i in range(1,51):
    total = valor_pao * i
    print(f'{i} - R$ {total:.2f}')