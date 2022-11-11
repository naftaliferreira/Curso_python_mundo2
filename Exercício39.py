""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. """


# Import libraries
from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

# 1º teste
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

# Condicionais 

if idade == 18:
	print('Você deve se alistar imediatamente!')
elif idade < 18:
	saldo = 18 - idade
	ano = atual + saldo
	print('Ainda faltam {} anos para o alistamento'.format(saldo))
	print('Seu alistamento será em {}.'.format(ano))
elif idade > 18: 
	saldo = idade - 18
	ano = atual - saldo
	print('Você deveria ter se alistado à {} anos'.format(saldo))
	print('Seu alistamento foi em {}.'.format(ano))
