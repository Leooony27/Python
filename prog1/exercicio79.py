#VALORES UNICOS EM UMA LISTA UTILIZANDO O .sort()
numeros = lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        lista.append(n)
        print ("Valor adicionado com sucesso...")
    else:
        print ("Valor duplicado! Não vou adiciona-lo...\nDigite outro valor!")
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer adicionar mais um valor ? [S/N] ")).upper().strip()
    if resp == 'N':
        break
lista.sort()
print (f"Os valores digitados foram {numeros}")
