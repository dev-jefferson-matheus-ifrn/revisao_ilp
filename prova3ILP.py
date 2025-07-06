# QUESTÕES AVALIÇÃO ILP

"""
1 – (10 pts) Você foi contratado para desenvolver um sistema que analisa uma relação de produtos vendidos
ao longo de um ano, a respectiva quantidade vendida e o mês em que ocorreu a venda. Implemente um
programa que solicite todas as linhas de registros da planilha ao usuário, o qual deverá inserir manualmente
esses dados. Uma vez que esses dados tenham sido inseridos no programa, ele deverá apresentar as seguintes
informações no terminal:
a) Qual produto teve a maior quantidade vendida, ao longo dos meses?
b) Qual o mês com o maior número de vendas?
c) Qual o produto mais vendido em cada mês?
d) Quantos produtos tiveram vendas acima de 50 unidades?
e) Crie uma lista contendo apenas os produtos que venderam 50 ou mais unidades e o mês e exiba essa
lista
"""

# quantidade_produtos = int(input('Informe a quantidade de itens no estoque: '))

# produtos = [input('Iforeme o produto: ') for i in range(quantidade_produtos)]

# print(produtos)


# itens_vendidos_mes = {}

# quantidade_total_itens_vendidos_mes = {}

# lista_quantidade_total_itens_vendidos_mes = []

# maior_valor_itens_vendidos_mes = 0

# quantidade_produtos_acima_50 = 0

# produtos_acima_50 = []

# quantidade_produtos_ao_longo_meses = {}

# item_mais_vendido_ao_longo_mes = ''

# quantidade_item_mais_vendido_ao_longo_mes = 0



# for i in range(2):
#     mes = input('Informe o mês de vendas: ')
#     quantidade_itens_vendidos_mes = {}
#     quantidade_total = 0
#     for produto in produtos:
#         quantidade = int(input(f'Informe a quantidade de {produto} vendidos(a): '))
#         quantidade_itens_vendidos_mes[produto] = quantidade
#         quantidade_total += quantidade
#     itens_vendidos_mes[mes] = quantidade_itens_vendidos_mes
#     quantidade_total_itens_vendidos_mes[mes] = quantidade_total
#     lista_quantidade_total_itens_vendidos_mes += [quantidade_total]

    


# print(itens_vendidos_mes)

# print(quantidade_total_itens_vendidos_mes)

# print(lista_quantidade_total_itens_vendidos_mes)

# for quantidade in lista_quantidade_total_itens_vendidos_mes:
#     if(maior_valor_itens_vendidos_mes < quantidade):
#         maior_valor_itens_vendidos_mes = quantidade

# for chave,valor in quantidade_total_itens_vendidos_mes.items():
#     if(maior_valor_itens_vendidos_mes == valor):
#         print(chave)


# for chave,valor in itens_vendidos_mes.items():
#     t = dict(itens_vendidos_mes[chave])
#     for c,v in t.items():
#         if((v >= 50) and (c not in produtos_acima_50)):
#             quantidade_produtos_acima_50 += 1
#             produtos_acima_50 += [c]
#             print(quantidade_produtos_acima_50)
#             print(produtos_acima_50)
    

# for key,value in itens_vendidos_mes.items():
#     valores = dict(itens_vendidos_mes[key])
#     quantidade_produto_mais_vendido_mes = 0
#     for item,total in valores.items():
#         if(quantidade_produto_mais_vendido_mes < total):
#             quantidade_produto_mais_vendido_mes = total
#             produto_mais_vendido = item
#     print(f'{key}:{produto_mais_vendido}')
        


# for mes, itens_vendidos in itens_vendidos_mes.items():
#     vendas = dict(itens_vendidos_mes[mes])
#     for nome_produto, quantidade_vendida in vendas.items():
#         total_produto_especifico = 0
#         if(nome_produto in quantidade_produtos_ao_longo_meses):
#             total_produto_especifico += quantidade_vendida
#             quantidade_produtos_ao_longo_meses[nome_produto] += total_produto_especifico
#         else:
#             quantidade_produtos_ao_longo_meses[nome_produto] = quantidade_vendida


# for produto, quantidade_ao_longo_mes in quantidade_produtos_ao_longo_meses.items():
#     if(quantidade_item_mais_vendido_ao_longo_mes < quantidade_ao_longo_mes):
#         quantidade_item_mais_vendido_ao_longo_mes = quantidade_ao_longo_mes
#         item_mais_vendido_ao_longo_mes = produto


