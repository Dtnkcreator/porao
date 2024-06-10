'''
palavras = []
def adiciona_palavra():
    print("Você deseja adicionar uma palavra?\n Digite qualquer coisa,\n Caso não digitar nada,\n o programa para.")
    entrada = input("digite: ")
    if entrada == "":
        print("você não digitou nada, fim do programa.")
        print(palavras)
    else:
        palavras.append(entrada)
        adiciona_palavra()

adiciona_palavra()

'''




#1
frases = []
print("Programa de escrever frases \n")

def nova_frase():
    entrada = input("Digite Algo: (Para encerrar o programa digite \"vazio\".) ")

    if entrada == "":

        def continuar_pergunta():
            continuar = input ("Você parou o programa. Deseja continuar ou não? (Sim/Não) ")

            if continuar == "sim" or continuar == "Sim":
                nova_frase()

            elif continuar == "não" or continuar == "Não":
                print ("\n Fim do programa.")
                print (f"Suas frases são: \n {frases}")
    
            else:
                print("\n Caractere inválido, tente novamente \n.")
                continuar_pergunta()
        continuar_pergunta()
    elif entrada == "apagar" or entrada == "Apagar":
        frases.pop(-1)
        nova_frase()
    else:
        frases.append(entrada)
        nova_frase()

nova_frase()


