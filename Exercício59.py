"""Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. """

print('-=-' * 10, 'Calculadora Dinâmica', '-=-' * 10)

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
opção = 0
while opção != 5:

    print("""\033[32mEscolha uma das opções abaixo: 

    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa\033[m
    """)
    print('Qual a sua opção? ')
    opção = int(input('Insira aqui a sua opção: '))

    if opção == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))

    elif opção == 2: 
        print('{} x {} = {}'.format(n1, n2, n1 * n2))

    elif opção == 3:
        if n1 > n2:
            print('O número {} é maior!'.format(n1))
        else:
            print('O número {} é maior!'.format(n2))

    elif opção == 4:
        print('Informe os números novamente!')
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))

    elif opção == 5:
        print('Finalizando ...')
    else:
        print('Opção inválida! Tente novamente!')


print('Fim do programa!')





