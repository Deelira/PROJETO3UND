#operador aritmético de exponenciação

peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura:"))

imc = peso / (altura ** 2)
imc= round(imc, 2)
print(f"meu IMC é {imc}")
