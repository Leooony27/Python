def fatorial(num):
    f = 1
    for c in range (num , 0, -1):
        f *= c 
    return f
n = int(input("Digite um numero: "))
print (f"O fatorial de {n} é igual a {fatorial(n)}")