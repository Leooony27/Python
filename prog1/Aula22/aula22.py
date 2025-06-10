#MÓDULOS E PACOTES (utiliza-se bastante funções)
#Modularização() é usada para sistemas maiores (Dividir programas grandes, aumentar a legibilidade do programa e facilitar a manutenção do código)
import defs
'''from defs import fatorial
from defs import dobro
from defs import triplo'''

'''def fatorial(n):
    f = 1
    for c in range (1, n+1):
        f *= c
    return f

def dobro(n):
    return n*2

def triplo(n):
    return n*3'''


num = int(input("Digite um valor: "))
fat = defs.fatorial(num)
print (f"O fatorial de {num} é {defs.fatorial(num)}")
print (f"O dobro de {num} é {defs.dobro(num)}")
print (f"O triplo de {num} é {defs.triplo(num)}")
print (f"Aumentando 10 na soma de {num} é {defs.aumentar(num)}")
print (f"Diminuindo o {num} sobra {defs.diminuir(num)}")