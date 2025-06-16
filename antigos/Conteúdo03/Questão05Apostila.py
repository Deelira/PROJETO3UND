pais_A = int(input('Digite a população do país A: '))
Taxa_A = float(input('Digite a taxa de crescimento do país A: '))
Taxa_A = 1 + Taxa_A/100
pais_B = int(input('Digite a população do país B: '))
Taxa_B = float(input('Digite a taxa de crescimento do país A: '))
Taxa_B = 1 + Taxa_B/100
anos = 0


while pais_A <= pais_B:
    pais_A *= Taxa_A
    pais_B *= Taxa_B
    anos += 1
    print (f'Pais A {pais_A:.0f}, Pais B {pais_B:.0f}')
print(anos)