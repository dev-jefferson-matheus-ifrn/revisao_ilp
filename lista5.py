#-------------- QUESTÃO 1 --------------
'''
1. Criação e acesso: Escreva um programa que crie uma tupla que seja criada contendo
os dados nome, idade e estado. Como saída, o programa deve imprimir cada um
desses valores separadamente.
'''
print("Questão 1: Criação e acesso.\n")
tupla = ('Ana', 20, 'RN')
print("Nome:", tupla[0], "\nIdade:", tupla[1], "\nEstado:", tupla[2])
tupla = ('José', 15, 'CE')
print("Nome:", tupla[0], "\nIdade:", tupla[1], "\nEstado:", tupla[2])

#---------------------------------------


#-------------- QUESTÃO 2 --------------
'''
2. Desempacotamento: Escreva um programa que realiza o cálculo da distância entre
dois pontos no plano cartesiano. O programa deve receber como entrada 4 valores
inteiros para os dois pontos. Em seguida, calcular a distância entre os dois pontos e
exibir o valor da distância ao usuário.
'''
print("\nQuestão 2: Desempacotamento.\n")
pontos = []
for i in range(2):
    x = int(input(f'Digite o valor da coordenada x do ponto {i+1}: '))
    y = int(input(f'Digite o valor da coordenada y do ponto {i+1}: '))
    pontos += [(x, y)]

distancia = ((pontos[1][0] - pontos[0][0])**2 + (pontos[1][1] - pontos[0][1])**2)**.5
print(f'Distância: {distancia:.2f}')

#---------------------------------------


#-------------- QUESTÃO 3 --------------
'''
3. Concatenação de tuplas: Escreva um programa que cria duas tuplas: uma para frutas
e outra para vegetais. O programa deve imprimir no terminal o resultado de uma única
tupla formada pela concatenação das duas tuplas anteriormente fornecidas pelo
usuário.
'''
print("\nQuestão 3: Concatenação de tuplas.\n")
frutas = input('Insire uma sequência de frutas (ex: manga, ciriguela e pitanga): ')
frutas = frutas.split(',')
vegetais = input('Insira uma sequência de vegetais (ex: beterraba, cebola): ')
vegetais = vegetais.split(',')

lista_aux = []
for item in frutas:
    lista_aux += item.strip().split(' e ')
frutas = tuple(lista_aux)

lista_aux = []
for item in vegetais:
    lista_aux += item.strip().split(' e ')
vegetais = tuple(lista_aux)

print(frutas + vegetais, '\n')

##se for fazer sem a interação com o usuário:
frutas = ('manga', 'ciriguela', 'pitanga', 'acerola')
vegetais = ('beterraba', 'cebola', 'alho', 'batata')
print(frutas + vegetais)

#---------------------------------------


#-------------- QUESTÃO 4 --------------

#---------------------------------------


#-------------- QUESTÃO 5 --------------
'''
5. Troca de posições em tuplas: Escreva um programa que, dada uma tupla e dois valores
inteiros correspondentes às posições nessa tupla, troque os elementos conforme as
posições fornecidas. Lembre-se de que tuplas são imutáveis, portanto, você precisará
converter a tupla para uma lista, fazer a troca e depois converter de volta para uma
tupla. Imprima o resultado da tupla inicial e com as posições permutadas.
'''
print("\nQuestão 5: Troca de posições em tuplas.\n")
#sem a interação do usuário:
tupla = (1, 2, 3, 4, 5)
print('Tupla A:', tupla)
p1 = 2
p2 = 4
lista = list(tupla)
lista[p1], lista[p2] = lista[p2], lista[p1]
tupla = tuple(lista)
print('Tupla B:', tupla)

#com a interação do usuário:
lista = input('\ninsira uma sequencia de valores inteiros separados por vírgula: ').split(',')
p1 = int(input('insira a posição 1: '))
p2 = int(input('insira a posição 2: '))

lista = [int(item) for item in lista]
tupla = tuple(lista)
print('Tupla A:', tupla)
lista[p1], lista[p2] = lista[p2], lista[p1]
tupla = tuple(lista)
print('Tupla B:', tupla)

#---------------------------------------


