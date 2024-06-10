'''
def dizer_ola():
    print("Olá Mundo!")

dizer_ola()
'''

x = 10

def imprime_x(): #variável é global(fora do bloco) então mesmo não na mesma linha é possivel acessá-la
    print(x)

imprime_x()
print(x)

def imprime_y(): #variável é local(dentro do bloco) então se não for na mesma linha não é possivel acessá-la
    y = 20
    print(y)

print(y)