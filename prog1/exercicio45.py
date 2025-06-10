#JOGO DE PEDRA, PAPEL E TESOURA
from time import sleep
from random import randint

itens = ("Pedra", "Papel", "Tesoura")

computador = randint (0, 2)
print ("\033[0;36;40m=-=\033[m" * 15)
print ('''\033[1;32;42mSuas opções são:\033[m
\033[0;32;40m[ 0 ]\033[m \033[1;30;40mPEDRA\033[m
\033[0;33;40m[ 1 ]\033[m \033[1;30;40mPAPEL\033[m 
\033[0;31;40m[ 2 ]\033[m \033[1;30;40mTESOURA\033[m''')

print ("\033[0;36;40m=-=\033[m" * 15)
jogador = int(input("Qual é a sua \033[0;32;40mjo\033[m\033[0;33;40mga\033[m\033[0;31;40mda?\033[m "))
print ("\033[0;32;40mJÔ\033[m")
sleep(1)
print ("\033[0;33;40mKEN\033[m")
sleep(1)
print ("\033[0;31;40mPO!\033[m")
print ("\033[0;36;40m-=-\033[m" * 15)
print ("\033[0;31;40mComputador\033[m jogou {}".format(itens[computador]))
print ("\033[0;32;40mJogador\033[m jogou {}".format(jogador))
print ("\033[0;36;40m-=-\033[m" * 15)

if computador == 0:
    if jogador == 0:
        print ("\033[0;33;40mEMPATOU!\033[m")
    elif jogador == 1:
        print ("\033[0;32;40mVOCE VENCEU \033[0;32;40m!\033[m\033[0;33;40m!\033[m\033[0;31;40m!\033[m")
    elif jogador == 2:
        print ("\033[0;31;40mYOU LOST!\033[m")
    else:
        print ("\033[0;31;40mJOGADA INVÁLIDA\033[m")
elif computador == 1:
    if jogador == 0:
        print ("\033[0;31;40mYOU LOST!\033[m")
    elif jogador == 1:
        print ("\033[0;33;40mEMPATOU!\033[m")
    elif jogador == 2:
        print ("\033[0;32;40mVOCE VENCEU \033[0;32;40m!\033[m\033[0;33;40m!\033[m\033[0;31;40m!\033[m")
    else:
        print("\033[0;31;40mJOGADA INVÁLIDA\033[m")

elif computador == 2:
    if jogador == 0:
        print ("\033[0;32;40mVOCE VENCEU \033[0;32;40m!\033[m\033[0;33;40m!\033[m\033[0;31;40m!\033[m")
    elif jogador == 1:
        print ("\33[0;31;40mYOU LOST!\033[m")
    elif jogador == 2:
        print ("\033[0;33;40mEMPATOU!\033[m")
    else:
        print ("\033[0;31;40mJOGADA INVÁLIDA\033[m")