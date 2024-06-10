
numero_1 = int(input("Escreva o primeiro número: "))
print("O 1 número escolhido é o", numero_1)
numero_2 = int(input("Escreva o segundo número: "))
print("O 2 número escolhido é o", numero_2)
if numero_1 > numero_2:
    print(numero_1, ">", numero_2, ", O maior é o", numero_1)
elif numero_1 == numero_2:
    print(numero_1, "=", numero_2,"Os dois são iguais.")
else:
    print(numero_1, "<", numero_2,"O maior é o", numero_2)
