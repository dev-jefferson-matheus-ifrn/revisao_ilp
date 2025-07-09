# Questão 01

# Você foi contratado para desenvolver um sistema que analisa uma relação de produtos vendidos
# ao longo de um ano, a respectiva quantidade vendida e o mês em que ocorreu a venda. Implemente um
# programa que solicite todas as linhas de registros da planilha ao usuário, o qual deverá inserir manualmente
# esses dados. Uma vez que esses dados tenham sido inseridos no programa, ele deverá apresentar as seguintes
# informações no terminal:
# a) Qual produto teve a maior quantidade vendida, ao longo dos meses?
# b) Qual o mês com o maior número de vendas?
# c) Qual o produto mais vendido em cada mês?
# d) Quantos produtos tiveram vendas acima de 50 unidades?
# e) Crie uma lista contendo apenas os produtos que venderam 50 ou mais unidades e o mês e exiba essa
# lista.

registros = []
numero_registros = int(input("Quantos registros de vendas você deseja inserir? "))

for i in range(numero_registros):
    linha = input("Insira o registro no formato 'produto,quantidade,mês': ")
    produto, quantidade, mes = linha.split(',')
    quantidade = int(quantidade)
    registros.append((produto, quantidade, mes))

# a) Qual produto teve a maior quantidade vendida, ao longo dos meses?
total_vendas = {}
for produto, quantidade, mes in registros:
    if produto in total_vendas:
        total_vendas[produto] += quantidade
    else:
        total_vendas[produto] = quantidade

maior_quantidade = 0
for produto, quantidade in total_vendas.items(): # o método .items() retorna os pares chaves e valores de um dicionário.
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        produto_mais_vendido = produto

print(f"a) O produto que teve a maior quantidade vendida ao longo dos meses foi {produto_mais_vendido}")

# b) Qual o mês com o maior número de vendas?
vendas_por_mes = {}
for produto, quantidade, mes in registros:
    if mes in vendas_por_mes:
        vendas_por_mes[mes] += quantidade
    else:
        vendas_por_mes[mes] = quantidade

maior_venda = 0
for mes, total in vendas_por_mes.items():
    if total > maior_venda:
        maior_venda = total
        mes_mais_vendido = mes

print(f"b) O mês com o maior número de vendas foi {mes_mais_vendido}")

# c) Qual o produto mais vendido em cada mês?
produtos_por_mes = {}
for produto, quantidade, mes in registros:
    if mes not in produtos_por_mes:
        produtos_por_mes[mes] = {} # cria uma chave com o nome do mês caso ele não exista.
    if produto in produtos_por_mes[mes]:
        produtos_por_mes[mes][produto] += quantidade
    else:
        produtos_por_mes[mes][produto] = quantidade

produto_mais_vendido_por_mes = {}

for mes, produtos in produtos_por_mes.items():
    maior_quantidade = -1
    for produto, quantidade in produtos.items():
        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            produto_mais_vendido = produto
    produto_mais_vendido_por_mes[mes] = produto_mais_vendido

print("c) O produto mais vendido em cada mês foi:")
for mes, produto in produto_mais_vendido_por_mes.items():
    print(f"Mês: {mes}, Produto: {produto}")

# d) Quantos produtos tiveram vendas acima de 50 unidades?
produtos_acima_50 = set()
for produto, quantidade, mes in registros:
    if quantidade > 50:
        produtos_acima_50.add(produto)

print(f"d) Quantidade de produtos com vendas acima de 50 unidades: {len(produtos_acima_50)}")

# e) Crie uma lista contendo apenas os produtos que venderam 50 ou mais unidades e o mês e exiba essa lista.
produtos_menor_50 = []
for produto, quantidade, mes in registros:
    if quantidade >= 50:
        produtos_menor_50.append((produto, quantidade, mes))

print("e) Lista de produtos que venderam 50 ou mais unidades e o mês:")
for produto, quantidade, mes in produtos_menor_50:
    print(f"Produto: {produto}, Quantidade: {quantidade}, Mês: {mes}")

# Questão 02

