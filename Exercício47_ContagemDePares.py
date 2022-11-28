""" Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. """

# Primeira forma de fazer:
for c in range(1, 51):
    if c % 2 == 0:
        print('.', end='')
        print(c, end=' ')
print('Fim')

# Segunda forma de fazer:
for c in range(2, 51, 2):
    print('.', end='')
    print(c, end=' ')
print('FIM')
