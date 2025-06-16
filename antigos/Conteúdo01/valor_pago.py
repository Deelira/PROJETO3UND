valor = float(input('Digite o valor do produto: '))
pago = float(input('Digite o valor pago: '))

if pago >= valor:
    print('O produto está pago')
    troco = pago - valor
    print(f'Você comprou o produto e o troco é {troco}')

else:
    falta = valor - pago
    print(f'Falta você pagar {falta}')