# Uma instituição de ensino deseja criar um sistema para armazenar o cadastro dos alunos. O
# programa deverá registrar, manualmente, uma coleção de alunos, bem como das disciplinas que os alunos
# podem cursar. Em seguida, o programa deverá permitir que os alunos possam se matricular nas disciplinas
# do interesse deles. Os alunos não devem ser matriculados em duplicidades nas disciplinas. Crie um menu
# que possibilite:
# a) Cadastrar (incluir/remover/atualizar) os alunos e disciplinas.
# b) Realizar a matrícula de aluno em disciplina.
# c) Exibir a relação de alunos e a relação de disciplinas, em separado.
# d) Exibir os dados de matrículas, por aluno, exibindo o nome do aluno e a relação de disciplinas nas
# quais esteja matriculado.
# e) Encerrar o programa (no caso específico dessa avaliação, isso deverá encerrar a questão) e exibir
# uma mensagem de encerramento.

alunos = {}
disciplinas = {}
matriculas = {} 

while True:
    print("\nMenu:")
    print("a) Cadastrar (incluir/remover/atualizar) os alunos e disciplinas")
    print("b) Realizar a matrícula de aluno em disciplina")
    print("c) Exibir a relação de alunos e a relação de disciplinas, em separado")
    print("d) Exibir os dados de matrículas, por aluno")
    print("e) Encerrar o programa")

    escolha = input("Escolha uma opção (a/b/c/d/e): ").strip()

    if escolha == 'a':
        print("\nCadastrar:")
        print("1) Incluir aluno")
        print("2) Remover aluno")
        print("3) Atualizar aluno")
        print("4) Incluir disciplina")
        print("5) Remover disciplina")
        print("6) Atualizar disciplina")
        
        cadastro_escolha = input("Escolha uma opção (1/2/3/4/5/6): ").strip()
        
        if cadastro_escolha == '1':
            aluno_id = input("Digite o ID do aluno: ").strip()
            aluno_nome = input("Digite o nome do aluno: ").strip()
            if aluno_id not in alunos:
                alunos[aluno_id] = aluno_nome
                matriculas[aluno_id] = []
                print("Aluno cadastrado com sucesso.")
            else:
                print("ID do aluno já existe.")

        elif cadastro_escolha == '2':
            aluno_id = input("Digite o ID do aluno a ser removido: ").strip()
            if aluno_id in alunos:
                del alunos[aluno_id]
                del matriculas[aluno_id]
                print("Aluno removido com sucesso.")
            else:
                print("ID do aluno não encontrado.")

        elif cadastro_escolha == '3':
            aluno_id = input("Digite o ID do aluno a ser atualizado: ").strip()
            if aluno_id in alunos:
                novo_nome = input("Digite o novo nome do aluno: ").strip()
                alunos[aluno_id] = novo_nome
                print("Nome do aluno atualizado com sucesso.")
            else:
                print("ID do aluno não encontrado.")

        elif cadastro_escolha == '4':
            disciplina_id = input("Digite o ID da disciplina: ").strip()
            disciplina_nome = input("Digite o nome da disciplina: ").strip()
            if disciplina_id not in disciplinas:
                disciplinas[disciplina_id] = disciplina_nome
                print("Disciplina cadastrada com sucesso.")
            else:
                print("ID da disciplina já existe.")

        elif cadastro_escolha == '5':
            disciplina_id = input("Digite o ID da disciplina a ser removida: ").strip()
            if disciplina_id in disciplinas:
                del disciplinas[disciplina_id]
                print("Disciplina removida com sucesso.")
                for aluno in matriculas:
                    if disciplina_id in matriculas[aluno]:
                        matriculas[aluno].remove(disciplina_id)
            else:
                print("ID da disciplina não encontrado.")

        elif cadastro_escolha == '6':
            disciplina_id = input("Digite o ID da disciplina a ser atualizada: ").strip()
            if disciplina_id in disciplinas:
                novo_nome = input("Digite o novo nome da disciplina: ").strip()
                disciplinas[disciplina_id] = novo_nome
                print("Nome da disciplina atualizado com sucesso.")
            else:
                print("ID da disciplina não encontrado.")

    elif escolha == 'b':
        aluno_id = input("Digite o ID do aluno: ").strip()
        disciplina_id = input("Digite o ID da disciplina: ").strip()
        if aluno_id in alunos and disciplina_id in disciplinas:
            if disciplina_id not in matriculas[aluno_id]:
                matriculas[aluno_id].append(disciplina_id)
                print("Matrícula realizada com sucesso.")
            else:
                print("O aluno já está matriculado nesta disciplina.")
        else:
            print("ID do aluno ou ID da disciplina não encontrado.")

    elif escolha == 'c':
        print("\nRelação de alunos:")
        for aluno_id, aluno_nome in alunos.items():
            print(f"ID: {aluno_id}, Nome: {aluno_nome}")

        print("\nRelação de disciplinas:")
        for disciplina_id, disciplina_nome in disciplinas.items():
            print(f"ID: {disciplina_id}, Nome: {disciplina_nome}")

    elif escolha == 'd':
        print("\nDados de matrículas por aluno:")
        for aluno_id, disciplinas_ids in matriculas.items():
            aluno_nome = alunos[aluno_id]
            disciplina_nomes = [disciplinas[disciplina_id] for disciplina_id in disciplinas_ids]
            print(f"Aluno: {aluno_nome}, Disciplinas: {', '.join(disciplina_nomes)}")

    elif escolha == 'e':
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida, por favor, escolha uma opção válida.")