# print(quantidade_produtos_ao_longo_meses)
# print(f'Item mais vendido ao longo do mês: {item_mais_vendido_ao_longo_mes}')

# ---------------------------------------------------------------------

"""
2 – (10 pts) Uma instituição de ensino deseja criar um sistema para armazenar o cadastro dos alunos. O
programa deverá registrar, manualmente, uma coleção de alunos, bem como das disciplinas que os alunos
podem cursar. Em seguida, o programa deverá permitir que os alunos possam se matricular nas disciplinas
do interesse deles. Os alunos não devem ser matriculados em duplicidades nas disciplinas. Crie um menu
que possibilite:
a) Cadastrar (incluir/remover/atualizar) os alunos e disciplinas.
b) Realizar a matrícula de aluno em disciplina.
c) Exibir a relação de alunos e a relação de disciplinas, em separado.
d) Exibir os dados de matrículas, por aluno, exibindo o nome do aluno e a relação de disciplinas nas
quais esteja matriculado.
e) Encerrar o programa (no caso específico dessa avaliação, isso deverá encerrar a questão) e exibir
uma mensagem de encerramento.
"""
disciplinas = []
alunos = []
matriculas = {}

print('\t\t\tCADASTRO DE ALUNOS\n')

print('\t\t\t1-Cadastrar uma disciplina')
print('\t\t\t2-Cadastrar um aluno')
print('\t\t\t3-Remover um aluno')
print('\t\t\t4-Remover uma disciplina')
print('\t\t\t5-Atualizar um aluno')
print('\t\t\t6-Atualizar uma disciplina')
print('\t\t\t7-Matricular um aluno')
print('\t\t\t8-Alunos matriculados')
print('\t\t\t9-Sair\n')
print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
escolha = int(input('\t\t\tInforme a escolha: '))





