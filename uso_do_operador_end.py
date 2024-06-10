
print("Qual é sua condição?")
print("1) idoso")
print("2) gestante")
print("3) cadeirante")
print("4) nenhuma das opções")
qual_publico_ele_esta =(int(input("Qual é sua condição de 1 a 4?")))
if qual_publico_ele_esta == 1 or qual_publico_ele_esta == 2 or qual_publico_ele_esta == 3:
    print("você está na fila de prioridade.")
else:
    print("você não está na fila de prioridade.")
