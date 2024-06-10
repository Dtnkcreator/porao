print ("Escreva a Disciplina da prova do aluno: ")
print ("1. Português, 2.Matemática e 3.Inglês")
materia = int(input())
print ("A disciplina escolhida foi", materia)
if materia == 1:
    print("A disciplina é português.")
elif materia == 2:
    print("A disciplina é matemática.")
elif materia == 3:
    print("A disciplina é inglês.")
else:
    print("A disciplina escolhida é inválida, tente novamente.")
    
nota = float(input("Digite a nota que o aluno tirou de 0 a 10.0: "))
print("a nota é", nota)
if nota < 6.0 and nota >= 0 and not nota == -0:
    print("o aluno tirou nota F!")
elif 7 >= nota >= 6.0:
        print("o aluno tirou nota D!")
elif 8.0 >= nota > 7.0:
        print("o aluno tirou nota C!")
elif 9.0 >= nota > 8.0:
        print("o aluno tirou nota B!")
elif 10 >= nota > 9.0:
        print("o aluno tirou nota A!")
else:
    print("Nota inválida, escreva novamente com um número entre 0 e 10.0.")
