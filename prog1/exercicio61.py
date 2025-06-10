#PROGESSAO ARITIMETICA V2
from time import sleep
print ("Gerador de PA")
print ("-=-" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao da PA: "))
termo = primeiro 
cont = 1 
print ("Progredindo...")
sleep(1)
while cont <= 10:
    print ("{} > ".format(termo), end="")
    termo = termo + razao 
    cont += 1 
print ("FIM.")