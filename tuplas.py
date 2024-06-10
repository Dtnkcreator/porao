'''
tupla_numeros = (1,2,3,4,5)
soma = sum(tupla_numeros)
produto = 1

for num in tupla_numeros:
    produto = produto*soma

'''
'''
pessoa = {"nome": "Carlos", "idade": 40,"cidade": "Rio de Janeiro"}

for chave, valor in pessoa.items():
    print(chave + ":", valor)

'''

dicio = {"chave1": "bola", "chave2": "chocolate", "chave3": 50}
valor = dicio.get("chave2")
print(valor)

capitais = {
    ("Brasil", "Goiás"): "Goiânia",

}

for capital in capitais:
    print(f"região:{capital["Brasil"]})