total = 0
# Dados do cliente
cliente = input('Digite o nome do cliente: ')
cpf = input('Digite o CPF do cliente: ')
contato = input('Digite o telefone para contato: ')

# Dados do veículo
placa = input('Digite a placa do veículo: ')
cor = input('Digite a cor do veículo: ')

# Cadastro de serviços
servicos = []
valor = []

desc_servico = 's'
while desc_servico == 's':
    servico = input('Descreva o serviço: ')
    preco = float(input('Digite o valor do serviço: '))
    
    servicos.append(servico)
    valor.append(preco)

    desc_servico = input('Deseja adicionar outro serviço? (S) (N): ').lower()

# Calcular o valor total
total = sum(valor)

# Exibir orçamento
print('\n--- ORÇAMENTO ---')
print(f'Cliente: {cliente}')
print(f'CPF: {cpf}')
print(f'Contato: {contato}')
print(f'Veículo: Placa {placa}, Cor {cor}')
print('\nServiços:')
for s, v in zip(servicos, valor):
    print(f'- {s}: R$ {v:.2f}')
print(f'\nValor total: R$ {total:.2f}')