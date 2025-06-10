#MANIPULACAO DE TUPLAS
lanche = 'Hamburguer', 'Suco','Pizza', 'Pudim' 
#TUPLAS SAO IMUTAVEIS
#print (lanche)
#o for é utilizado como uma repetição.(neste caso como itens. Mas pode ser usado como range também)
for comida in lanche:
    print(f"Eu vou comer {comida}")
print("Comi demais!!!")