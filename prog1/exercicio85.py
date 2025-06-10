cadastro = [[], []]
#pares = []
#impares = []
valor = 0
#Está maneira é usando somente uma única lista para obter outras listas dentro dela.
for c in range (1, 8):
    valor = (int(input(f"Digite o {c}o. valor: ")))
    if valor % 2 == 0:
        cadastro[0].append(valor)
    else:
        cadastro[1].append(valor)
#======================================================================================
#Está maneira é ultilizando 3 listas.
'''for i,v in enumerate(cadastro):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)'''
#=======================================================================================
print ("-=" * 30)
#print (f"Os valores digitados foram: {cadastro}.")
cadastro.sort()
print ("-=" * 30)
cadastro.sort[0]
cadastro.sort[1]
#print (f"A lista em ordem crescente é {cadastro}.")
#pares.sort()
print (f"Os números pares são {cadastro[0]}.")
#impares.sort()
print (f"Os números impares são {cadastro[1]}.")