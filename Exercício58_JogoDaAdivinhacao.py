""" Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. """

from random import randint

pc = randint(0, 10)
erros = 0

print('Sou seu computador ... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    
    if jogador == pc:
        acertou = True
    else:
        erros += 1

print('Acertou!')
print('Antes de acertar, você errou {} vezes.'.format(erros))



