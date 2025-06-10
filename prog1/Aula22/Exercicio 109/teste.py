import moeda 
p = float(input("Digite o preço: "))
print (f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
print (f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print (f"Aumentando 10% do valor, temos R${moeda.aumentar(p, 10, True)}")
print (f"Diminuindo 10% do valor, temos R${moeda.diminuir(p, 13, True)}")