#-------------- QUESTÃO 6 --------------

#---------------------------------------


#-------------- QUESTÃO 7 --------------
'''
7. União e diferença: Escreva um programa que solicite ao usuário 3 conjuntos (A, B e
C) de números inteiros e em seguida realize as seguintes operações sobre conjuntos:
união: (A U B); e diferença: (A U B) - C. O programa deverá exibir como saída o
resultado da união e diferença entre os conjuntos (use as funções embutidas union()
e difference()).
'''
print("\nQuestão 7: União e diferença.\n")

conj_A = input('Digite uma sequência de números inteiros, separados por vírgula, para o conjunto A (Ex: 1, 2, 3): ').split(',')
conj_A = [int(item) for item in conj_A]
conj_A = set(conj_A)
conj_B = input('Digite uma sequência de números inteiros, separados por vírgula, para o conjunto B (Ex: 1, 2, 3): ').split(',')
conj_B = [int(item) for item in conj_B]
conj_B = set(conj_B)
conj_C = input('Digite uma sequência de números inteiros, separados por vírgula, para o conjunto C (Ex: 1, 2, 3): ').split(',')
conj_C = [int(item) for item in conj_C]
conj_C = set(conj_C)

print("União: ", conj_A.union(conj_B))
print("Diferença: ", conj_A.union(conj_B).difference(conj_C))

#---------------------------------------


#-------------- QUESTÃO 8 --------------

#---------------------------------------


#-------------- QUESTÃO 9 --------------
'''
9. Operações em Conjuntos: Escreva um programa que, dados dois conjuntos A e B de
valores fornecidos pelo usuário, verifique se B é um subconjunto de A. Em seguida crie
um conjunto C com valores do conjunto A, mas sem os valores do conjunto B. Ao final,
exiba os valores de ambos os conjuntos.
'''
print("\nQuestão 9: Operações em Conjuntos.\n")

conj_A = {1, 'a', 8, '4'}
conj_B = {8, '4'}

if conj_B.issubset(conj_A):
    print('B é um subconjunto de A')
else:
    print('B não é um subconjunto de A')

conj_C = conj_A.difference(conj_B)
print('Conjunto A:', conj_A)
print('Conjunto B:', conj_B)
print('Conjunto C:', conj_C)

#---------------------------------------


#-------------- QUESTÃO 10 --------------

#----------------------------------------


#-------------- QUESTÃO 11 --------------
'''
11. Escreva um programa que receba como entrada uma string várias palavras separadas
por espaço. O programa deverá verificar e apresentar a quantidade de ocorrência de
cada palavra no texto repassado como entrada para o programa, sem fazer distinção
entre letras maiúsculas ou minúsculas. Os sinais de pontuação não devem ser
contabilizados, como por exemplo “.” Ou “,”. Crie um dicionário que armazene a
contagem de cada palavra no texto. A chave do dicionário deve ser a palavra e o valor
deve ser o número de vezes que a palavra aparece no texto. Imprima o dicionário
resultante.
'''
print("\nQuestão 11: Contagem de palavras.\n")

string_inicial = input("Digite o texto que quer verificar: ").lower()
qtd_palavras = {}

val = ''
for char in string_inicial:
    if char == ' ':
        qtd_palavras[val] = 1 if val not in qtd_palavras else qtd_palavras[val] + 1
        val = ''
    elif (char not in ['.', ',', '!', '?', '-', ';', ':', '/', '(', ')']): #sei lá quantos símbolos colocar kk
        val += char

if val:
    qtd_palavras[val] = 1 if val not in qtd_palavras else qtd_palavras[val] + 1

print('Contagem de palavras: ', qtd_palavras)

#----------------------------------------


#-------------- QUESTÃO 12 --------------

#----------------------------------------


