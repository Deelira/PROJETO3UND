'''
Faça um sistema que mostre a tabuada de multiplicação do 1 até o 9. use um for dentro do outro for
'''
#multiplicador = 1

#for multiplicando in range (11):
#    resultado = multiplicador * multiplicando
#    print(f'{multiplicador} * {multiplicando} = {resultado}')

for i in range(10):
    for j in range(10):
        print (f'{i} x {j} = {i*j}')
        