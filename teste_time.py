

def timer():
    import time

    minutos = 5
    segundos_iniciais = minutos*60
    segundos = 0

    for i in range(segundos_iniciais):
         
        while segundos < 0 and minutos > 0:
            minutos -= 1
            segundos += 60

        if segundos >= 0:
            time.sleep(0.1)
            print(f"{minutos} : {segundos}")
            segundos = segundos-1
    print(f"{minutos} : {segundos}")
    if segundos == 0 and minutos == 0:
            print("Acabou o tempo!")

timer()




'''
import time

segundos = 0
minutos = 1

#minutos = int(input("quantos minutos você deseja esperar?"))
#segundos = int(int("e agora, quantos segundos?"))
print(f"{minutos}:{segundos}")
for i in range((minutos*60)+segundos):
    time.sleep(0.1)  
   
    if minutos >0:
        if segundos >0:
            segundos = segundos-1
        else:
            segundos = 59
            minutos = minutos-1
    elif minutos ==0 and segundos>0:
         segundos = segundos-1
    else:
        print("erro inesperado")

    print(f"{minutos}:{segundos}")
    if minutos ==0 and segundos == 0:
            print("acabou")
'''