#VARIÁVEIS COMPOSTAS - DICIONÁRIOS
#Os dicionarios sao identificados por "{}" 
dados = dict()
dados = {"nome":"Pedro", "idade":25}
dados["sexo"]="M"
print (dados["nome"])
print (dados["sexo"])
print (dados.values())
print (dados.keys())
print (dados.items())
for k,v in dados.items():
    print (f"O {k} é {v}")