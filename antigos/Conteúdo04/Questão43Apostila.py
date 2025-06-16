'''
O cardápio de uma lanchonete é o seguinte:

Especificação Código Preço
Cachorro Quente 100 R$ 1,20
Bauru Simples 101 R$ 1,30
Bauru com ovo 102 R$ 1,50
Hambúrguer 103 R$ 1,20
Cheeseburguer 104 R$ 1,30
Refrigerante 105 R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser
pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido
deve ser encerrado.

'''

produtos = [['Cachorro Quente', 100, 1.20], ['Bauru Simples', 101, 1.30], ['Bauru com ovo', 102, 1.50], ['Hamburguer', 103, 1.20], ['Cheeseburguer', 104, 1.30], ['Refrigerante', 105, 1.00]]

op = 's'
total = 0
indice = ''
valor_final = []

for i in produtos:
    print(i)

while op != 'n':
    item = int(input('Digite o código do produto: '))
    quant = int(input('Digite a quantidade de produtos: '))
    for i in produtos:
        if i[1] == item:
            total += (i[2]*quant)
            print(f'{i} * {quant} = {total}')
            valor_final.append(total)
    op = input('Deseja adicionar um novo item? (S) (N) ').lower()
    total = 0

print(f'Total: {sum(valor_final)}')