#-------------- QUESTÃO 13 --------------
'''
13. Escreva um programa que dado um dicionário aluno_nota, onde as chaves
representam nomes de alunos e os valores representam suas respectivas notas, cujos
valores sejam fornecidos pelo usuário. Crie um novo dicionário que inverta as chaves
e os valores do dicionário aluno_nota, ou seja, as notas serão as chaves e os nomes
dos alunos serão os valores. Considere que duas ou mais pessoas podem ter a mesma
nota, e neste caso, o valor deve ser uma lista com os nomes dos alunos. Imprima o
dicionário resultante.
'''
print("\nQuestão 13: Inversão de dicionários.\n")
qtd_alunos = int(input('Digite a quantidade de alunos que deseja inserir: '))
aluno_nota = {}
for i in range(qtd_alunos):
    nome = input(f'\nDigite o nome do aluno {i+1}: ')
    nota = int(input(f'Digite a nota de {nome}: '))
    aluno_nota[nome] = nota

nota_aluno = {}
for nome, nota in aluno_nota.items():
    if nota not in nota_aluno:
        nota_aluno[nota] = nome
    else:
        nota_aluno[nota] = nota_aluno[nota] + [nome] if type(nota_aluno[nota]) == list else [nota_aluno[nota], nome]

print('aluno_nota: ', aluno_nota)
print('nota_aluno: ', nota_aluno)

#----------------------------------------


#-------------- QUESTÃO 14 --------------
'''
14. Escreva um programa que dado dois dicionários que representam valores de estoque
de itens em duas lojas, cujos valores sejam fornecidos pelo usuário. Crie um novo
dicionário para representar o estoque total que combine esses dois primeiros
dicionários, somando as quantidades dos itens que aparecem em ambas as lojas. Para
itens que aparecem apenas em uma loja, mantenha a quantidade original. Imprima o
dicionário de cada loja e o dicionário resultante.
'''
print("\nEstoque em duas lojas.\n")
lojas = {
    'Loja 1': {}, 
    'Loja 2': {}
    }
estoque_total = {}

for loja, itens in lojas.items():
    item = ''
    while True:
        item = input(f"\nDigite o nome do item (produto) que deseja inserir na {loja}, ou 0 para parar: ")
        if item == '0': 
            print('-' * 50)
            break
        estoque = int(input(f"Digite a quantidade de intens do produto {item}: "))
        itens[item] = estoque
    
    for prod, qtd in itens.items():
        estoque_total[prod] = (estoque_total[prod] + qtd) if estoque_total.get(prod, False) else qtd
    
print('Loja 1: ', lojas['Loja 1'])
print('Loja 2: ', lojas['Loja 2'])
print('Estoque: ', estoque_total)

#----------------------------------------


#-------------- QUESTÃO 15 --------------
'''
15. Escreva um programa que realiza o cálculo das vendas de uma lista de vendedores
ao longo de um trimestre. O programa deve solicitar a relação de nomes dos
vendedores e em seguida criar um dicionário em que o nome do vendedor é a chave
e o valor deve ser o total das vendas desse vendedor. Faça com que o programa
solicite para cada vendedor o quantitativo de vendas ao longo de cada mês no
trimestre. Em seguida, calcule a soma das vendas de cada vendedor e crie uma lista
de tuplas contendo o nome o valor total das vendas de cada vendedor ordenada pelo

valor das vendas em ordem decrescente. Exiba ao final o dicionário do relatório de
vendas e a lista ordenada de tuplas.
'''
print("\nQuestão 15: Vendas de vendedores.\n")
qtd_vendedores = int(input('Digite a quantidade de vendedores que deseja inserir: '))
vendas = {}
vendas_copy = {} #aqui só pra poder modificar sem alterar o original

for i in range(qtd_vendedores):
    nome = input(f'\nDigite o nome do vendedor {i+1}: ')
    vendas[nome] = 0
    vendas_copy[nome] = 0
    for mes in range(1, 4):
        qtd = int(input(f'Digite a quantidade de vendas do vendedor {nome} no mês {mes}: '))
        vendas[nome] += qtd
        vendas_copy[nome] += qtd

#lista só com os totais de vendas
lista_vendas = list(vendas.values())
lista_vendas.sort()
lista_vendas.reverse()

for i in range(len(lista_vendas)):
    for nome, qtd in vendas_copy.items():
        if lista_vendas[i] == qtd:
            lista_vendas[i] = (nome, qtd)
            del vendas_copy[nome]
            break


print("Relatório de vendas: ", vendas)
print("Lista ordenada de tuplas: ", lista_vendas)

#----------------------------------------