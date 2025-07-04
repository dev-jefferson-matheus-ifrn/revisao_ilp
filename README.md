# execicos

# revisao_ilp

revisão ilp

### Estrutura de Dados

No Python, podemos utilizar diversos tipos de estruturas de dados. Estas estruturas resolvem um tipo de problema e podem ser úteis em diversas situações. As principais estruturas são as Listas, Sets, Dicionários e Tuplas e neste artigo veremos as diferenças e principais características de cada uma.

#### Listas

Uma lista é a estrutura de dados mais básica do Python e armazena os dados em sequência, onde cada elemento possui sua posição na lista, denominada de índice. O primeiro elemento é sempre o índice zero e a cada elemento inserido na lista esse valor é incrementado.

No Python, uma lista pode armazenar qualquer tipo de dado primitivo (string, inteiro, float, etc).

##### Declarando Listas

Para a criação de uma lista no Python, a sintaxe é a seguinte:

```python
nome_da_lista = []  # Criação de uma lista vazia.
nome_da_lista = [1, 2, 3]  # Criação de uma lista de inteiros.
nome_da_lista = [1, "Olá mundo!", 1.1]  # Criação de uma lista com vários tipos diferentes.
```

Podemos também criar listas dentro de outras listas. Essas são chamadas de nested lists e sua sintaxe é a seguinte:

```python
nome_da_lista = ["Olá mundo!", [1, 2, 3], ["outra_lista"]]
```

#### Tuplas

Uma tupla é uma estrutura bastante similar a uma lista, com apenas uma diferença: **os elementos inseridos em uma tupla não podem ser alterados**, diferente de uma lista onde podem ser alterados livremente. Sendo assim, em um primeiro momento, podemos pensar em uma tupla como uma lista que não pode ser alterada, mas não é bem assim…

É certo que as tuplas possuem diversas características das listas, porém os usos são distintos. As listas são destinadas a serem sequências homogêneas, enquanto que as Tuplas são estruturas de dados heterogêneas.

Sendo assim, apesar de bastante similares, a tupla é utilizada para armazenar dados de tipos diferentes, enquanto que a lista é para dados do mesmo tipo.

##### Declarando Tuplas

A sintaxe para criação de uma tupla, assim como uma lista, também é bem simples. Ao invés de se utilizar colchetes (listas), são utilizados parênteses, como podemos ver abaixo:

```python
nome_da_tupla = () # Tupla vazia
nome_da_tupla = (1, 2, 3) # Tupla de inteiros
nome_da_tupla = (1, "Olá mundo!", 1.5) # Tupla heterogênea
```

#### Tuplas x Listas

As tuplas possuem algumas vantagens com relação às listas, que são:

- Como as tuplas são imutáveis, a iteração sobre elas é mais rápida e, consequentemente, possuem um ganho de desempenho com relação às listas;
- Tuplas podem ser utilizadas como chave para um dicionário, já que seus elementos são imutáveis. Já com a lista, isso não é possível;
- Se for necessário armazenar dados que não serão alterados, utilize uma tupla. Isso garantirá que esses sejam protegidos de alterações posteriores.

#### Sets

No Python, os sets são uma coleção de itens desordenada, parcialmente imutável e que não podem conter elementos duplicados. Por ser parcialmente imutável, os sets possuem permissão de adição e remoção de elementos.

Além disso, os sets são utilizados, normalmente, com operações matemáticas de união, interseção e diferença simétrica, conforme veremos nos próximos tópicos.

##### Declarando Sets

Para a criação de um set no Python há duas formas: A primeira é bem similar às listas e tuplas, porém utilizando chaves **{}** para determinar os elementos do set:

```python
nome_do_set = {}  # Set vazio

# A segunda é utilizando o método 'set' presente no Python:
nome_do_set = set([])
```

#### Dicionários

