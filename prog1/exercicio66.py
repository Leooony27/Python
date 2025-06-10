num = soma = cont = 0
cont = 0
num = int(input("Digite um numero: [999 to stop] "))
while num != 999:
    soma += num 
    num = int(input("Digite um numero: [999 to stop ]"))
    cont += 1
print (f"{cont} numeros foram digitados. E a soma entre eles foi {soma}")