while(escolha != 9):
    match escolha:
        case 1:
            disciplina = input('\t\t\tInforme a disciplina a ser cadastrada: ')
            print('\t\t\t_________________________________________________________')
            if(disciplina not in disciplinas):
                disciplinas += [disciplina]
            print('\t\t\tCADASTRO DE ALUNOS\n')

            print('\t\t\t1-Cadastrar uma disciplina')
            print('\t\t\t2-Cadastrar um aluno')
            print('\t\t\t3-Remover um aluno')
            print('\t\t\t4-Remover uma disciplina')
            print('\t\t\t5-Atualizar um aluno')
            print('\t\t\t6-Atualizar uma disciplina')
            print('\t\t\t7-Matricular um aluno')
            print('\t\t\t8-Alunos matriculados')
            print('\t\t\t9-Sair\n')
            print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
            escolha = int(input('\t\t\tInforme a escolha: '))
            while(not((escolha <= 9) and (escolha >= 1))):
                escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))

        case 2:
            aluno = input('\t\t\tInforme O Aluno a ser cadastrado(a): ')
            print('\t\t\t_________________________________________________________')
            if(aluno not in alunos):
                alunos += [aluno]
            print('\t\t\tCADASTRO DE ALUNOS\n')

            print('\t\t\t1-Cadastrar uma disciplina')
            print('\t\t\t2-Cadastrar um aluno')
            print('\t\t\t3-Remover um aluno')
            print('\t\t\t4-Remover uma disciplina')
            print('\t\t\t5-Atualizar um aluno')
            print('\t\t\t6-Atualizar uma disciplina')
            print('\t\t\t7-Matricular um aluno')
            print('\t\t\t8-Alunos matriculados')
            print('\t\t\t9-Sair\n')
            print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
            escolha = int(input('\t\t\tInforme a escolha: '))
            while(not((escolha <= 9) and (escolha >= 1))):
                escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))

        case 3:
            aluno = input('\t\t\tInforme O Aluno a ser removido(a): ')
            print('\t\t\t_________________________________________________________')
            if(aluno in alunos):
                alunos.remove(aluno)
            else:
                print('\t\t\tAluno não encontrado')

            print('\t\t\tCADASTRO DE ALUNOS\n')

            print('\t\t\t1-Cadastrar uma disciplina')
            print('\t\t\t2-Cadastrar um aluno')
            print('\t\t\t3-Remover um aluno')
            print('\t\t\t4-Remover uma disciplina')
            print('\t\t\t5-Atualizar um aluno')
            print('\t\t\t6-Atualizar uma disciplina')
            print('\t\t\t7-Matricular um aluno')
            print('\t\t\t8-Alunos matriculados')
            print('\t\t\t9-Sair\n')
            print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
            escolha = int(input('\t\t\tInforme a escolha: '))
            while(not((escolha <= 9) and (escolha >= 1))):
                escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))

         
        case 4:
            disciplina = input('\t\t\tInforme disciplina a ser removido(a): ')
            print('\t\t\t_________________________________________________________')
            if(disciplina in disciplinas):
                disciplinas.remove(disciplina)
            else:
                print('\t\t\tDisciplina não encontrada')

            print('\t\t\tCADASTRO DE ALUNOS\n')

            print('\t\t\t1-Cadastrar uma disciplina')
            print('\t\t\t2-Cadastrar um aluno')
            print('\t\t\t3-Remover um aluno')
            print('\t\t\t4-Remover uma disciplina')
            print('\t\t\t5-Atualizar um aluno')
            print('\t\t\t6-Atualizar uma disciplina')
            print('\t\t\t7-Matricular um aluno')
            print('\t\t\t8-Alunos matriculados')
            print('\t\t\t9-Sair\n')
            print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
            escolha = int(input('\t\t\tInforme a escolha: '))
            while(not((escolha <= 9) and (escolha >= 1))):
                escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))

        case 5:
            aluno = input('\t\t\tInforme o aluno(a) a ser atualizado(a): ')
            if aluno in alunos:
                atualização = input('\t\t\tInforma o aluno(a) atualizado(a): ')
                index = alunos.index(aluno)
                alunos[index] = [atualização]
                if aluno in matriculas:
                    disciplinas_cursando = matriculas[aluno]

                    matriculas[atualização] = disciplinas_cursando

                    del matriculas[aluno]
            else:
                print('\t\t\tAluno não encontrado')
                print('\t\t\t___________________________________________________')
                print('\t\t\tCADASTRO DE ALUNOS\n')

                print('\t\t\t1-Cadastrar uma disciplina')
                print('\t\t\t2-Cadastrar um aluno')
                print('\t\t\t3-Remover um aluno')
                print('\t\t\t4-Remover uma disciplina')
                print('\t\t\t5-Atualizar um aluno')
                print('\t\t\t6-Atualizar uma disciplina')
                print('\t\t\t7-Matricular um aluno')
                print('\t\t\t8-Alunos matriculados')
                print('\t\t\t9-Sair\n')
                print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
                escolha = int(input('\t\t\tInforme a escolha: '))
                while(not((escolha <= 9) and (escolha >= 1))):
                    escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))

            print('\t\t\tCADASTRO DE ALUNOS\n')

            print('\t\t\t2-Cadastrar um aluno')
            print('\t\t\t3-Remover um aluno')
            print('\t\t\t4-Remover uma disciplina')
            print('\t\t\t5-Atualizar um aluno')
            print('\t\t\t6-Atualizar uma disciplina')
            print('\t\t\t7-Matricular um aluno')
            print('\t\t\t8-Alunos matriculados')
            print('\t\t\t9-Sair\n')
            print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
            escolha = int(input('\t\t\tInforme a escolha: '))
            while(not((escolha <= 9) and (escolha >= 1))):
                escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))

        case 6:
            disciplina = input('\t\t\tInforme o disciplina a ser atualizado: ')
            if disciplina in disciplinas:
                atualização = input('\t\t\tInforma a disciplina atualizada: ')
                index = disciplinas.index(disciplina)
                disciplinas[index] = atualização
                for chave, valor in matriculas.items():
                    disciplinas_a_serem_alteradas = list(matriculas[chave])
                    if disciplina in disciplinas_a_serem_alteradas:
                        index = disciplinas_a_serem_alteradas.index(disciplina)
                        disciplinas_a_serem_alteradas[index] = atualização
                        matriculas[chave] = disciplinas_a_serem_alteradas
                        

            else:
                print('\t\t\tDisciplina não encontrada')
                print('\t\t\t___________________________________________________')
                print('\t\t\tCADASTRO DE ALUNOS\n')

                print('\t\t\t1-Cadastrar uma disciplina')
                print('\t\t\t2-Cadastrar um aluno')
                print('\t\t\t3-Remover um aluno')
                print('\t\t\t4-Remover uma disciplina')
                print('\t\t\t5-Atualizar um aluno')
                print('\t\t\t6-Atualizar uma disciplina')
                print('\t\t\t7-Matricular um aluno')
                print('\t\t\t8-Alunos matriculados')
                print('\t\t\t9-Sair\n')
                print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
                escolha = int(input('\t\t\tInforme a escolha: '))
                while(not((escolha <= 9) and (escolha >= 1))):
                    escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))

            print('\t\t\tCADASTRO DE ALUNOS\n')

            print('\t\t\t2-Cadastrar um aluno')
            print('\t\t\t3-Remover um aluno')
            print('\t\t\t4-Remover uma disciplina')
            print('\t\t\t5-Atualizar um aluno')
            print('\t\t\t6-Atualizar uma disciplina')
            print('\t\t\t7-Matricular um aluno')
            print('\t\t\t8-Alunos matriculados')
            print('\t\t\t9-Sair\n')
            print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
            escolha = int(input('\t\t\tInforme a escolha: '))
            while(not((escolha <= 9) and (escolha >= 1))):
                escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))
            
                 
        
        case 7:
            aluno = input('\t\t\tInforme aluno a ser matriculado(a): ')
            disciplina = input('\t\t\tInforme a disciplina para o aluno ser matriculado(a): ')
            if((aluno not in alunos) or (disciplina not in disciplinas)):
                print('\t\t\tDisciplina ou aluno não encontrado\n')
                print('\t\t\t___________________________________________________')
                print('\t\t\tCADASTRO DE ALUNOS\n')

                print('\t\t\t1-Cadastrar uma disciplina')
                print('\t\t\t2-Cadastrar um aluno')
                print('\t\t\t3-Remover um aluno')
                print('\t\t\t4-Remover uma disciplina')
                print('\t\t\t5-Atualizar um aluno')
                print('\t\t\t6-Atualizar uma disciplina')
                print('\t\t\t7-Matricular um aluno')
                print('\t\t\t8-Alunos matriculados')
                print('\t\t\t9-Sair\n')
                print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
                escolha = int(input('\t\t\tInforme a escolha: '))
                while(not((escolha <= 9) and (escolha >= 1))):
                    escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))
            else:
                if aluno not in matriculas:
                    matriculas[aluno] = [disciplina]
                    print('\t\t\tCADASTRO DE ALUNOS\n')

                    print('\t\t\t1-Cadastrar uma disciplina')
                    print('\t\t\t2-Cadastrar um aluno')
                    print('\t\t\t3-Remover um aluno')
                    print('\t\t\t4-Remover uma disciplina')
                    print('\t\t\t5-Atualizar um aluno')
                    print('\t\t\t6-Atualizar uma disciplina')
                    print('\t\t\t7-Matricular um aluno')
                    print('\t\t\t8-Alunos matriculados')
                    print('\t\t\t9-Sair\n')
                    print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
                    escolha = int(input('\t\t\tInforme a escolha: '))
                    while(not((escolha <= 9) and (escolha >= 1))):
                        escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))
                else:
                    matriculas[aluno] += [disciplina]
                    print('\t\t\tCADASTRO DE ALUNOS\n')

                    print('\t\t\t1-Cadastrar uma disciplina')
                    print('\t\t\t2-Cadastrar um aluno')
                    print('\t\t\t3-Remover um aluno')
                    print('\t\t\t4-Remover uma disciplina')
                    print('\t\t\t5-Atualizar um aluno')
                    print('\t\t\t6-Atualizar uma disciplina')
                    print('\t\t\t7-Matricular um aluno')
                    print('\t\t\t8-Alunos matriculados')
                    print('\t\t\t9-Sair\n')
                    print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
                    escolha = int(input('\t\t\tInforme a escolha: '))
                    while(not((escolha <= 9) and (escolha >= 1))):
                        escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))



        case 8:
            print(f'\t\t\t{matriculas}\n')
            print('\t\t\t_____________________________________________')
            print('\t\t\tCADASTRO DE ALUNOS\n')

            print('\t\t\t1-Cadastrar uma disciplina')
            print('\t\t\t2-Cadastrar um aluno')
            print('\t\t\t3-Remover um aluno')
            print('\t\t\t4-Remover uma disciplina')
            print('\t\t\t5-Atualizar um aluno')
            print('\t\t\t6-Atualizar uma disciplina')
            print('\t\t\t7-Matricular um aluno')
            print('\t\t\t8-Alunos matriculados')
            print('\t\t\t9-Sair\n')
            print('\t\t\tEscolha de 1 a 9 para utilizar as opções')
            escolha = int(input('\t\t\tInforme a escolha: '))
            while(not((escolha <= 9) and (escolha >= 1))):
                escolha = int(input('\t\t\tEscolha errada Informe a escolha correta: '))
                





            