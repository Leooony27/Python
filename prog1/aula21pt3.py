#ESCOPO DE VARIAVEIS
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print (f"Na função teste , a vale {a}")
    print (f"Na função teste , b vale {b}")
    print (f"Na função teste , c vale {c}")
#ESCOPO LOCAL
#======================================================================#
#Programa principal
a = 5
teste(a)
print (f"No programa principal, a vale {a}")
#print (f"No programa principal, b vale {b}")
#print (f"No programa principal, c vale {c}")
#ESCOPO GLOBAL
#======================================================================#