# Questão 03

# Crie um programa que simula um campeonato de natação nado
# livre em piscina de 50m. O programa deverá receber como entrada o nome de 32 nadadores e dividí-los
# em 4 grupos(4x8). O programa deverá exibir o resultado das disputas de cada grupo escolhendo de forma
# aleatória os resultados de tempos em segundos que cada nadador obterá na disputa, os quais devem
# variar entre 20.00 e 22.99, ao longo de cada uma das fases de disputa até a etapa final do campeonato, e
# exibindo o nome e o resultado. A fase seguinte da competição consiste em formar mais dois grupos com
# 8 nadadores, cada qual formado pelos 16 melhores tempos da primeira fase, independente do grupo em
# que o nadador esteja. Se houver um empate no tempo entre os nadadores em qualquer uma das fases
# para determinar quem avança (como as semifinais), pode haver uma prova de desempate (swim-off) para
# decidir. Caso isso aconteça, o programa deverá exibir especificamente a disputa com os mesmos detalhes
# das fases anteriores, mas informando que se trata de um desempate. Para a fase final, seguem os 8
# melhores tempos dos nadadores entre os 16 competidores da fase anterior. Ao término da disputa da
# fase final, o programa deverá exibir o pódio informando quem foi o medalhista de ouro, o medalhista de
# prata e o medalhista de bronze. Caso haja empate na fase final, os nadadores que empatarem dividirão
# as medalhas entre si e isso deverá ser informado. Exemplo de uso da função uniform():
# # Exemplo de uso da função uniform()
# import random
# gera um número aleatório entre 1.00 e 30.99 com duas casas
# numero_aleatorio = round(random.uniform(1.0, 30.99), 2)

import random

# Inicializando listas para os grupos
grupo_nadadores1 = []
grupo_nadadores2 = []
grupo_nadadores3 = []
grupo_nadadores4 = []

# Coletando os nomes dos nadadores e dividindo em grupos
print("Digite os nomes dos 32 nadadores:")

for i in range(1, 33):
    nome = input(f'Nadador {i}: ')
    if len(grupo_nadadores1) < 8:
        grupo_nadadores1.append(nome)
    elif len(grupo_nadadores2) < 8:
        grupo_nadadores2.append(nome)
    elif len(grupo_nadadores3) < 8:
        grupo_nadadores3.append(nome)
    else:
        grupo_nadadores4.append(nome)

# Gerando tempos aleatórios para cada grupo
tempos_primeiro_grupo = {}
tempos_segundo_grupo = {}
tempos_terceiro_grupo = {}
tempos_quarto_grupo = {}

for nadador in grupo_nadadores1:
    tempos_primeiro_grupo[nadador] = round(random.uniform(20.00, 22.99), 2)

for nadador in grupo_nadadores2:
    tempos_segundo_grupo[nadador] = round(random.uniform(20.00, 22.99), 2)

for nadador in grupo_nadadores3:
    tempos_terceiro_grupo[nadador] = round(random.uniform(20.00, 22.99), 2)

for nadador in grupo_nadadores4:
    tempos_quarto_grupo[nadador] = round(random.uniform(20.00, 22.99), 2)

# Exibindo resultados dos grupos
print("\nResultados do Grupo 1:")
for nadador, tempo in tempos_primeiro_grupo.items():
    print(f"Nadador: {nadador}, Tempo: {tempo}s")

print("\nResultados do Grupo 2:")
for nadador, tempo in tempos_segundo_grupo.items():
    print(f"Nadador: {nadador}, Tempo: {tempo}s")

print("\nResultados do Grupo 3:")
for nadador, tempo in tempos_terceiro_grupo.items():
    print(f"Nadador: {nadador}, Tempo: {tempo}s")

