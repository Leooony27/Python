#TENTE ADVINHAR O NUMERO V.2
from time import sleep 
from random import randint
computador = randint(0, 20)
print ("Olá meu peixe, sou seu computador...")
sleep(0.5)
print ("Acabei de pensar em um número entre 0 e 20")
sleep(0.8)
print ("Tente adivinhar...")
sleep(1)
acertou = False
sorte = 0
while not acertou:
    jogador = int(input("Digite um número de 0 a 20 para tentar a sorte: "))
    sorte += 1
    if jogador == computador:
        acertou = True 
    else:
        if jogador < computador:
            print ("Cague mais...")
        elif jogador > computador:
            print ("Cague menos...")
print (f"Acertou com {sorte} cagadas. Parabéns")

