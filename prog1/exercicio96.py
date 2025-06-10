#FUNÇÃO QUE CALCULA ÁREA
def area(larg, comp):
    a = larg * comp
    print(f"A área de um terreno {larg} x {comp} é de {a}m²")

#PROGRAMA PRINCIPAL
print ("Controle de Terrenos")
print ("=" * 20)
l = float(input("LARGMUA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l, c)