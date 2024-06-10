lista = ["José", "Gustavo", "Ernesto", "Júlia"]
print("Lista antes do Pedro:")
print(lista)
def add_pedro():

    lista.append("Pedro")
    print("Lista com Pedro:")
    return print(lista)

add_pedro()

def add_nome():
    pergunta = input("(1) Adicionar (2) Sair: ")
    if pergunta == 1:
        nome1 = input("Nome para adicionar")
        lista.append(nome1)
        print(lista)
        add_nome()
    else:
         print("Fim do programa")

add_nome()