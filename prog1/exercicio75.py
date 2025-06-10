num = (int(input("Digite um numero: "))),(int(input("Digite um numero: "))),(int(input("Digite um numero: "))),(int(input("Digite um numero: ")))
print (f"Voce digitou os valores {num}.")
print (f"O valor 9 apareceu {num.count(9)} vezes.")
if 3 in num:
    print (f"O valor 3 apareceu na {num.index(3)+1} vezes.")
else:
    print ("O valor 3 nao foi encontrado.")
for n in num:
    if n % 2 == 0:
        print (n, end = "")