"""
import random 
numeroadivinha = random.randint (1, 10)
print("O número foi", numeroadivinha)
attempts = 0
guess = None
while guess!= numeroadivinha:
        guess = int(input("Número entre 1 a 10: "))
        if guess == 1 or guess == 2 or guess == 3 or guess == 4 or guess == 5 or guess == 6 or guess == 7 or guess == 8 or guess == 9 or guess == 10:
            attempts += 1 and guess<=10 and guess>=1
            print (" Tentativas:", attempts)

            if guess > numeroadivinha:
                print ("Tente um número menor")

            elif guess < numeroadivinha:
                print ("Tente um número maior")

        else:
            print ("Número ou caractere digitado não disponível")
            print (" Tentativas:", attempts)
 
print("Números de tentativas:", attempts)
"""

lista = ["a","b","c"]
import random
numeroadivinha = random.lista("a","b","c")
print("O número foi", numeroadivinha)