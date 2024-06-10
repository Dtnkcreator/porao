'''
#ATIVIDADE INTRODUTÓRIA
#1 Com Retorno

def com_r(a,b):
    return a+b

resultado = com_r(2,10)
print (resultado)


#2 Sem retorno
def sem_r(a,b):
    print(a+b)

sem_r(2,10)

'''


'''

#EXERCÍCIOS



#1.
#SEM RETURN
def soma(a,b):
    print(a+b)

a = int(input("letra A: "))
b = int(input("letra B: "))

print("A soma é :")
soma(a,b)
print("\n") 

'''

'''

#COM RETURN

def soma():
    a = int(input("letra A: "))
    b = int(input("letra B: "))
    return a+b

adicao = soma() 
print("A resposta é:", adicao)

'''




'''

#2.

n1 = int(input("n1: "))
n2 = int(input("n2: "))

def operacoes(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2

resultado = operacoes(n1,n2)

print("As operações respectivamentes de (+,-,* e /) são:")
print(resultado)

'''




'''

#3
print("\n")

def consumo_m():

    distancia = int(input("Escreva a distância percorrida: "))
    print(distancia, "km")
    total_c = int(input("Combustível gasto: "))
    print(total_c, "L")
    return distancia/total_c

consumo_medio = consumo_m()

print("O consumo médio por litro é: %.2fkm/L" %(consumo_medio))

'''





'''

#4
def info_salario():
    nome = str(input("Nome: "))
    salario = int(input("Salário: "))
    vendas = int(input("Vendas em dinheiro: "))
    comissao = vendas * 0.15
    salario_total = salario + comissao
    print("Nome:", nome, "\n", "Salário Fixo: R$", salario, "\n", "Salário Total: R$", salario_total)

info_salario()


'''






'''

#7

def conversao_temp():
    celsius = int(input("Temperatura em Celsius °C: "))
    fahrenheit = 9 * celsius+160/5
    print("A temperatura de °C,", celsius, "convertida em °F é:", fahrenheit)

conversao_temp()

'''






'''

#8

def conversao_real_dolar():
    real = int(input("Valor em R$: "))
    cotaçao = int(input("Cotação do dólar em R$: "))
    return real/cotaçao

dolar = conversao_real_dolar() 
print("O valor de conversão de R$ para U$ é: 5,17")
print("O valor disponível de U$ é: %.2f" %(dolar))


'''





'''

#9

def poupanca():
    valor_dp = 0
    valor_dp += int(input("Valor depositado: "))
    juros = valor_dp * 0.007
    return valor_dp + juros
resultado = poupanca()
print("O valor após botar na poupança é:", resultado)

'''






'''
#10

def mamao_acucar():
    produto = int(input("Valor do produto comprado: "))
    prestacoes = produto/5
    print("O valor do produto foi R$", produto, "e será dividido em 5 prestações de R$", prestacoes)

mamao_acucar()

'''






#12
fabrica = int(input("Valor da fabricação do produto para informarmos seu valor total: "))
def imposto_distribuidor():
    global fabrica
    imposto_distribuidor = fabrica + (fabrica * 0.28)
    return imposto_distribuidor

def calculos_impostos_gov(v):
    v+= v*0.45
    return v

v_atualizado = imposto_distribuidor()
v_atualizado = calculos_impostos_gov(v_atualizado)

print(f"O valor da fábrica foi {fabrica} total gasto pelo consumidor foi de {v_atualizado}")




