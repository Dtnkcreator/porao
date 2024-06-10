

'''
#1

def classifi():
    classificacion = int(input("Qual é o código do produto? "))

    match classificacion:

        case 1:
            print("\n É um alimento não-perecível.\n")
        case x if x >= 2 and x < 5:
            print("\n É um alimento perecível. \n")
        case x if x >= 5 and x < 7:
            print("\n É uma peça de vestuário. \n")
        case x if x >= 7 and x < 8:
            print("\n É um produto de higiene pessoal. \n")
        case x if x >= 8 and x < 16:
            print("\n É um produto de limpeza ou utensílio doméstico. \n")
        case _:
            print("\n Código Inválido. \n")

classifi()

'''


'''

#2


def media_calculo():
    m_aritmetica_1 = float(input("Escreva a primeira nota: "))

    m_aritmetica_2 = float(input("Escreva a segunda nota: "))

    media = (m_aritmetica_1 + m_aritmetica_2)/2
    match media:

        case x if x <= 4 and x >0:
            print(f"O aluno está reprovado, pois está com {media} de média.")
        case x if x <= 6.9 and x >4:
            print(f"O aluno está em exame, pois está com {media} de média.")
        case x if x <= 7 and x >= 10:
            print(f"O aluno está aprovado, pois está com {media} de média.")
        case _:
            print("Algo deu errado, tente novamente.")

media_calculo()

'''


'''

#3

def program_numbers():

    n1 = float(input("Escreva o primeiro número: "))

    n2 = float(input("Escreva o segundo número: "))

    operacao = int(input("Qual tipo de operação gostaria de aplicar nos dois números? (De 1 a 4) "))

    match operacao:
        case 1:
            calculo = (n1+n2)/2
            print(f"Após realizar a média entre os 2 números, o resultado é: {calculo}.")
    
        case 2:
            calculo = n1-n2
            print(f"Após realizar a diferença entre os 2 números, o resultado é: {calculo}.")

        case 3:
            calculo = n1*n2
            print(f"Após realizar o produto entre os 2 números, o resultado é: {calculo}.")

        case 4:
            calculo = n1/n2
            print(f"Após realizar a divisão entre os 2 números, o resultado é: {calculo}.")
        
        case _:
            print(f"O número {operacao} não está entre as alternativas, tente novamente.")

program_numbers()


'''

#4
#codigo do item,quantidade e valor 

def compra_lanchonete():

    produto = int(input("Qual o código do produto a ser escolhido? (De 101 a 105) "))

    quantidade = int(input("Qual a quantidade de lanches que será escolhida? "))

    match produto:
        
        case 100:
            calculo = quantidade*1.7
            return print ("O valor total a ser pago será: R$%.2f " %(calculo))

        case 101:
            calculo = quantidade*2.3
            return print ("O valor total a ser pago será: R$%.2f " %(calculo))

        case 102:
            calculo = quantidade*2.6
            return print ("O valor total a ser pago será: R$%.2f " %(calculo))

        case 103:
            calculo = quantidade*2.4
            return print ("O valor total a ser pago será: R$%.2f " %(calculo))

        case 104:
            calculo = quantidade*2.5
            return print ("O valor total a ser pago será: R$%.2f " %(calculo))

        case 105:
            calculo = quantidade*1.0
            return print ("O valor total a ser pago será: R$%.2f " %(calculo))

        case _:
            return print(f"O código {produto} não existe, tente novamente.")

cardapio_atendimento = compra_lanchonete()
