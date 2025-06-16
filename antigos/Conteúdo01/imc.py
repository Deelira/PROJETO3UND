# calculando o IMC
altura = float(input("Digite a sua altura:")) #Utilizar float para números decimais
peso = float(input("Digite o seu peso:"))
nome = input("Digite o seu nome:") #Apenas input para strings ( textos )
imc = peso / (altura * altura) # Fórmula do IMC
imc = round(imc, 2) #mostra o resultado em apenas duas casas decimais
print(nome, "possui imc igual a", imc)