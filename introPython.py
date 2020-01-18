numero = 5
numeroChute = int(input('Chute um número de 1 a 10: '))

if numero == numeroChute:
    print('Você acertou')

elif numero < numeroChute:
    print('O número é menor do que ' + str(numeroChute))

else:
    print('O número é maior do que '+ str(numeroChute))