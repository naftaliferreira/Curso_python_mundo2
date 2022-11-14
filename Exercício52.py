""" Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. """

n = int(input('Digite um número: '))
tot = 0

for c in range(1, n + 1): 
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')

if tot == 2:
    print('O número {} é primo!'.format(n))
else:
    print('\n\033[mO número {} não é primo!'.format(n))

# Números primos apenas são divisíveis por ele mesmo e por 1 
# Porém por via de regra o número 1 não é primo. 

