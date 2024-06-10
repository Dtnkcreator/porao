laranjaspedro = 10
laranjasretiradas = int(input("Quantas laranjas seram retiradas de Pedro?"))

laranjasquesobraram = laranjaspedro - laranjasretiradas

if laranjasquesobraram > 5:
    print ("Pedro ficou feliz com a quantia de laranjas.")
elif laranjasquesobraram == 5:
    print ("Pedro está satisfeito com a quantia de laranjas.")
else:
    print ("Pedro ficou triste com a quantia de laranjas.")

