'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. '''

# Variáveis de contadores
somaidade = 0
media_idade = 0
maior_idade_homem = 0
nomevelho = ''
totmulher20 = 0

# Variáveis com laço

for n in range(1, 5):
    print('----- {}ª pessoa -----'.format(n))
    nome = str(input('Digite o nome: ')).strip() 
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: ')).strip()
    somaidade += idade   # 
    if n == 1 and sexo in 'Mm': # se o dado de idade retornar >1 e o sexo for masculino
        maior_idade_homem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
       maior_idade_homem = idade
       nomevelho = nome 
    if sexo in 'Ff' and idade < 20: # Se o sexo feminino estiver em sexo e a idade for menor que 20
        totmulher20 += 1
media_idade = somaidade / 4  # Calculando a média das 4 idades apresentadas. 
# Exindo os resultados
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nomevelho))
print('No grupo tem {} mulheres com menos de 20 anos de idade'.format(totmulher20))

    

