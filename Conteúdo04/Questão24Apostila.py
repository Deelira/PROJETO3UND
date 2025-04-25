'''
. Faça um programa que calcule o mostre a média aritmética de N notas.
'''
notas = 0
total = 0

while True:
    nota = float(input('Digite a nota: '))
    notas += 1
    total += nota
    parar = input('Deseja adicionar outra nota? (S) (N) ').lower()
    if parar == 's':
        continue
    elif parar == 'n':
        break

media = total / notas
print(f'Sua média é {media:.1f}')