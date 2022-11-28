''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. '''

# Variables
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
limite = salario * (30 / 100) # calculo de 30% do salário do comprador
'''
# 1º teste do programa
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))
# 2º teste comparação limite x prestação
print('Comparando prestação = {:.2f}, valor limite = {:.2f}'.format(prestação, limite))
'''
# Condicional, a prestação não pode exceder 30% da renda, caso contrário o empréstimo é negado. 
if prestação <= limite:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação é de R${:.2f}'.format(casa, anos, prestação))
    print('\033[1;32mEmprestimo pode ser concedido!\033[m')
else:
    print('\033[1;31mEmprestimo negado!\033[m')

