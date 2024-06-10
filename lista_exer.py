'''

#15


lista = []

for x in range (0,11):
    if x <= 9:
        entrada = int(input("digite um número: "))
        lista.append(entrada)

print("Digite 10 números:")
for n in lista:
    print(n)

print("Ordem original: ", lista)

lista.reverse()
print("Ordem inversa: ",lista)


'''


#4



#SEM LISTA
def verific_nome():
    print("Digite quatro nomes:")

    nome1 = str(input(""))
    nome2 = str(input(""))
    nome3 = str(input(""))
    nome4 = str(input(""))

    pesquisa = str(input("Digite o nome que quer pesquisar: "))
    if nome1 == pesquisa or nome2 == pesquisa or nome3 == pesquisa or nome4 == pesquisa:
        print(f"{pesquisa} está entre os cadastrados")
    else:
        print(f"{pesquisa} não está entre os cadastrados")

verific_nome()



#CORREÇÃO

nomes = []

def verifica_se_esta_na_lista(string_):
    global nomes
    if string_ in nomes:
        print(f"o nome {string_} está na lista:\n {nomes}")
    else:
        print(f"o nome {string_} não está na lista:\n {nomes}")  


for i in range(0,4):
    entrada = input(f"{i}: digite um nome: ")
    nomes.append(entrada)

ultima_entrada = input("Agora digite um nome para ver se está na lista: ")

verifica_se_esta_na_lista(ultima_entrada)