#DIVIDINDO VALORES EM VARIAS LISTAS 
num = list()
pares = list()
impares = list()

while True:
    num.append(int(input("Digite um numero: ")))
    resp = str(input("Quer cotinuar ? [S/N]")).upper().strip()
    if resp in 'Nn':
        break 
for i,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print ("-=-" * 25)
print (f"A lista completa é {num}")
print (f"A lista de numeros pares são {pares}")
print (f"A lista de numeros ímpares são {impares}")