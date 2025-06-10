#CADASTRO DE JOGADOR DE FUTEBOL
jogador = dict()
partidas = list()
jogador ["nome"] = str(input("Nome do Jogador: "))
tot = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))
for c in range (0, tot):
    partidas.append(int(input(f"  Quantos gols na partida {c+1}a?")))
jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)
#1a forma de usar o print.
print ("-=" * 30)
print (jogador)
#2a forma de usar o print.
print ("-=" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
#3a forma de usar o print, é a melhor e mais complexa.THE BESST!
print ("-=" * 30)
print (f"O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.")
for i, v in enumerate(jogador["gols"]):
    print (f"  => Na partida {i+1}a, fez {v} gols.")
print (f"Foi um total de {jogador["total"]} gols.")