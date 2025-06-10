#TABUADA V3
while True:
    print ("\033[0;33;40m-=-\033[m" * 15)
    num = int(input("Voce quer ver a tabuada de qual valor? "))
    if num < 0:
        break
    print ("\033[0;33;40m-=-\033[m" * 15)
    for c in range (1, 11):
        print ("\033[0;33;40m-=-\033[m" * 5)
        print (f"{num} X {c} = {num*c}")
print ("\033[0;32;40m-=-\033[m" * 15)
print ("Programa finalizado com sucesso. Volte sempre!")
