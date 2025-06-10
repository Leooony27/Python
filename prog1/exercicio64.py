#TRATANDO VARIOS VALORES
num = cont = soma = 0 
num = int(input("Digite um número [999 para parar]: "))
while num != 999:    
    soma += num
    #cont = cont + 1
    cont += 1 
    num = int(input("Digite um número [999 para parar]: "))
print ("Voce digitou {} números e a soma entre eles foi {}.".format(cont, soma))
