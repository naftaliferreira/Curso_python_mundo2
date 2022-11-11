""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida"""
# Variaveis
peso = float(input('Qual é o seu peso: (Kg) '))
altura = float(input('Qual é a sua altura: (m) '))
imc = peso / (altura ** 2)
# teste
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

# Condicionais
if imc <= 18.5:
    print('Está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Está com o peso ideal!')
elif imc > 25 and imc <= 30:
    print('Está com sobrepeso!')
elif imc > 30 and imc <= 40:
    print('Alerta! Obesidade!')
else:
    print('Alerta! Obesidade mórbida!')