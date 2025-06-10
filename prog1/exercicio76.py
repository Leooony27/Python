#LISTA DE PREÇOS COM TUPLAS
from random import randint

produtos = ('Lapis', 1.50,
            'Caneta', 2,
            'Caderno', 20,
            'Borracha', 2,
            'Apontador', 5,
            'Cola', 7,
            'Compasso', 15,
            'Mochila', 200,
            'Livro', 30,
            'Estojo', 50)
print ("-" * 40)
print (f"{"LISTAGEM DE PREÇOS":^40}")
print ("-" * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print (f"{produtos[pos]:.<30}", end= '')
    else:
        print (f"R${produtos[pos]:>7.2f}")