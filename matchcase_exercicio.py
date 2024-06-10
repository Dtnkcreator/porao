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
