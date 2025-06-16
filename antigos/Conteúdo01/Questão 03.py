# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M -
# Masculino, Sexo Inválido.

letra = input('Digite a letra que representa o seu sexo: ')
letra = letra.upper()

if letra == 'F':
    print('Você escolheu o sexo Feminino')

if letra == 'M':
        print('Você escolheu o sexo Masculino')

else:
    print('A letra digitada está incorreta, digite (F) ou (M)')