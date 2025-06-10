from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor:"))
opcao = 0 
while opcao != 5:
    print ('''[ 1 ] Somar 
[ 2 ] Multiplicar 
[ 3 ] Saber o maior valor
[ 4 ] Novos números 
[ 5 ] Sair do programa''')
    opcao = int(input(">>>Qual é sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print ("A soma de {} + {} é {}".format(n1, n2, soma))
    elif opcao == 2:
        vzs = n1 * n2
        print ("O resultado da multiplicação é {}".format(vzs))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print ("Entre {} é {} , o maior numero é o {}".format(n1 ,n2, maior))
    elif opcao == 4:
        print ("Informe os numeros novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))

    elif opcao == 5:
        print ("Finalizado com sucesso!")

    else:
        print ("Opção inválida. Tente novamente!")
    print ("-=-" * 15)
sleep(2)
print ("Programa finalizado! Volte sempre!")