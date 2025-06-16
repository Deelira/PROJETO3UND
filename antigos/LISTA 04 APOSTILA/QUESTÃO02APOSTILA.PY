reais = []

for i in range (10):
    num = float(input('Digite um número real: '))
    reais.append(num)

for j in range(len(reais) -1, -1, -1):
    print(reais[j], end=(' '))

reais.sort(reverse=True)
print(f'\n{reais}')