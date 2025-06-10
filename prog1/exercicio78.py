valores = []
for cont in range (0, 5):
    valores.append(int(input("Digite um valor: ")))
print (f"Os valores que você digitou foram {valores}.")
for c,v in enumerate(valores):
    print (f"Na posição {c} encontrei o valor {v}.")
print (f"O maior valor digitado foi o {max(valores)}.")
print (f"O menor valor digitado foi o {min(valores)}.")