#desenvolva um algorítmo na linguagem python para ler o peso
#de um carro, o peso dos três ocupantes e exibir:
#a soma dos pesos dos passageiros e do carro
#a média de pesos apenas dos ocupantes

peso_carro = float(input("Digite o peso do carro:"))
peso_ocupante1 = float(input("Digite o peso do primeiro ocupante:"))
peso_ocupante2 = float(input("Digite o peso do segundo ocupante:"))
peso_ocupante3 = float(input("Digite o peso do terceiro ocupante:"))          
peso_total = (peso_carro + peso_ocupante1 + peso_ocupante2 + peso_ocupante3)

media = (peso_ocupante1 + peso_ocupante2 + peso_ocupante3) / 3
media = round(media,2)
print(f"A soma de pesos dos passageiros e do carro é {peso_total}")
print(f"A média de peso dos ocupantes é {media}")