""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO  """

# Variaveis
nota1 = float(input('Qual é a primeira nota? '))
nota2 = float(input('Qual é a segunda nota? '))
media = (nota1 + nota2) / 2

# Condicionais
if media >= 7:
    print('O aluno está aprovado!')
elif media >= 5 and media <=6.9:
    print('O aluno está de recuperação!')
else:
    print('O aluno está reprovado!')

    

