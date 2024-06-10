

'''

#9 


#NOME
nome = str(input("Qual o seu nome? "))


def calculo_total():
    #BEBIDA
    vai_beber = str(input(f"{nome}, irá beber algo? "))
    gasto_bebida = 0
    if vai_beber == "sim" or vai_beber == "Sim":
        gasto_bebida += 80
    
    print(f"O gasto da bebida será R${gasto_bebida}.")

    #COMIDA
    vai_comer = str(input(f"{nome}, irá comer algo? "))
    gasto_comida = 0
    if vai_comer == "sim" or vai_comer == "Sim":
        gasto_comida += 60
    print(f"O gasto da comida será R${gasto_comida}.")
    
    #TRANSPORTE
    vai_transporte = str(input(f"{nome}, irá ir de transporte? "))
    gasto_transporte = 0
    if vai_transporte == "sim" or vai_transporte == "Sim":
        gasto_transporte += 15
    print(f"O gasto de transporte será R${gasto_transporte}.")
    
    #PESSOAS
    gasto_pessoas = int(input(f"{nome}, irá com quantas pessoas? "))

    print(f"Todos os gastos anteriores serão aplicados para {gasto_pessoas} pessoas.")

    return (gasto_transporte+gasto_comida+gasto_bebida)*(gasto_pessoas+1)

gastos = calculo_total()

print(f"Os possíveis gastos da noite serão R${gastos}.")

'''

'''

#VARIAÇÂO #9

# bebida 80 comida 60 transporte 15
gasto_total = 0

print("custo médio da noite  bebida 80 comida 60 transporte 15 ")
pergunta1_bebida= int(input("deseja beber? [1]para sim e [2]para não "))
if not pergunta1_bebida == 1 and not pergunta1_bebida == 2:
    print("opção inválida")
pergunta2_comida= int(input("deseja comer? [1]para sim e [2]para não "))
if not pergunta2_comida == 1 and not pergunta2_comida == 2:
    print("opção inválida")
pergunta3_transporte= int(input("deseja transporte? [1]para sim e [2]para não "))
if not pergunta3_transporte == 1 and not pergunta3_transporte == 2:
    print("opção inválida")

pergunta4_amigos= int(input("quantas pessoas vão sair com você? "))


def calc_gasto_noite(b,c,t,a):
    global gasto_total
    if b == 1:
        gasto_total += 80
    if c == 1:
        gasto_total += 60      
    if t == 1:
        gasto_total += 15
    if a > 0:
        gasto_total += gasto_total*a+1
calc_gasto_noite(pergunta1_bebida,pergunta2_comida,pergunta3_transporte,pergunta4_amigos)

print(f"o gasto estimado da noite é R${gasto_total}")



'''







'''

#3

   
tempo_menor_aposenta = 25
tempo_max_aposenta = 40

print("Bem vindo ao programa para calcular o benefício para aposentadoria. \n")

sexo = str(input("Qual o seu sexo? (M/F) "))


idade_começou_contribuir = int(input("Com qual idade começou a contribuir? "))

#masculino
idade_min_aposentadoria = idade_começou_contribuir + tempo_menor_aposenta

idade_max_aposentadoria = idade_começou_contribuir + tempo_max_aposenta
#feminino
idade_min_aposentadoria_f = idade_começou_contribuir + tempo_menor_aposenta

def reforma_previdencia(): 
    if sexo == "m" or sexo == "M":
        if idade_começou_contribuir <= 40:
            print ("A idade mínima para se aposentar é 65 anos. \n")
        else:
            print (f"A idade mínima para conseguir se aposentar é {idade_min_aposentadoria}. \n")
    
        print(f"Com essa idade será possível conseguir 70% do benefício. \n")

        print(f"Para alcançar o benefício máximo será preciso trabalhar até {idade_max_aposentadoria}. \n")

    if sexo == "F" or sexo == "f":
        if idade_começou_contribuir <= 37:
            print ("A idade mínima para se aposentar é 62 anos. \n")
        else:
            print (f"A idade mínima para conseguir se aposentar é {idade_min_aposentadoria}. \n")
    
        print(f"Com essa idade será possível conseguir 77,5% do benefício. \n")
        
        print(f"Para alcançar o benefício máximo (100%) será preciso trabalhar até {idade_max_aposentadoria}. \n")

calculo_previdencia = reforma_previdencia()

'''