No Python, os dicionários são coleções de itens desordenados com uma diferença bem grande quando comparados às outras coleções (_listas, sets, tuplas, etc_): **um elemento dentro de um dicionário possui uma chave atrelada a ele, uma espécie de identificador**. Sendo assim, é muito utilizado quando queremos armazenar dados de forma organizada e que possuem identificação única (como acontece em bancos de dados).

Um dicionário, portanto, pode ser visto como a figura abaixo:
![Diagrama de funcionamento de um Dicionário no Python](https://media.geeksforgeeks.org/wp-content/uploads/20200108193543/Dictionary_inmage1.jpg)

Onde cada valor é “atrelado” à uma chave, seu identificador. Vale lembrar que, por necessitar que cada valor possua uma chave relacionada a ele, as chaves dos dicionários devem ser únicas para que possam ser acessadas, também, através do seu índice.

> [!warning] ATENÇÃO:
> As chaves também não são armazenadas em qualquer ordem, elas apenas são associadas aos valores que pertencem.

##### Declarando Dicionários

Existem duas formas de se criar um dicionário utilizando o Python. A primeira delas é utilizando chaves ( {} ) e separando os elementos das chaves com dois pontos ( : ) e os outros elementos por vírgula ( , ):

```python
nome_do_dicionario = {1: 'João', 2: 'José'}
nome_do_dicionario = {'nome': 'João', 'sobrenome': 'Santos'}
```

A segunda forma é utilizando o método **dict()** com o dicionário sendo passado como parâmetro:

```python
nome_do_dicionario = dict({1: 'João', 2: 'José'})
nome_do_dicionario = dict({'nome': 'João', 'sobrenome': 'Santos'})
```

### Listas

Vamos agora aprofundar o nosso estudo em torno da estrutura de dados *"lista"*. Não se preocupe, que o estudo anterior também irá se aplicar aqui, pois precisamos das estruturas de repetição para percorrer as listas.

Trabalhar com listas nos permite resolver vários problemas. Você pode criar listas de cada um dos tipos básicos e até mesmo de outras listas.

**Mas, o quem vem a ser uma lista?**

_Ora tenho certeza que você já criou uma lista alguma vez na vida. Podemos citar diversos exemplos, como uma lista de compras no supermercado, a lista dos seus filmes favoritos, a lista das matérias que você precisa estudar mais._

![Lista de Tarefas em um caderno com uma caneta](https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1172&q=80)

**Em Python, uma lista é uma sequência mutável de n valores que podem ser de qualquer tipo (inclusive outras listas, tuplas e dicionários). De forma simples, uma lista pode ser entendida como um vetor de elementos que podem ser de qualquer tipo. As listas são exatamente iguais às Strings, exceto pelo fato de Strings serem imutáveis e listas serem mutáveis.**

As listas podem ser percorridas, “fatiadas” e concatenadas da mesma forma que as Strings. A diferença é que em se tratando de Strings, cada elemento é um caractere e, em se tratando de listas, cada elemento pode ser qualquer tipo de variável. Além disso, uma String pode ser convertida para uma lista (como já foi visto) e uma lista pode ser convertida para uma string. Abaixo são ilustradas estas duas conversões.

```python
a = "Eu adoro Python!"
# Converte cada letra da string em elementos de uma lista:
b = list(a)
print(b)  # ['E', 'u', ' ', 'a', 'd', 'o', 'r', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n', '!']

# Converte cada palavra da string (separada por espaço) em elementos de uma lista:
b = a.split()
print(b)  # ['Eu', 'adoro', 'Python!']

# Concatena todos os elementos da lista, separando-os por um espaço:
a = ' '.join(b)
print(a)  # Eu adoro Python!

```

Vamos começar com um exemplo simples, a lista de compras no mercado. Pois bem, vamos supor que a lista é composta pelos seguintes produtos: arroz, feijão, macarrão, cogumelo, pizza e leite . Essa é uma lista de strings (textos) constante, pois já sabemos de antemão quais são os seus elementos. Iremos agora salvar a lista em uma variável para manipulá-la usando algumas propriedades.

```python
compras = ['arroz', 'feijão', 'macarrão', 'cogumelo', 'pizza', 'leite']
print(compras[2])  # macarrão
tamanho = len(compras)
ultimo = tamanho - 1
print(compras[ultimo])  # leite
```

No código acima, salvamos a lista de compras na variável _**compras**_. Uma primeira propriedade sobre listas é que os seus elementos ocupam uma posição determinada. O primeiro elemento está na _posição 0_, o segundo na _posição 1_, e o último na _posição tamanho da lista - 1_. Assim, se você quiser obter o terceiro elemento da lista de compras, você deve fazer **_compras[2]_** (linha 2).

> [!warning] ATENÇÃO:
> Observe que você sempre deve seguir esse mesmo padrão (nome da lista, abre colchetes, posição, fecha colchetes) quando quiser obter um elemento da lista.

Caso você queira obter o tamanho da lista você deve usar a função “**len**”, passando para ela o nome da lista, como na _linha 3_ do código **(len(_compras_))**. Nós usamos essa informação para obter o último elemento da lista, que está na posição tamanho da lista – 1 (_linhas 4 e 5_).

Da mesma forma que podemos acessar os elementos de uma lista pela sua posição, é possível também modificar esses elementos. Se você quiser trocar o item **“macarrão”** por **“iogurte”**, você deve fazer: compras[2] **=** **"iogurte"** . Agora, se você der um **print** na lista (print(compras)) verá que na _posição 3_ (**compras[2]**) o item **“macarrão”** foi substituído por **“iogurte”**.

```python
compras = ['arroz', 'feijão', 'macarrão', 'cogumelo', 'pizza', 'leite']
compras[2] = 'iogurte'
print(compras[2])  # iogurte
tamanho = len(compras)
ultimo = tamanho - 1
print(compras[ultimo])  # leite
```

Preste atenção ao fato de que você só pode acessar um elemento que esteja na lista, ou seja, entre a _posição 0_ (primeiro elemento) e a _posição tamanho -1_ (último elemento). Se você tentar acessar um elemento fora dos limites da lista, o programa irá terminar com um erro.

Se você quiser adicionar um elemento em uma lista já criada anteriormente, você pode usar a palavra **append**. O **append** adiciona o novo elemento ao final da lista. Caso queira remover definitivamente um elemento de uma determinada posição, você deve usar a palavra **del**, na forma como é exemplificada no código a seguir.

```python
compras = ['arroz', 'feijão', 'macarrão', 'cogumelo', 'pizza', 'leite']
compras.append('sabão')
print(compras)  # ['arroz', 'feijão', 'macarrão', 'cogumelo', 'pizza', 'leite', 'sabão']
del(compras[1])
print(compras)  # ['arroz', 'macarrão', 'cogumelo', 'pizza', 'leite', 'sabão']

```

No código acima, ao adicionar o elemento “sabão” na _linha 3_ usando **append** a lista será composta da seguinte forma: [**"arroz", "feijão", "macarrão", "cogumelo", "pizza", "leite", "sabão"**]. Por sua vez, na linha 4 removemos o elemento da posição 1, ou seja, o **“feijão”**, tendo como resultado a lista: [**"arroz", "macarrão", "cogumelo", "pizza", "leite", "sabão"**].

Com o uso do **append**, é possível construirmos uma lista a partir da lista vazia. Por exemplo, vamos gerar a lista dos números ímpares de 3 até 15. Para isso, vamos precisar também de uma estrutura de repetição, conforme pode ser visto no código abaixo:

```python
impares = []
n = 3
while n <= 15:
	impares.append(n)
	n = n + 2  # n += 2
print(impares)  # [3, 5, 7, 9, 11, 13, 15]
```

Observe que na _linha 1_ do código foi criada uma lista vazia, denominada de ímpares. A variável “**_n_**” da _linha 2_ recebe o primeiro número ímpar. Ela serve de variável de controle do **while**, ao mesmo tempo que é usada para construir a lista. Na _linha 3_ temos o teste do **while**, que irá parar apenas quando “_**n**_” atingir o valor 15. Na _linha 4_, o **append** é usado para inserir cada elemento, um por vez em cada repetição. A _linha 5_ atualiza o valor de “**_n_**” para o próximo número ímpar. Por fim, a _linha 6_, que está fora do **while**, realiza a impressão da lista gerada.

Caro aluno, estamos terminando a parte escrita do nosso capítulo e, a seguir, serão apresentados algumas videoaulas que devem ser assistidas. No entanto, caso deseje saber mais sobre listas, seus operadores, funções e métodos, [clique neste link](https://www.devmedia.com.br/como-trabalhar-com-listas-em-python/37460).

### Dicionários

Como vimos no capítulo sobre as principais estruturas de dados no Python, os dicionários são coleções de itens desordenados com uma diferença bem grande quando comparados às outras coleções (listas, sets, tuplas, etc): **um elemento dentro de um dicionário possui uma chave atrelada a ele, uma espécie de identificador**.

Os dicionários proveem uma ótima forma para armazenar dados organizados e com um padrão simples de entender. Assim, saber manipulá-los é fundamental para utilizá-los em nossos projetos.

Por isso, neste capítulo, veremos como manipular os dicionários com os principais métodos disponibilizados no Python.

O código abaixo cria dois dicionários: o primeiro utilizando as chaves "**{ }**" e separando os elementos das suas chaves com dois pontos "**:**" e o segundo utilizando o método **dict()**. As duas formas terão o mesmo resultado.

```python
meu_dicionario = {1: 'Fábio', 2: 'Maria', 3: 'João', 4: 'José'}
print(type(meu_dicionario))
meu_dicionario_2 = dict({1: 'Fábio', 2: 'Maria', 3: 'João', 4: 'José'})
print(type(meu_dicionario_2))
```

Para retornar um elemento pelo seu índice de um dicionário, há duas formas. A primeira é passando, entre colchetes ([]) o índice do elemento desejado. Já a segunda é utilizando o método **get()** com a posição do elemento como parâmetro, conforme é demonstrado no código abaixo.

```python
meu_dicionario = {1: 'Fábio', 2: 'Maria', 3: 'João', 4: 'José'}
print(meu_dicionario[2])  # Maria
print(meu_dicionario[4])  # José
```

Já para inserir novos elementos em um dicionário, existem duas formas. A primeira é passar o valor ao índice de um dicionário e a segunda é utilizando o método **update()**, passando como parâmetro a chave e o elemento a ser adicionado.

```python
meu_dicionario = {1: 'Fábio', 2: 'Maria', 3: 'João', 4: 'José'}
# Adicionando elementos a um dicionário:
meu_dicionario[5] = 'Joaquina'
print(meu_dicionario)  # {1: 'Fábio', 2: 'Maria', 3: 'João', 4: 'José', 5: 'Joaquina'}
meu_dicionario.update({6: 'Pedro'})
print(meu_dicionario)  # {1: 'Fábio', 2: 'Maria', 3: 'João', 4: 'José', 5: 'Joaquina', 6: 'Pedro'}
# Removendo elementos de um dicionário:
meu_dicionario.pop(2)
print(meu_dicionario)  # {1: 'Fábio', 3: 'João', 4: 'José', 5: 'Joaquina', 6: 'Pedro'}
```

No código  figura acima, também é demonstrado como remover elementos de um dicionário utilizando o método **pop()** seguido do índice do elemento que deve ser removido.

Os dicionários proveem uma ótima forma para armazenar dados organizados e com um padrão simples de entender, como vimos neste artigo. Saber manipulá-los é fundamental para utilizá-los em nossos projetos.
