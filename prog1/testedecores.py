nome = str(input("Digite seu nome: "))
cor = {"limpa":"\033[m",
        
         "branco":"\033[0;30;40m",
        
         "vermelho":"\033[0;31;40m",
        
         "verde":"\033[0;32;40m",
        
         "amarelo":"\033[0;33;40m",
         
         "azul":"\033[0;34;40m",
         
         "rosa":"\033[0;35;40m",
         
         "ciano":"\033[0;36;40m",
         
         "cinza":"\033[0;37;40m"}

print ("Fala tu , prazer em te comer {}{}{}!".format(cor["azul"], nome , cor["limpa"]))

