""" Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes """ 

# Variaveis
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Condicionais
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print('Os segmentos acima podem formar um triângulo ', end='')
	if r1 == r2 == 3:
		print('EQUILÁTERO') # Todos os lados iguais.
	elif r1 != r2 != r3 != r1:
		print('ESCALENO') # Todos os lados diferentes.
	else:
		print('ISÓSCELES') # Dois lados iguais e um diferente. 
else: 
	print('Os segmentos acima não podem formar um triângulo!')