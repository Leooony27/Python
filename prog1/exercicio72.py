from cores import Cores

cont = ('zero', 'um', 'dois', 'tres',
'quatro', 'cinco', 'seis', 'sete', 'oito',
'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
'quinze','dezesseis', 'dezessete', 'dezoito' , 'dezenove',
'vinte')

while True:
    resp = ' '
    while True:
        num = int(input("Digite um numero entre 0 e 20: "))
        if 0 <= num <= 20:
            break 
        print (Cores.colorir("Tente novamente. ", Cores.VERMELHO))
    print (f"Voce digitou o numero {cont[num]}")
    while resp not in 'SN':
        resp = str(input(Cores.colorir("Deseja testar outro numero? [S/N]", Cores.AMARELO))).strip().upper()[0]
    if resp == 'N':
        break
print (Cores.colorir("Programa finalizado! Obrigado pelo teste.", Cores.VERDE))