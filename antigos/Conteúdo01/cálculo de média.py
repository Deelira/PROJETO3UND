# "Cálculo de média aritmétrica"
ava1 = int (input ("Digite o valor da 1ª avaliação: "))
ava2 = int (input ("Digite o valor da 2ª avaliação: "))
ava3 = int (input ("Digite o valor da 3ª avaliação: "))
calculo = (ava1 + ava2 + ava3) / 3
if calculo >= 7 :
    print(f"Parabéns, sua média final é {calculo:.2f}, você foi aprovado!")
else:
    print(f"Que pena, sua média final é {calculo:.2f}, você foi reprovado!")