#EXTRAINDO DADOS DE UMA LISTA
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
numeros.sort(reverse=True)
print ("-" * 50)
print (f"Você digitou {len(numeros)} elementos.")
print ("-" * 50)
print (f"Os valores em ordem decrescdente sao {numeros}")
print ("-" * 50)
if 5 in numeros:
    print ("O valor 5 está na lista.")
else:
    print ("O valor 5 não está na lista.")
