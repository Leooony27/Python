num = [8, 2, 5, 4, 9, 3, 0]
#O comando .sort é utilizado para arrumar a lista de forma cronológica,
num.sort()
#O comando .sort(reverse=True) ordena os valores de forma reversa.
num.sort(reverse=True)
num.insert(2, 0)
num.pop(1)
if 7 in num:
    num.remove(7)
else:
    print("Não encontrei o número 7")
print (num)
print (f"Essa lista tem {len(num)} elementos.")