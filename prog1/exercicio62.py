#PROGRESSAO ARITIMETICA V3
from time import sleep
print ("Gerador de PA")
print ("-=-" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao da PA: "))
termo = primeiro 
cont = 1 
total = 0
mais = 10
print ("Progredindo...")
sleep(1)
while mais != 0:
    total = total + mais
    while cont <= total:
        print ("{} > ".format(termo), end="")
        termo = termo + razao 
        cont += 1 
    print ("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print ("Progressão finalizada com {} termos finalizados.".format(total))