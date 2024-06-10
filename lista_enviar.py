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
print("Ordem inversa: ", lista)
