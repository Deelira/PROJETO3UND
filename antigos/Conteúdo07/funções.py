# funções: blocos de instruções que podem ser chamadas repetidamente
# ajuda a deixar o código compacto
# melhora o recuo de código
# tres tipos de funções:
# não tem parametro de entrada e que não tem retorno
# tem parametro de entrada e tem retorno
# não tem parametro de entrada e tem retorno
# tem paramentro de entrada e tem retorno

def saudar_usuario(nome, idade):
    ano = 2025 - idade 
    print(f'\nOla {nome}, seja bem-vindo. Você tem apenas {idade} anos')
    print(f'Você nasceu em {ano}')

'''
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
saudar_usuario(nome, idade)
'''

def testar():
    num1 = 22
    num2 = num1 / 3



def mostrar_resultado(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return round(media, 2)


minha_media = mostrar_resultado(8.1, 4, 7.9)
print(minha_media)