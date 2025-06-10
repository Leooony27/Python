from time import sleep

def contador(i,f,p):
    """""
        >Faz uma contagem e mostra na tela.
        :param i: inicio da contagem
        :param f: fim da contagem
        :param p: passo de contagem
        :return:sem retorno
    """""
    c = i 
    while c <= f:
        print (f'{c}', end = "..")
        c += p
    print ("FIM")


contador (0, 100 , 10)
help(contador)
