lista_livro = [
    {"titulo":"Dom Quixote", "autor":"Miguel de Cervantes", "ano de Lançamento": 1612,"favorito": 0},
    {"titulo":"Um Conto de Duas Cidades", "autor":"Charles Dickens", "ano de Lançamento": 1859,"favorito": 0},
    {"titulo":"Pequeno Príncipe", "autor":"Antonine de Saint-Exupéry", "ano de Lançamento": 1943,"favorito": 0}     
]


livro_fav = lista_livro[2] 

livro_fav["favorito"] = 1 

lista_livro[2] = livro_fav 
print(lista_livro)