#JOGO DO IMPAR OU PAR
from random import randint 
v = 0
while True:
    jogador = int(input("Digite um número: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print (f"Você jogou {jogador} e o computador {computador}. Total de {total}")
    if tipo == 'P':
        if total % 2 == 0:
            print ("VOCE GANHOU! ")
            v += 1 
        else: 
            print ("VOCE PERDEU! ")
            break 
    elif tipo == 'I':
        if total % 2 == 1:
            print ("VOCE GANHOU! ")
            v += 1 
        else:
            print ("VOCE PERDEU! ")
            break
    print ("Vamos jogar novamente...")
print (f"GAME OVER! Você venceu do computador {v} vezes.")