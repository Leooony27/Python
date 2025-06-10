c = ('\033[m',
     '\033[0;30;41m')

def ajuda (com):
    help (com)

def titulo(msg, cor):
    tam = len (msg) + 4
    print ('=' * tam)
    print (f'   {msg}')
    print ('=' * tam)



#PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo ('SITEMA DE AJUDA PyHELP')
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    titulo (' ATÉ LOGO! ')