'''

textao = "Lorem ipsum dolor sit amet$ consectetur adipiscing elit$ sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam$ quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident$ sunt in culpa qui officia deserunt mollit anim id est laborum."

print("\nAntes:\n", textao, "\n")

textao = textao.replace('$',',')

print("Depois:\n", textao, "\n")



a = ["apple", "banana"]
b = ["pineapple", "pear", "watermelon"]
for item in b:
    a.append(item)
print(a)

a.append(b)
#no final das contas, foi inserido um novo item no final da lista A e o valor desse novo item é a lista de B como podemos ver no console
print(a)



numeros = [1,2,3,4,5,6,7,8,9,10]
numeros2 = numeros[5:11]
x = numeros2[0:2]
print(numeros2)
print(numeros)
print(x)

dias_semana = ["Segunda", "Terça", "Quarta", "Quinta","Sexta"]

dia = str(input("Escreva o dia: "))
if dia in dias_semana:
    print("Sim, está na lista!")
else:
    print("Não está!")



nomes = ["joao","maria","pedro"]
animais_de_estimacao = ["cachorro","gato","pato"]

for nome in nomes:
    for animal in animais_de_estimacao:
        print(nome,animal)

'''