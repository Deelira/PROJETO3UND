numero = float(input("Digite um número: "))
    
if numero == round(numero):  # Verifica se o número arredondado é igual ao original
    print("O número é inteiro.")
else:
    print("O número é decimal.")