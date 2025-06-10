#JOGO DE DADOS EM PYTHON
from random import randint
from time import sleep
from operator import itemgetter
jogo = { "Jogador 1": randint(1, 6),
        "Jogador 2": randint (1, 6),
        "Jogador 3": randint (1, 6),
        "Jogador 4": randint (1, 6)}
rank = dict()
print ("-=" * 30)
print ("Valores sorteados: ")
print ("-=" * 30)
for k, v in jogo.items():
    print (f"{k} tirou: {v} no dado.")
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print ("-=" * 30)
sleep(1)
print ("     <TABELA DE RANKING>     ")
sleep(1)
for i, v in enumerate(rank):
    print (f"{i+1}o lugar: {v[0]} com {v[1]}.")
    sleep(0.5)

