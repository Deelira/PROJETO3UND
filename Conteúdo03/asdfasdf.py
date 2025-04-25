multiplicador = 1
multiplicando = 1

while multiplicando < 9:
    for multiplicador in range(11):
        print(f'{multiplicador} x {multiplicando} = {multiplicando*multiplicador}')
        multiplicando += 1