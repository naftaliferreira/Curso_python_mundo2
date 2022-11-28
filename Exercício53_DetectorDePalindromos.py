""" Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:"""

frase = str(input('Digite uma frase: ')).strip().upper() # Ler a frase, tirar os espaços e converter letras para maiusculo. 
palavras = frase.split()  # Separar a frase por palavras. 
junto = ''.join(palavras)  # juntar todas as palavras sem os espaços entre elas. 
inverso = '' # Variável onde será armazenado a varredura da variável junto. 

for reverse in range(len(junto) - 1, -1, -1): # len() para pegar a última letra, - 1 a última letra de tras pra frente é zero, -1 é retirado de 1 em 1 as letras, -1 contagem regressiva. 
    inverso += junto[reverse]
print(junto, inverso)

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

# Outra forma de resolver o problema e de uma forma bem mais simples, sem o laço for:
new_inverso = junto[::-1] # Variável junto do início ao fim, de tras pra frente. 
print(new_inverso)




