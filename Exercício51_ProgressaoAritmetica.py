""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. """

n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = n1 + (10 - 1) * razao  # Fórmula Matemática para encontrar o décimo termo de uma PA.  
for c in range(n1, decimo_termo + razao, razao):
    print('{}'.format(c), end=" -> ")
print('FIM!')



