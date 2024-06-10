'''
#2 

lista_passaro = ["pombo", "papagaio", "pinguim", "periquito", "canário", "beija-flor", "tucano", "joão-de-barro", "quero-quero", "coruja"]

def zera_lista(l:list):
    print(l)
    entrada = input("Escreva o funcionamento: (Para parar é o termo \"stop\") ")
    if entrada == "stop":
        print("Fim do programa.")
    else:
        if len(l) > 0:
            l.pop()
            zera_lista(l)

        else:
            print("a lista não possui itens.")
            print("Fim do programa.")

zera_lista(lista_passaro)

'''

'''

def ola_infinito():
    entrada = input("Escreva algo: (Para parar o programa escreva \"stop\")")
    match entrada:
        case "stop":
            print(f"Fim do programa. A quantidade de olas foram de {repetiçoes} vezes.")
        case _:
            print("Olá!")
            ola_infinito()

ola_infinito()

'''

def operacion(n:int, n2:int):
    match funcao:
        case 1:

            soma = n + n2
            print(f"{n} + {n2} = {soma}")

        case 2:
            subtracion = n - n2
            print(f"{n} - {n2} = {subtracion}")

        case 3:
            multiplica = n * n2
            print(f"{n} x {n2} = {multiplica}")
        
        case 4:
            dividir = n / n2
            print(f"{n} / {n2} = {dividir}")
    
n = int (input("Qual número gostaria de adicionar? "))
n2 = int (input("Qual número gostaria de adicionar? "))
funcao = int(input("Qual operação numérica gostaria de realizar? (1. Adição, 2. Subtração, 3. Multiplicação, 4. Divisão) "))
operacion(n, n2)
    
def mescla_palavras(palavra:str,palavra2:str):
    mescla = palavra+" "+palavra2
    print(f"{palavra} + {palavra2} = {mescla}")

palavra = str (input("Adicione uma palavra: "))
palavra2 = str (input("Adicione uma segunda palavra: "))
mescla_palavras(palavra, palavra2)