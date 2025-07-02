# Exercicios de coleções


# Questões de Tuplas
# <------------------- QUESTÂO 1 ---------------->

"""
1. Escreva um programa que receba uma tupla de números inteiros e como
saída uma nova tupla com os elementos pares da tupla original. Por
exemplo, se a tupla for (1, 2, 3, 4, 5), o programa deve imprimir (2, 4).
"""

tupla = (1,2,3,4,5)

tupla_pares = ()

for i in range(len(tupla)):
    item_atual = tupla[i]

    if(item_atual % 2 == 0):

        tupla_pares += (item_atual,)


print(tupla_pares)


# <------------------- QUESTÂO 2 ---------------->

"""
2. Escreva um programa que receba uma tupla de strings e exiba uma nova
tupla com as strings ordenadas alfabeticamente e sem repetições. Por
exemplo, se a tupla for ("banana", "maçã", "laranja", "banana", "uva"), o
programa deve imprimir ("banana", "laranja", "maçã", "uva").
"""

tupla = ("banana", "maçã", "laranja", "banana", "uva")

conjunto_frutas = list(set(tupla))

conjunto_frutas.sort()

print(conjunto_frutas)




# Questões de dicionarios
# <------------------- QUESTÂO 3 ---------------->

"""
3. Escreva um programa que receba um dicionário que mapeia nomes de
países para suas populações e exiba o nome do país com a maior
população. Por exemplo, se o dicionário for {"Brasil": 211.8, "China":
1400.5, "Índia": 1366.4}, o programa deve exibir "China".
"""

paises = {"Brasil": 211.8, "China":1400.5, "Índia": 1366.4}

populacoes = [value for key,value in paises.items()]

maior_populacao = 0

for i in range(len(populacoes) - 1):
    maior_populacao = populacoes[i]
    if(maior_populacao < populacoes[i + 1]):
        maior_populacao = populacoes[i + 1]
        

pais_maior_populacao = ''

for chave, valor in paises.items():
    if(maior_populacao == valor):
        pais_maior_populacao = chave


print(pais_maior_populacao)


# <------------------- QUESTÂO 4 ---------------->

"""
4. Escreva um programa que receba como entrada um dicionário que mapeia
nomes de alunos para suas notas e exiba um novo dicionário com os nomes
dos alunos aprovados e suas respectivas médias. Considere que um aluno é
aprovado se sua média for maior ou igual a 7. Por exemplo, se o dicionário
for {"Ana": [8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 4.0], "Carla": [7.0, 8.0, 9.0]},
o programa deve exibir {"Ana": 8.33, "Carla": 8.0}.
"""

alunos = {"Ana": [8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 4.0], "Carla": [7.0, 8.0, 9.0]}

alunos_aprovados = {}

somatorio = []

incremento = 0

soma = 0

for x, y in alunos.items():
    valor_atual = y
    for i in range(len(valor_atual)):
        soma += valor_atual[i]
    somatorio += [soma / (i + 1)]
    soma = 0

for item in alunos:
    if(somatorio[incremento] >= 7):
        alunos_aprovados[item] = somatorio[incremento]
    incremento += 1
    
print(alunos_aprovados)



# Questões de Conjuntos
# <------------------- QUESTÂO 5 ---------------->

"""
5. Escreva um programa que receba dois conjuntos de números inteiros como
entrada e exiba um novo conjunto com os elementos que estão em ambos
os conjuntos. Por exemplo, se os conjuntos forem {1, 2, 3, 4} e {3, 4, 5, 6},
o programa deve exibir {3, 4}.
"""

primeiro_conjunto = {1, 2, 3, 4}

segundo_conjunto = {3, 4, 5, 6}

lista_primeiro_conjunto = list(primeiro_conjunto)

lista_segundo_conjunto = list(segundo_conjunto)

subconjunto = set({})

for x in lista_primeiro_conjunto:
    if ((x in lista_primeiro_conjunto) and (x in lista_segundo_conjunto)):
        subconjunto.add(x)


print(subconjunto)





# <------------------- QUESTÂO 6 ---------------->

"""
6. Escreva um programa que receba um conjunto de strings e exiba um novo
conjunto com as strings que são palíndromos. Um palíndromo é uma palavra
que é igual a ela mesma quando lida de trás para frente. Por exemplo, se o
conjunto for {"arara", "casa", "ovo", "radar"}, o programa deve exibir
{"arara", "ovo", "radar"}.
"""

palavras = {"arara", "casa", "ovo", "radar"}

lista_palavras = list(palavras)

palindromos = set({})


for palavra in lista_palavras:
    palindromo = palavra[-1::-1]
    if(palindromo == palavra):
        palindromos.add(palindromo)

print(palindromos)

