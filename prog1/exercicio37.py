#Conversor de Base Numericas 
from time import sleep
num = int(input("\033[33;40mDigite\033[m um \033[32;40mnúmero\033[m inteiro: "))
print ('''\033[0;36;40mEscolha uma das bases para a conversão:\033[m
\033[33;40m[ 1 ]\033[m Converter para \033[32;40mBINÁRIO\033[m
\033[33;40m[ 2 ]\033[m Converter para \033[32;40mOCTAL\033[m
\033[33;40m[ 3 ]\033[m Converter para \033[32;40mHEXADECIMAL\033[m''')
opcao = int(input("\033[36;30mEscolha uma opção:\033[m"))
print("\033[0;32;40m-=-\033[m" * 20)
print("\033[0;33;40mConvertendo seu número...\033[m")
print ("\033[0;32;40m-=-\033[m" * 20)
sleep(2)
if opcao == 1:
    print ("\033[32;40m{}\033[m convertido para \033[0;33;40mBINÁRIO\033[m é igual a \033[32;40m{}\033[m".format(num, bin(num)[2:]))
elif opcao == 2:
    print ("\033[32;40m{}\033[m convertido para \033[0;33;40mOCTAL\033[m é igual a \033[32;40m{}\033[m".format(num, oct(num)[2:]))
elif opcao == 3:
    print ("\33[32;40m{}\033[m convertido para \033[0;33;30mHEXADECIMAL\033[m é igual a \033[32;40m{}\033[m".format(num, hex(num)[2:]))
else:
    print ("\033[0;31;40mSeu animal essa opcao nao existe...\033[m")