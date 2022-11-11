"""  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER """ 

# Variaveis
idade = int(input('Quantos anos o atleta tem? '))

# Condicionais
if idade > 25:
    print('O atleta está na modalidade Master')
elif idade > 19 and idade <= 25:
    print('O atleta está na modalidade SÊNIOR')
elif idade > 14 and idade <= 19:
    print('O atleta está na modalidade JÚNIOR')
elif idade > 9 and idade <= 14:
    print('O atleta está na modalidade INFANTIL')
elif idade < 9:
    print('O atleta está na modalidade MIRIM')

