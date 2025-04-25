'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número
desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para
indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente
forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
'''
produtos = []

while True:

    novo_produto = 1000
    valor = 0
    total = 0

    for i in range(novo_produto):
        valor = float(input('Digite o valor do produto: R$ '))
        total = total + valor
        produtos.append(f'Produto{i+1}: R$ {valor}')

        if valor == 0:
            break
    
    print(f'\n{total}')

    dinheiro = float(input('\nDigite o valor pago pelo cliente: R$ '))
    troco = dinheiro - total

    if dinheiro < total:
        print(f'Ops, o cliente não entregou dinheiro suficiente para a compra, ainda faltam R$ {troco*-1:.2f}')
    else:
        print('\nLojas Tabajara')
        for p in produtos:
            print(p)
        print(f'Total: R$ {total:.2f}')
        print(f'Dinheiro: R$ {dinheiro}')
        print(f'Troco: R$ {troco}')
        print('...\n')