print("\nResultados do Grupo 4:")
for nadador, tempo in tempos_quarto_grupo.items():
    print(f"Nadador: {nadador}, Tempo: {tempo}s")

# Consolidando todos os tempos em um único dicionário
tempos_geral = {}
tempos_geral.update(tempos_primeiro_grupo)
tempos_geral.update(tempos_segundo_grupo)
tempos_geral.update(tempos_terceiro_grupo)
tempos_geral.update(tempos_quarto_grupo)

# Convertendo o dicionário em lista de tuplas
tempos_geral_lista = list(tempos_geral.items())

# Ordenando a lista de tuplas por tempo (segundo item da tupla) manualmente
n = len(tempos_geral_lista)
for i in range(n):
    for j in range(i + 1, n):
        if tempos_geral_lista[j][1] < tempos_geral_lista[i][1]:
            tempos_geral_lista[i], tempos_geral_lista[j] = tempos_geral_lista[j], tempos_geral_lista[i]

# Selecionando os 16 melhores nadadores para a próxima fase
melhores_16 = tempos_geral_lista[:16]

# Criando grupos para a próxima fase
grupo_semifinal_1 = [nadador for nadador, tempo in melhores_16[:8]]
grupo_semifinal_2 = [nadador for nadador, tempo in melhores_16[8:]]

# Gerando tempos para a semifinal
tempos_semifinal_1 = {}
tempos_semifinal_2 = {}

for nadador in grupo_semifinal_1:
    tempos_semifinal_1[nadador] = round(random.uniform(20.00, 22.99), 2)

for nadador in grupo_semifinal_2:
    tempos_semifinal_2[nadador] = round(random.uniform(20.00, 22.99), 2)

# Exibindo resultados das semifinais
print("\nResultados da Semifinal 1:")
for nadador, tempo in tempos_semifinal_1.items():
    print(f"Nadador: {nadador}, Tempo: {tempo}s")

print("\nResultados da Semifinal 2:")
for nadador, tempo in tempos_semifinal_2.items():
    print(f"Nadador: {nadador}, Tempo: {tempo}s")

# Consolidando todos os tempos das semifinais e selecionando os 8 melhores para a final
todos_semifinais = list(tempos_semifinal_1.items()) + list(tempos_semifinal_2.items())

# Ordenando a lista de tuplas por tempo (segundo item da tupla) manualmente
n = len(todos_semifinais)
for i in range(n):
    for j in range(i + 1, n):
        if todos_semifinais[j][1] < todos_semifinais[i][1]:
            todos_semifinais[i], todos_semifinais[j] = todos_semifinais[j], todos_semifinais[i]

melhores_8 = todos_semifinais[:8]

# Gerando tempos para a final
tempos_final = {}
for nadador, tempo in melhores_8:
    tempos_final[nadador] = round(random.uniform(20.00, 22.99), 2)

# Exibindo resultados finais
print("\nResultados da Final:")
for nadador, tempo in tempos_final.items():
    print(f"Nadador: {nadador}, Tempo: {tempo}s")

# Determinando o pódio
classificacao = list(tempos_final.items())

# Ordenando a lista de tuplas por tempo (segundo item da tupla) manualmente
n = len(classificacao)
for i in range(n):
    for j in range(i + 1, n):
        if classificacao[j][1] < classificacao[i][1]:
            classificacao[i], classificacao[j] = classificacao[j], classificacao[i]

medalha_ouro = [classificacao[0][0]]
medalha_prata = [classificacao[1][0]]
medalha_bronze = [classificacao[2][0]]

# Verificar empates
tempo_ouro = tempos_final[medalha_ouro[0]]
tempo_prata = tempos_final[medalha_prata[0]]
tempo_bronze = tempos_final[medalha_bronze[0]]

for nadador, tempo in tempos_final.items():
    if tempo == tempo_ouro and nadador not in medalha_ouro:
        medalha_ouro.append(nadador)
    elif tempo == tempo_prata and nadador not in medalha_prata:
        medalha_prata.append(nadador)
    elif tempo == tempo_bronze and nadador not in medalha_bronze:
        medalha_bronze.append(nadador)

# Exibindo o pódio
print("\nPódio:")
print(f"Medalha de Ouro: {', '.join(medalha_ouro)}")
print(f"Medalha de Prata: {', '.join(medalha_prata)}")
print(f"Medalha de Bronze: {', '.join(medalha_bronze)}")