#VARIÁVEIS COMPOSTAS | AULA DE LISTAS (diferente das tuplas as listas sao mutáveis, ou seja é possivel adicionar, editar e remover algo da lista.)

cardapio = ['Hamburguer' , 'Refrigerante', 'Pizza', 'Pudim']

#O comando .append adiciona um novo item pra dentro da lista(porem ele vai para o final dela.) 
cardapio.append ('Cookie')

#O comando .insert isere um novo item para dentro da lista(podem ele pode ser escolhido a posição em que vai ficar na lista.)
cardapio.insert(0 ,'Cachorro Quente')

#O comando del serve para excluir algo de dentro da lista.(Para usar o "del" temos que colocar o numero entre colchetes.)
del cardapio [3]

#O comando .pop tambem pode ser usado para deletar algo da lista. Ele geralmente é usado para eliminar o ultimo da lista.
cardapio.pop(4)

#O comando .remove tambem deleta algo no final da lista, porem para funcionar ele tem que ser digitado o nome do produto da lista.
if 'Hamburguer' in cardapio:
    cardapio.remove('Hamburguer')
print (cardapio)  