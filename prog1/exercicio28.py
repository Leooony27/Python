from random import randint
from time import sleep
cor = {"limpa":"\033[m",
        
         "branco":"\033[0;30;40m",
        
         "vermelho":"\033[0;31;40m",
        
         "verde":"\033[0;32;40m",
        
         "amarelo":"\033[0;33;40m",
         
         "azul":"\033[0;34;40m",
         
         "rosa":"\033[0;35;40m",
         
         "ciano":"\033[0;36;40m",
         
         "cinza":"\033[0;37;40m"
         }
computador = randint(0, 5)
print("\033[0;34;40m-=-\033[m" * 20)
print("Vou pensar em um \033[0;36;40mNUMERO\033[m entre \033[0;32;40m0\033[m e \033[0;32;40m5\033[m.Tente advinhar...")
print("\033[0;34;40m-=-\033[m" * 20)
jogador = int(input("Em que \033[0;32;40mNUMERO\033[m eu pensei? "))
print("\033[0;35;40m=-=\33[m" * 20)
print("\033[0;33;40mPROCESSANDO O GAME\033[m...")
print("\33[0;35;40m=-=\033[m" * 20)
sleep(2)
if jogador == computador:
    print("\033[0;32;40mPARABENS\033[m,Voce acertou!!!Agora \033[0;31;40foda-se\033[m")
else:
    print("\033[0;31;40mYOU LOST\033[m meu peixe, o \033[0;32;40mNUMERO\033[m que eu pensei foi o {}.\033[0;31;40mTente novamente seu bagre!\033[m".format(computador))
