#encontre x' e x'' recebendo os valores do usuário

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

x1 = -b + (b** - 4 * a * c ** (1/2)) / (2*a) #formula de bhaskara completa
x2 = -b - (b** - 4 * a * c ** (1/2)) / (2*a)
x1 = round (x1, 2)
x2 = round (x2, 2)
print(f"O valor de x1 é {x1}")
print(f"O valor de x2 é {x2}")

#utilizando formula de bhaskara separadamente
# delta = b**2 - 4*a*c
# x1 = (-b + delta ** (1/2)) / (2*a)
# x2 = (-b - delta ** (1/2)) / (2*a)