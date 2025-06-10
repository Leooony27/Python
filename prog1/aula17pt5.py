#CONTINUAÇÃO DE VARIÁVEIS COMPOSTAS 2.0
dados = []
dados.append ("Luffy")
dados.append (25)
print (dados[0])
print (dados[1])

pessoas = [["Pedro",25], ["Maria",19], ["Joao",32]]
pessoas.append(dados[:])
print (pessoas[0][0])
print (pessoas[1][1])
print (pessoas[2][0])
print (pessoas[1])