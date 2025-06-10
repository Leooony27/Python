#CALCULADOR DE MAQUINA DE PAGAMENTO
from time import sleep
print ("\033[0;37;40m{:=^40}\033[m".format(" \033[0;36;40mLOJA DO BIG\033[m "))

preco = float(input("Preço das compras \033[0;32;40mR$\033[m"))

print('''\033[0;33;40mFORMAS DE PAGAMENTO\033[m
\033[0;32;40m[ 1 ]\033[m Á vista \033[0;32;40mdinheiro\033[m ou \033[0;32;40mpix\033[m
\033[0;32;40m[ 2 ]\033[m Á vista \033[0;32;40mcartão\033[m
\033[0;32;40m[ 3 ]\033[m 2x no \033[0;32;40mcartão\033[m 
\033[0;32;40m[ 4 ]\033[m 3x ou mais no \033[0;32;40mcartão\033[m''')

opcao = int(input("Qual será a opção de \033[0;33;40mpagamento?\033[m "))
print ("\033[0;33;40mVERIFICANDO FORMA DE PAGAMENTO!\033[m")
sleep(1)
print ("\033[0;33;40mAGUARDE...\033[m")
sleep(2)
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print ("\033[0;37;40m-=-\033[m" * 20)
    print ("\033[0;32;40mOBRIGADO PELA COMPRA, VOLTE SEMPRE!\033[m")
    print ("\033[0;37;40m-=-\033[m" * 20)

elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print ("\033[0;37;40m-=-\033[m" * 20)   
    print ("\033[0;32;40mOBRIGADO PELA COMPRA, VOLTE SEMPRE!\033[m")
    print ("\033[0;37;40m-=-\033[m" * 20)

elif opcao == 3:
    total = preco 
    parcela = total / 2 
    print ("Sua compra será \033[0;33;40mPARCELADA\033[m em 2x de \033[0;32;40R${:.2f}\033[m".format(parcela))
    print ("\033[0;37;40m-=-\033[m" * 20)   
    print ("\033[0;32;40mOBRIGADO PELA COMPRA, VOLTE SEMPRE!\033[m")
    print ("\033[0;37;40m-=-\033[m" * 20)

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input("Quantas \033[0;33;40mparcelas?\033[m "))
    parcela = total / totparc
    print("Sua compra será \033[0;33;40mPARCELADA\033[m em {}x de \033[0;32;40R${:.2f}\033[m COM JUROS".format(totparc, parcela))
    print ("\033[0;37;40m-=-\033[m" * 20)    
    print ("\033[0;32;40mOBRIGADO PELA COMPRA, VOLTE SEMPRE!\033[m")
    print ("\033[0;37;40m-=-\033[m" * 20)

else:
    total = preco
    print ("\033[0;31;40mOPÇÃO INVÁLIDA\033[m. Tente novamente mais tarde!")
    print ("\033[0;31;40mO PAGAMENTO NÃO FOI EFETUADO COM SUCESSO!\033[m")

print ("Sua compra de \033[0;32;40mR${:.2f}\033[m vai custar \033[0;32;40mR${:.2f}\033[m no final".format(preco, total))

