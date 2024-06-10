print("programa verifica 3 números informados em ordem decrescente.")

n1 = int(input("numero 1: "))
print (n1)

n2 = int(input("numero 2: "))
print (n2)

n3 = int(input("numero 3: "))
print (n3)

if n1>=n2 and n2>=n3: #1,2,3
    print ("n1 =", n1, "n2 =", n2, "n3 =", n3)
    
elif n1>=n3 and n3>=n2: #1,3,2
    print ("n1 =", n1, "n3 =", n3, "n2 =", n2)
    
elif n3>=n2 and n2>=n1: #3,2,1
    print ("n3 =", n3, "n2 =", n2, "n1 =", n1)
    
elif n3>=n1 and n1>=n2: #3,1,2
    print ("n3 =", n3, "n1 =", n1, "n2 =", n2)
    
elif n2>=n3 and n3>=n1: #2,3,1
    print ("n2 =", n2, "n3 =", n3, "n1 =", n1)
elif n2>=n1 and n1>=n3:#2,1,3
    print ("n2 =", n2, "n1 =", n1, "n3 =", n3)
else:
    print ("Você digitou um número inválido!")
