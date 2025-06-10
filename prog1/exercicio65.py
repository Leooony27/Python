#MENOR E MAIOR VALOR
resp = 'S'
soma = quant = media = maior = menor = 0 
while resp in 'S':
    num = int(input("Digite um valor: "))
    soma += num 
    quant += 1 
    if quant == 1:
        maior = menor = num 
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num  
    resp = str(input("Quer continuar ? [S/N] ")).upper().strip()[0]
media = soma / quant 
print ("Voce digitou {} e a media foi {}".format(num, media)) 
print ("O valor maior foi o {} e o menor foi o {}".format(maior, menor))