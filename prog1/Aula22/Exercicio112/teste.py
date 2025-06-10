#import moeda
from utilidadescev.moeda import moeda
from utilidadescev.dado import dado

p = dado.leiaDinheiro ("Digite o preço: ")   
moeda.resumo(p, 20 , 12)