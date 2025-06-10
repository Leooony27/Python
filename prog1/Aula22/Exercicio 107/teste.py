import moeda 
p = float(input("Digite o preço: "))
print (f"A metade de {p} é {moeda.metade(p)}")
print (f"O dobro de {p} é {moeda.dobro(p)}")
print (f"Aumentando 10% do valor, temos R${moeda.aumentar(p, 10)}")
print (f"Diminuindo 10% do valor, temos R${moeda.diminuir(p, 10)}")