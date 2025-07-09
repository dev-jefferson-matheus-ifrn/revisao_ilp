#-------------- QUESTÃO 1 --------------
'''
1 – (10 pts) Você foi contratado para desenvolver um sistema que analisa uma relação de produtos vendidos
ao longo de um ano, a respectiva quantidade vendida e o mês em que ocorreu a venda. Implemente um
programa que solicite todas as linhas de registros da planilha ao usuário, o qual deverá inserir manualmente
esses dados. Uma vez que esses dados tenham sido inseridos no programa, ele deverá apresentar as seguintes
informações no terminal:
a) Qual produto teve a maior quantidade vendida, ao longo dos meses?
b) Qual o mês com o maior número de vendas?
c) Qual o produto mais vendido em cada mês?
d) Quantos produtos tiveram vendas acima de 50 unidades?
e) Crie uma lista contendo apenas os produtos que venderam 50 ou mais unidades e o mês e exiba essa lista.
'''
print("1. Relaçao de produtos vendidos ao longo do ano.")
# produtos = {
#     'Prod 1': {'jan':20, 'fev': 30},
#     'Prod 2': {'jan':20, 'mar': 30}
# }
produtos_qtd_mensais = {}
menu_options = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun', 7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez', 0: 'encerrar'}
while 1:
    prod = input(f"\nDigite o nome do produto que deseja inserir, ou 0 para parar: ")
    if prod == '0': 
        print('-' * 50, '\n')
        break
    
    print('\nAgora escolha o respectivo mês para inserir a quantidade de vendas.', end = '')
    while 1:
        mes = int(input('\nInsira o número corresponte ao mês, ou 0 para encerrar:\n'
            '\t1: Jan    2: Fev    3: Mar    4: Abr     5: Mai     6: Jun\n'
            '\t7: Jul    8: Ago    9: Set    10: Out    11: Nov    12: Dez\n'
            '\t0: encerrar\n'
            'Sua escolha: '))
        
        if mes not in menu_options:
            print('Opção no encontrada.')
            continue
        elif mes == 0:
            break
        
        qtd = int(input(f'Agora digite a quantidade de produtos vendidos no mês de {menu_options[mes]}: '))
        
        if not produtos_qtd_mensais.get(prod, False): #se não existir um produto cadastrado eu crio um dicionário
            produtos_qtd_mensais[prod] = {}
        produtos_qtd_mensais[prod][menu_options[mes]] = qtd

a_prod_que_vendeu_mais = {'prod': '', 'qtd': 0}
b_qtd_vendas_mes = {}
c_prod_mais_vendido_mes = {}
d_qtd_prod_com_mais_de_50 = 0
# essa última aqui, letra e, eu não entendi o que ele quer com lista, então eu fiz o que entendi mas com dicionário de listas
e_prod_com_mais_de_50_e_mes = {}

for prod, meses_qtd in produtos_qtd_mensais.items():
    soma_qtd_meses = 0
    teve_alguma_venda_acima_de_50 = False
    for mes, qtd in meses_qtd.items():
        soma_qtd_meses += qtd
        b_qtd_vendas_mes[mes] = qtd if b_qtd_vendas_mes.get(mes) == None else b_qtd_vendas_mes[mes]+qtd

        if c_prod_mais_vendido_mes.get(mes) == None:
            c_prod_mais_vendido_mes[mes] = prod
        elif qtd > produtos_qtd_mensais[c_prod_mais_vendido_mes[mes]][mes]:
            # atualiza o produto do mês se a quantidade do produto que está sendo verificado for maior do que a quantidade do produto já registrado no mês atual
            c_prod_mais_vendido_mes[mes] = prod
        
        if not teve_alguma_venda_acima_de_50:
            teve_alguma_venda_acima_de_50 = qtd > 50

        if qtd > 50:
            e_prod_com_mais_de_50_e_mes[prod] = [mes] if e_prod_com_mais_de_50_e_mes.get(prod) == None else e_prod_com_mais_de_50_e_mes[prod] + [mes]


    if (soma_qtd_meses > a_prod_que_vendeu_mais['qtd']):
        a_prod_que_vendeu_mais = {'prod': prod, 'qtd': soma_qtd_meses}
    
    if teve_alguma_venda_acima_de_50: 
        d_qtd_prod_com_mais_de_50 += 1

print('a) Qual produto teve a maior quantidade vendida, ao longo dos meses?\n', a_prod_que_vendeu_mais)

b_mes_com_mais_vendas = {'mes': '', 'qtd': 0}
for mes, qtd in b_qtd_vendas_mes.items():
    if (qtd > b_mes_com_mais_vendas['qtd']):
        b_mes_com_mais_vendas = {'mes': mes, 'qtd': qtd}

print('b) Qual o mês com o maior número de vendas?\n', b_mes_com_mais_vendas)
print('c) Qual o produto mais vendido em cada mês?\n', c_prod_mais_vendido_mes)
print('d) Quantos produtos tiveram vendas acima de 50 unidades?\n', d_qtd_prod_com_mais_de_50)
print('e) Lista contendo apenas os produtos que venderam 50 ou mais unidades e o(s) mês(es):\n', e_prod_com_mais_de_50_e_mes)