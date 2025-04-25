# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
#triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado01 = int(input('Digite o tamanho do primeiro lado do triângulo: '))
lado02 = int(input('Digite o tamanho do segundo lado do triângulo: '))
lado03 = int(input('Digite o tamanho do terceiro lado do triângulo: '))

if lado01 + lado02 > lado03 and lado02 + lado03 > lado01 and lado01 + lado03 > lado02:
    if lado01 == lado02 and lado02 == lado03:
        print('Este é um triângulo Equilátero')
    if lado01 != lado02 and lado02 != lado03 and lado01 != lado03:
        print('Este é um triângulo Escaleno')
    if (lado01 == lado02 and lado02 != lado03) or (lado02 == lado03 and lado01 != lado03)or (lado03 == lado01 and lado02 != lado01):
        print('Este é um triângulo Isósceles')