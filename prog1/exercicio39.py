from datetime import date 
atual = date.today().year
nasc = int(input("Digite seu ano de \033[0;31;40mNASCIMENTO :\033[m"))
idade = atual - nasc 
print ("Quem nasceu em {} tem {} anos em {}.".format(nasc , idade , atual))
if idade == 18: 
    print ("Voce tem que se alistar \033[0;31;40mIMEDIATAMENTE\033[m")
elif idade < 18:
    saldo = 18 - idade 
    print ("Voce ainda nao tem 18 anos.Ainda faltam {} anos para o \033[0;32;40mALISTAMENTO militar.\033[m".format(saldo))
    ano = atual + saldo
    print ("Seu \033[0;32;40mALISTAMENTO\033[m sera em {}.".format(ano))
elif idade > 18:
    saldo = idade - 18 
    print ("Voce ja deveria ter se alistado ha {} anos.".format(saldo))
    ano = atual - saldo
    print ("Seu \033[0;32;40mALISTAMENTO\033[m foi em {}.".format(ano))