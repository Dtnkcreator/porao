lista_livro = [
    {"titulo":"Dom Quixote", "autor":"Miguel de Cervantes", "ano de Lançamento": 1612,"favorito": 0},
    {"titulo":"Um Conto de Duas Cidades", "autor":"Charles Dickens", "ano de Lançamento": 1859,"favorito": 0},
    {"titulo":"Pequeno Príncipe", "autor":"Antonine de Saint-Exupéry", "ano de Lançamento": 1943,"favorito": 0}     
]

'''
livro_fav = lista_livro[2] #cria uma variável que acessa a lista de dicionários 

livro_fav["favorito"] = 1 # favorito do índice 2(Pequeno Príncipe) se torna 1

lista_livro[2] = livro_fav #a variável de ser favorito se torna igual ao índice 2

print(lista_livro)

'''

#Usando FOR

for livro in lista_livro: 
    if livro["titulo"] == "O Pequeno Príncipe": #se o 
        livro["favorito"] = 1

print(livros)
