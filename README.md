# Curso Python3 

Olá! Este material foi criado apartir das anotações feitas durante o curso de Python realizadas pelo Curso em Vídeo, do professor Gustavo Guanabara. O Python é uma linguagem moderna utilizada por grandes empresas como Google, Youtube, Globo e muitas outras.
Fácil de aprender, com código limpo e organizado, vem ganhando bastante espaço no mundo inteiro.

### Autor do Curso

- [@gustavoguanabara](https://github.com/gustavoguanabara)

### Para acompanhar os meus trabalhos: 
- [@naftaliferreira ](https://github.com/naftaliferreira)




# Arquivos

Caso queira utilizar este material para auxiliar nos estudos da linguagem, recomendo que  baixe os exercícios resolvidos para ajudar no aprendizado:
[Mundo1 Python3](https://github.com/naftaliferreira/Curso_python_mundo1.git)
[Mundo2 Python3](https://github.com/naftaliferreira/Curso_python_mundo2.git)

## Criação de arquivos e pastas

Para criar novos arquivos ou pastas, basta acessar a barra de navegação da idle escolhida. Você pode criar um novo arquivo clicando no botão **Novo arquivo**  . Da mesma forma pode criar uma nova pasta clicando no botão **N**.

## Trocar para outro arquivo

Todos os seus arquivos e pastas são apresentados como uma árvore no explorador de arquivos. Você pode alternar de um para outro clicando em um arquivo na árvore.

## Renomear arquivos

Você pode renomear o arquivo atual clicando no nome do arquivo na barra de navegação ou clicando no botão **Renomear** no explorador de arquivos.

## Deletar um arquivo

Você pode excluir o arquivo atual clicando no botão **Remover** no explorador de arquivos. O arquivo será movido para a pasta **Lixo** e excluído automaticamente após 7 dias de inatividade.

## Exportar um arquivo

Você pode copiar os arquivos que queira exportar de forma separada, ou copiar toda a pasta para outro dispositivo ou ambiente cloud como **Google Drive**, **Dropbox** ou outros. 

# Mundo 2 - Python
##### Embora tenha mudado o módulo a ordem de aulas e exercícios é mantida ao decorrer dos módutos. 

## Aula 11 - Dicas e Regras
> Informações a cerca de mundanças nas atualizações do Python.
## Aula 12 - Condições Aninhadas
>Estruturas aninhadas tem mais de 2 opções
>
		if, elif and else
		
> Dentro do if pode usar quantos elif forem necessários. 
		
### Exercício 36 - Aprovando Empréstimo
> Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
### Exercício 37 - Conversor de bases
> Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
### Exercício 38 - Comparando números
> Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

> – O primeiro valor é maior

> – O segundo valor é maior

> – Não existe valor maior, os dois são iguais
### Exercício 39 - Alistamento militar
> Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
### Exercício 40 - Aquele clássico da média
> Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

> – Média abaixo de 5.0: REPROVADO

> – Média entre 5.0 e 6.9: RECUPERAÇÃO

> – Média 7.0 ou superior: APROVADO
### Exercício 41 - Classificando Atletas
> A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
> – Até 9 anos: MIRIM
> – Até 14 anos: INFANTIL
> – Até 19 anos: JÚNIOR
> – Até 25 anos: SÊNIOR
> – Acima de 25 anos: MASTER
### Exercício 42 - Analisando Triângulos v2.0
> Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
> – EQUILÁTERO: todos os lados iguais
> – ISÓSCELES: dois lados iguais, um diferente
> – ESCALENO: todos os lados diferentes
### Exercícios 43 - Índice de massa corporal (IMC)
> Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
### Exercício 44 - Gerenciador de pagamentos 
> Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
### Exercício 45 - Game - Jo-Ken_po
> Crie um programa que faça o computador jogar Jokenpô com você.
## Aula 13 - Estrutura de repetição for
	
>exemplo1:

		laço c no intervalo(1,10)
			passo 
		pega
		
>  c é a variável, pode colocar o nome que quiser na variável, porém é recomendado colocar nomes que façam sentido com o trabalho que está sendo executado. 
> No exemplo acima, significa, andar 10 passos, para e pega um objeto no décimo passo. 
	
####  Como escrever o laço no python?
		for c in range(1, 10):
			passo
		pega
	
> exemplo2
> Em algorítimo:
 
		for c no intervalo(0,3)
			passo
			pula
		passo
		pega

> Escrito no Python:
> 
		for in range(0, 3):
			passo
			pula
		passo 
		pega
		
> exemplo3
>  Em algorítmo:
		
		for c no intervalo(0,3)
			se have_coin
				pega
			passo
			pula
		passo
		pega
> Escrito no Python:
> 
		for c in range(0, 3):
			if have_coin:
				pega
			passo
			pula
		passo
		pega

##### Exercícios práticos
	
	for c in range(0, 6):
		print('Oi')
	print('FIM')

> O python conta de 0 até número -1, e para. O último número não é contado, para fazer com que seja contado deve ser adicionado numero+1 ou um número a mais. 

	for c in range(1, 7):
		print(c)
	print('Fim')
> Contador de 1 até 6. 
	
>  Para criar um contador regressivo:

		for c in range(6, 0, -1):
			print(c)
		print('FIM')
	
> Criando um contador com saltos:
> 
		for c in range(0, 7, 2):
			print(c)
		print('FIM')
	
> Escolhendo até que número contar: 

		n = int(input('Digite um número: '))
		for c in range(0, n + 1):
			print(c)
		print('PRINT')
	
> Numero inicial, final e salto:
	
		i = int(input('Digite um número inicial: '))
		f = int(input('Digite um número final: '))
		s = int(input('Digite um número para o salto: '))
		
		for c in range(i, f +1, s):
			print(c)
		print('FIM')
	
> Repetir perguntas :
		
		for c in range(0, 3):
			n = int(input('Digite um valor: ')
		print('FIM')
		
> Somatorio
		
		s = 0
		fo c in range(0, 3):
			n = int(input('Digite um valor: ')
			s += n
		print('O somatório de todos os valores é {}.'.format(s))
		
### Exercício46 - Contagem Regressiva
> Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
### Exercício47 - Contagem de pares
>Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. 
### Exercício48 - Soma ímpares múltiplos de três
> Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
### Exercício49 - Tabuada v2.0
> Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
### Exercício50 - Soma dos pares
> Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
### Exercício51 - Progressão arítmética
> Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.	
### Exercício52 - Números primos
> Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
### Exercício53 - Detector de palindromo
> Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
### Exercício54 - Grupo da maioridade
> Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.	
### Exercício55 - Maior e menor da sequencial
> Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
### Exercício56 - Analisador completo
> Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.	
## Aula14 - Estrutura de repetição while

#### Estrutura de repetição com teste lógico. O laço while ao contrário do for, não é colocado inicio e fim, ele é usado quando não se sabe qual será o limite. 
>Os problemas que foram resolvidos com for, tambem podem ser resolvidos com while, porém quando se sabe qual é o limite, fica mais prático usar o laço for. 

> exemplo1 - simples:
	
	enquanto não chegar_no_fim                      while not final_line
		anda                                              walk
	para											stop
	
Tanto o while quanto o for não tem diferença de velocidade de execução, portanto qualquer uma das estruturas pode ser usado normalmente. 

> exemplo2 - aninhadas:
	
	enquanto não situação 1                          while no situation1:
		se situação 2                                	if situation2:
			ação 2	                                 		action2
		se situação 3                                   if situation3:
			ação 3                                          action3
		se situação 4                                   if situation4:
			ação 4                                         	action4
	ação 1                                           action1
	
	
>Exemplo3:
	
	Contar de 1 a 10 com laço for
	for c in range(1, 11):
		print(c)
	print('FIM')

	c = 1
	while c < 11:
		print(c)
		c += 1
	print('Fim')
	
##### O laço for e while podem ser usados em todos os problemas onde se sabe qual é o limite, porem, caso não saiba o limite apenas o while pode ser usado. 

>Exemplo4:
> ##### No laço for é necessário indicar o início e o fim da operação
	for c in range(1, 5):   
		n = int(input('Digite um valor: '))
	print('FIM')
> ##### Com o laço while, ele não vai parar até a condição for False. 
	n = 1
	while n != 0:          
		n = int(input('Digite um valor: '))
	print('FIM')
	
>Exemplo5: 
	
	r = 'S'
	while r == 'S':
		n = int(input('Digite um valor: ))
		r = str(input('Quer continuar? [S/N] ')).upper()
	print('FIM')
	
##### Com o exemplo acima é possível acrescentar valores de forma indefinidamente até a condição de parada for acionada. 
		
> Exemplo6:
	
	n = 1
	while n != 0:
	par = impar = 0
		n = int(input('Digite um valor: '))
		if n != 0:
			if n % 2 == 0:
				par += 1
			else:
				impar += 1
	print('Você digitou {} números pares e {} números impares'.format(par, impar))
	
### Exercício57 - Validação de dados
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
### Exercício58 - Jogo da adivinhação v2.0
Melhore o Exercício28 onde o computador vai 'pensar' em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.  
### Exercício59 - Criando um menu de opções
>Crie um programa que leia dois valores e mostre um menu na tela: 
	[1] Somar
	[2] Multiplicar
	[3] maior
	[4] novos números 
	[5] sair do programa
	
>Seu programa deverá realizar a operação solicitada em cada caso. 

> ##### Apartir do Exercício60 todos os exercícios passaram a ser realizados utilizando o Jupyter, pois possui formato de caderno e mais prático para manter anotações e testar cada linha de código de forma idependente. 
> ##### O Formato é ipynb
### Exercício60 - Calculo do fatorial
>Faça um programa que leia um número qualquer e mostre o seu fatorial, se possível colocar duas opções para o usuário escolher 1 ou 2 e fazer com for e while. 
### Exercício61 - Progressão Aritmética v2.0
>Refaça o exercício51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutrura while.
### Exercício62 - Super progressão Aritmética v3.0
> Melhore o Exercício61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos. 
### Exercício63 - Sequencia de fibonacci v1.0
>Escreva um programa que leia um número n interiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.  
### Exercício64 - Tratando vários valores v1.0
>Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição da parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag (999))  
### Exercício65 - Maior e menor valores 
>Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.  

## Aula15 - Interrompendo repetições while
	
> Relembrando estrutura enquanto (while):
	
	enquanto não pegar_maçã
		se tem_chão
			anda
		se tiver_buraco
			pula
		se tiver_moeda
			pega
	
	pega_maçã
	
>  Adicionando o comando break
	
	enquanto verdadeiro
		se tem_chão
			anda
		se tem_buraco
			pula
		se tem_moeda
			pega
		se tiver_trofeu
			pula
			interrompa
	
	pega
	
> Escrevendo em Python o exemplo anterior
	
	while True:
		if have_down
			walk
		if  have_hole
			jump
		if have_coin
			get
		if have_trofeu
			jump
			break
	
	get
	
	
##### Sem o break o comando roda para sempre pois, enquanto for verdadeiro e não tiver mais nenhuma outra condição, o programa não para. 
		
	
> Exemplo1:
	
	cont = 1
	while cont < 10:
		print(cont, '->', end='')
		cont += 1
	print('Acabou')
	
>> Neste exemplo acima, é mostrado numeros de 1 a 10 como solicitado. 
>> Porém se não colocar um objetivo para encerrar o laço, ele irá rodar para sempre: 
	
>Exemplo2:
	
	cont = 1
	while True:
		print(cont, '->', end='')
		cont += 1
	print('Acabou!')

>> Se for utilizado a estrura True, o comando roda para sempre, para parar tem duas opções : ou força a parada do idle ou usa o comando break. 
	
>> O comando break serve também para evitar algumas 'gambiarras' dentro da programação, por exemplo:
	
>Exemplo3:
	
	n = s = 0
	
	while n  != 999
		n = int(input('Digite um número: '))
		s += n
	print(s)
	
>> Com o exemplo acima, quando for exibir a soma irá somar o 999 que é a 'flag', a forma preguiçosa de resolver é inserindo outra linha e colocar s -= 999, e retirar o 999 manualmente.

>Recriando o problema acima adicionando o break:
		
	
	n = s = 0
	
	while True:
		n = int(input('Digite um número: '))
		if n == 999:
			break
		s += n
	
	print(s)
	
>> Com o exemplo acima o 999 ele não soma. 
	
	

### Mudando de assunto: 

	nova forma de formatar string do python
	
	forma utilizada até o momento:
	
	print('A soma é {}'.format(s))
	
	format nova:
	
	print(f'a soma é{s}')
	
	nome = 'Pedro'
	idade = '6'
	salario = 987.3
	print(f'O {nome} tem {idade} anos e ganha R$ {salario:.2f}.')
	
### Exercício66 - Vários números com flag
> Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


### Exercício67 - Tabuada v3.0
> Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

### Exercício68 - Jogo do Par ou Ímpar
> Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

### Exercício69 - Análise de dados do grupo
> Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
### Exercício70 - Estatísticas em produtos 
> Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
### Exercício71 - Simulador de Caixa eletrônico