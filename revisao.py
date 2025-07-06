# Revisão de Array/listas

# QUestões de listas/arrays

#<--------------- QUESTÃO 1 --------------->

"""
Exercício 1: Soma dos Pares (Fácil)

Crie um programa Python que receba uma lista de números inteiros. O programa deve calcular 
e imprimir a soma de todos os números pares presentes na lista.

Exemplo:

Se a lista for [1, 2, 3, 4, 5, 6], a saída deve ser 12 (2 + 4 + 6).
"""

# inteiros = [int(input('Informe um número inteiro: ')) for i in range(6)]

# resultado_pares = 0

# for numero in inteiros:
#     if numero % 2 == 1:
#         resultado_pares += numero

# print(resultado_pares)

# -------------------------------------------

#<--------------- QUESTÃO 2 --------------->

"""
Exercício 2: Inverter Lista Sem Usar Funções Built-in (Médio)

Desenvolva um programa Python que receba uma lista de elementos 
(pode ser de qualquer tipo). O programa deve criar e 
retornar uma nova lista contendo os elementos da lista original na ordem inversa. 
Você não pode usar funções built-in como reverse(), reversed() ou fatiamento [::-1].

Exemplo:

Se a lista for ['a', 'b', 'c', 'd'], a saída deve ser ['d', 'c', 'b', 'a'].
"""

# lista_inteiros = [1,2,3,4,5,6]

# lista_reversa = lista_inteiros[-1::-1]

# print(lista_reversa)



lista = [1,2,3]

# Matizes

# matriz = []

# for i in range(3):
#     outro_array = []
#     for j in range(3):
#        outro_array.append(j)

#     matriz.append(outro_array)



# print(matriz[0][1])

"""
Exercício: Soma das Diagonais de uma Matriz

Crie um programa em Python que receba uma matriz quadrada 
(ou seja, o número de linhas é igual ao número de colunas) de números inteiros. 
O programa deve calcular e imprimir a soma dos elementos da diagonal principal e a 
soma dos elementos da diagonal secundária.

Detalhes do Exercício:

    Entrada:

        Sua função deve receber uma lista de listas que representa a matriz.

    Saída:

        O programa deve imprimir duas linhas:

            "Soma da diagonal principal: [valor da soma]"

            "Soma da diagonal secundária: [valor da soma]"

Exemplo:

Para a seguinte matriz:

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

A saída esperada seria:

Soma da diagonal principal: 15
Soma da diagonal secundária: 15
"""

# quadrado = [
#     [1,2,3],
#     [5,6,7],
#     [9,0,1]
# ]

# diagonal_principal = quadrado[0][0] + quadrado[1][1] + quadrado[2][2]
# diagonal_secundaria = quadrado[0][2] + quadrado[1][1] + quadrado[2][0]

# print(diagonal_principal)
# print(diagonal_secundaria)


"""
10. Escreva um programa que leia 9 valores inteiros e armazene em uma matriz 3x3. O

programa deve informar quantos valores ímpares foram digitados pelo usuário e impri-
mir a matriz no formato 3x3. Dica: use o operador “%” para verificar se o número é

ímpar. “,”. Exemplo:
"""

# contador = 0
# inteiros = []

# for i in range(1,10,1):
#     novo_numero = int(input('Informe um novo número: '))
#     inteiros += [novo_numero]
#     if novo_numero % 2 == 1:
#         contador+= 1


# matriz = [inteiros[i:i+3] for i in range(0,9,3)]


# print(matriz)
# print(f'A quantidade de impares é: {contador}')


"""
11. Escreva um programa que solicite ao usuário o valor das duas dimensões de uma
matriz. Em seguida, solicite ao usuário e armazene nessa matriz uma quantidade de

valores inteiros correspondente ao tamanho necessário para preencher todas as posi-
ções da matriz. O programa deverá exibir a matriz de dimensões “m por n” informar o

resultado da soma de cada LINHA da matriz. Exemplos:

"""

numero_linhas = int(input('Informe a quantidade de linhas: '))
numero_colunas = int(input('Informe a quantidade de colunas: '))

print('_____________________________________________________')

matriz = []

for i in range(numero_linhas):
    linha = []
    for j in range(numero_colunas):
        inteiro = int(input('Informe um valor: '))
        linha.append(inteiro)

    matriz.append(linha)

print('_____________________________________________________')

print(matriz)

for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[i])):
        soma += matriz[i][j]
    
    print(f'A soma dos elementos da linha {i} é igual a: {soma}')

    


# ------------------------

# Revisão Dicionarios

"""
11. Escreva um programa que receba como entrada uma string várias palavras separadas
por espaço. O programa deverá verificar e apresentar a quantidade de ocorrência de
cada palavra no texto repassado como entrada para o programa, sem fazer distinção
entre letras maiúsculas ou minúsculas. Os sinais de pontuação não devem ser
contabilizados, como por exemplo “.” Ou “,”. Crie um dicionário que armazene a
contagem de cada palavra no texto. A chave do dicionário deve ser a palavra e o valor
deve ser o número de vezes que a palavra aparece no texto. Imprima o dicionário
resultante. Exemplos:
Entrada 1:
Lorem ipsum
dolor sit amet.
Lorem opsum
dolor amet, dolor
comem.

Saída 1:
Contagem de
palavras:
{‘Lorem’:2, ‘ipsum’:1,
‘dolor’:3, ‘sit’:1,
‘amet’:2, ‘opsum’:1,
‘comem’:1}

Entrada 2:
Lorem ipsum
ipsum lorem sit
amet. Lorem
corpus dolor
amet, dolor
comem CorpuS.

Saída 2:
Contagem de
palavras:
{‘lorem’:3, ‘ipsum’:2,
‘dolor’:2, ‘sit’:1,
‘amet’:1, ‘corpus’:2,
‘dolor’:2, ‘comem’:1}
"""

# texto = input('Informe um texto ou um conjunto de palavras separados por um espaço: ')

# while(not(len(texto) > 0)):
#     texto = input('Informe um texto ou um conjunto de palavras separados por um espaço: ')


# palavras = []

# palavra_completa = ''

# final = 1

# final_texto = len(texto)

# aparicoes_palavras = {}

# for caractere in texto:
#     if(not(caractere == ',' or caractere == '.' or caractere == ' ')):
#         palavra_completa += caractere
    
#     if(caractere == ' ' or final == final_texto):
#         palavras += [palavra_completa]
#         palavra_completa = ''

#     final += 1


# for palavra in palavras:
#     counter = 0
#     for i in range(len(palavras)):
#         if(palavra.lower() == palavras[i].lower()):
#             counter += 1

#     aparicoes_palavras[palavra.lower()] = counter

# print(aparicoes_palavras)