'''
1) qual idade para quando aposentar
2) porcentagem que terá direito com idade mínima
3) qual a idade para quando conseguir 100% da previdência

'''







#CORREÇÃO

TEMPO_CONTRI_MAXIMO = 40
sexo = str(input("digite M para masculino ou F para feminino"))
idade_contri_inicial = int(input("Com qual idade você começou a contribuir?"))
idade_contri_projetada_m = 65 - idade_contri_inicial
idade_contri_projetada_f = 62 - idade_contri_inicial

def print_tempo_faltando_homem():
    print("você terá direito a se aposentar com 65 anos")
    print(f"Você precisa trabalhar até os {tempo_faltando_contri_homem()} anos para conseguir 100%")
def print_tempo_faltando_mulher():
    print("você terá direito a se aposentar com 62 anos")
    print(f"Você precisa trabalhar até os {tempo_faltando_contri_mulher()} anos para conseguir 100%")
def tempo_faltando_contri_homem():
    global TEMPO_CONTRI_MAXIMO
    global idade_contri_projetada_m
    idade_contri_projetada_m_faltando = (TEMPO_CONTRI_MAXIMO - idade_contri_projetada_m)+65
    return idade_contri_projetada_m_faltando

def tempo_faltando_contri_mulher():
    global TEMPO_CONTRI_MAXIMO
    global idade_contri_projetada_f
    idade_contri_projetada_f_faltando = (TEMPO_CONTRI_MAXIMO - idade_contri_projetada_m)+65
    return idade_contri_projetada_f_faltando

def calc_contri_homem():
    global idade_contri_projetada_m
    if idade_contri_projetada_m >=25 and idade_contri_projetada_m <=29:
        print(f"você tem{idade_contri_projetada_m} anos de contribuição, o que te dá direito a 70% sobre o beneficio")
        print_tempo_faltando_homem()
    elif idade_contri_projetada_m >=30 and idade_contri_projetada_m <=34:
        print(f"você tem{idade_contri_projetada_m} anos de contribuição, o que te dá direito a 77,5% sobre o beneficio")
        print_tempo_faltando_homem()
    elif idade_contri_projetada_m >=35 and idade_contri_projetada_m <=39:
        print(f"você tem{idade_contri_projetada_m} anos de contribuição, o que te dá direito a 87,5% sobre o beneficio")
        print_tempo_faltando_homem()
    elif idade_contri_projetada_m >=40:
        print(f"você tem{idade_contri_projetada_m} anos de contribuição, o que te dá direito a 100% sobre o beneficio")
        print_tempo_faltando_homem()
    else:
        print(f"so sorry, você não atingiu o tempo mínimo de contribuição. Seu tempo de contribuição foi:{idade_contri_projetada_m} anos")
        print_tempo_faltando_homem()    

def calc_contri_mulher():
    global idade_contri_projetada_f
    if idade_contri_projetada_f >=25 and idade_contri_projetada_f <=29:
        print(f"você tem{idade_contri_projetada_f} anos de contribuição, o que te dá direito a 70% sobre o beneficio")
        print_tempo_faltando_mulher()
    elif idade_contri_projetada_f >=30 and idade_contri_projetada_f <=34:
        print(f"você tem{idade_contri_projetada_f} anos de contribuição, o que te dá direito a 77,5% sobre o beneficio")
        print_tempo_faltando_mulher()        
    elif idade_contri_projetada_f >=35 and idade_contri_projetada_f <=39:
        print(f"você tem{idade_contri_projetada_f} anos de contribuição, o que te dá direito a 87,5% sobre o beneficio")
        print_tempo_faltando_mulher()        
    elif idade_contri_projetada_f >=40:
        print(f"você tem{idade_contri_projetada_f} anos de contribuição, o que te dá direito a 100% sobre o beneficio")
        print_tempo_faltando_mulher()        
    else:
        print(f"so sorry, você não atingiu o tempo mínimo de contribuição. Seu tempo de contribuição foi:{idade_contri_projetada_f} anos")
        print_tempo_faltando_mulher()        



if sexo == "m" or sexo == "M":
    calc_contri_homem()
elif sexo == "f" or sexo == "F":
    calc_contri_mulher()
else:
    print("você digitou errado as opções.")
