''' Escreva um programa em Python que leia um número inteiro qualquer e 
peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. '''

# Variables
n = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
\033[1;32m
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL
\033[m
''')
opção = int(input('Sua Opção: '))

# Condictions and converting values
if opção == 1:
    print('O numero {} convertido para binário é {}'.format(n, bin(n)[2:])) # bin(x) conversão para binario, [2:] fatiamento de string
elif opção == 2:
    print('O número {} convertido para octal é {}'.format(n, oct(n)[2:])) # oct(x) conversão para octal, [2:] fatiamento de string
elif opção == 3:
    print('O número {} convertido para hexadecimal é {}'.format(n, hex(n)[2:])) # hex(x) conversão para hexadecimal, [2:] fatiamento de string
else:
    print('Error! Opção incorreta!')


