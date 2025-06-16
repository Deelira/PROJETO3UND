'''
Seu cliente tem um funilaria. Faça um programa que receba os dados de um proprietário do veículo o qual a oficina
irá prestar o serviço, receba também o serviço a ser executado e o valor para cada serviço.
Exiba o nome do proprietário e em seguida o seu orçamento.
'''

total = 0
# Dados do cliente
cliente = []
cpf = []
contato = []

# Dados do veículo
placa = []
cor = []
servicos = []

#outros dados
valor = []
valor_final = []

# Cadastro de cliente
while True:
    nome = input('Digite o nome do cliente: ')
    cliente.append(nome)
    
    doc = input('Digite o cpf do cliente: ')
    cpf.append(doc)

    tel = input('Digite o telefone para contato: ')
    contato.append(tel)

    num = input('Digite a placa do veículo: ')
    placa.append(num)

    cor_r = input('Digite a cor do veículo: ')
    cor.append(cor_r)
# Cadastro de serviço
    desc_servico = 's'
    while desc_servico != 'n':
        servico = input('Descreva o serviço: ')
        servicos.append(servico)

        preco = float(input('Digite o valor do serviço: '))
        valor.append(preco)

        desc_servico = input('Deseja adicionar outro serviço? (S) (N) ').lower()
#calcular o valor total
        if desc_servico == 'n':
            for i in (valor):
                total += i
                valor_final.append(total)

    print(cliente)
    print(cpf)
    print(contato)
    print(placa)
    print(cor)
    print(servicos)
    print(valor)
    print(total)