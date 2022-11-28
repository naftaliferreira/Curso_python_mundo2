''' Crie um programa que faça o computador jogar Jokenpô com você. '''

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opçoes:
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = int(input('Qual é a sua jogada? '))
print('-=-' * 15)
print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('-=-' * 15)

if computador == 0:
    if jogador == 0:
        print('Houve empate!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Jogada inválida!')

elif computador == 1:
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('Houve empate!')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('Houve empate!')
    else:
        print('Jogada inválida!')

