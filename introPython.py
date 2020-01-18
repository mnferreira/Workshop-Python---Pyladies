# jogo de adivinhar números:

# numero = 5
# numeroChute = int(input('Chute um número de 1 a 10: '))

# if numero == numeroChute:
#     print('Você acertou')

# elif numero < numeroChute:
#     print('O número é menor do que ' + str(numeroChute))

# else:
#     print('O número é maior do que '+ str(numeroChute))


# Exercício while:
# contador = 1
# preco = 0

# while contador <= 7:
#     nums = float(input('Insira o valor do lanche: '))
#     preco = preco + nums
#     contador = contador + 1

# print(preco)

#Exercício for:
linguagens = ['Java', 'JavaScript', 'PHP', 'C', 'Python']

for linguagem in linguagens:
    if linguagem.startswith('P'):
        print(linguagem)