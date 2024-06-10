'''

list = [1, 2, 3]
list2 = None
list2 = list.copy()
list2.append(4)
print(list2)
print(list)

#LISTA DOS NOMES

nomes = ["Ana", "Breno", "Carlos", "Diego"]

residentes_novos = nomes.copy()
residentes_novos.insert(4,"Eduardo")

print("A lista inicial dos nomes é:", nomes, "e a lista dos residentes novos é:", residentes_novos)

'''


#exemplo
for nome in nomes:
    print(nome)

#cores
cores = ["vermelho", "verde", "azul"]
for cor in cores:
    print(cor)