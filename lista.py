#1 
aves = ["galinha", "pelicano","canário", "tucano", "urubu", "beija-flor"]
print ("#1 Lista aves:",aves)
#2 POP
aves.pop(-1) #remove um índice da lista 
print ("#2 Remove o item beija-flor:",aves)
#3 APPEND
aves.append("Rolinha") #adiciona esse valor no final da lista
print ("#3 Adiciona o item Rolinha no final:",aves)
#4 INSERT
aves.insert(0,"falcão") #insere esse valor em qualquer índice
print ("#4 Adiciona falcão no índice 0:",aves)
#5 REMOVE
aves.remove("pelicano") #remove um índice
print ("#5 Remove o item pelicano:",aves)
#6 SORT
aves.sort() #Ordena a lista em ordem crescente
print ("#6 Ordena de forma crescente (melhor com números):", aves)
#7 REVERSE
aves.reverse() #inverte a lista
print ("#7 Inverte a lista:",aves)
#8 ATRIBUIR VALOR A UM ÍNDICE
aves[0] = "sabiá" # atribui um valor para um índice
print ("#8 Atribui ao índice 0(urubu) o valor (sabiá):",aves)
#9 MOSTRAR COMPRIMENTO DA LISTA
print("#9 Mostra o comprimento da lista:", len(aves)) # Mostra o comprimento da lista 
#10 VERIFICAR SE ELEMENTO ESTÁ NA LISTA
if 4 in aves:
    print("4 está na lista.")  # verifica se um elemento está na lista ou não
