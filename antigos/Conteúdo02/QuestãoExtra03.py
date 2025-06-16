'''
Faça um algoritmo que receba um valor inicial do usuário e exiba o valor final após alguns anos. O usuário deverá
informar o ano inicial, o ano final e cada ano deve ser einformado o valor da selic
'''

valor = float(input('Digite o valor do seu investimento: '))
ano_inicial = int(input('Digite o ano inicial do investimento: '))
ano_final = int(input('Digite o ano da retirada do seu investimento: '))

for ano in range (ano_inicial, ano_final + 1):
    print(f'Estamos em {ano}', end=',')
    selic = float(input('qual o valor da selic deste ano: '))

    if selic <= 8.5:
        juros = selic * 0.7
        valor = valor * (1 + (juros/100))
    else:
        valor = valor * (1 + 0.06)

ano = ano_final - ano_inicial

print(f'O valor final do seu investimento após {ano} anos foi {valor:.2f}')