"""  Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

# Importação de bibliotecas
from datetime import date

# Data atual 
atual = date.today().year
# Contadores 
maior = 0
menor = 0
# Repetição da pergunta para 7 pessoas
for n in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Das pessoas entrevistadas, {} pessoas eram maiores de idade e {} eram menores de idade!'.format(maior, menor))

