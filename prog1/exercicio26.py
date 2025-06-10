#Observacoes , o upper foi utilizado para deixar o input em maiusculo para ajudar na resolucao do problema
# o strip foi usado para tirar a contagem de espacos 

frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase.".format(frase.count('A')))
print("A primeira letra A apareceu na posicao {}".format(frase.find('A')+1))
print("A ultima letra A apareceu na posicao {}".format(frase.rfind('A')+1))