#from sistema2 import menu, cabecalho
from sistema2 import *
from time import sleep
from arquivo.arquivo import *

arq = "teste.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu (["Ver pessoas cadastradas" , "Cadastrar nova pessoas", "Sair do Sistema"])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
        #Opção de sair do sistema.
    elif resposta == 3:
        cabecalho("\033[32mSaindo do sistema...Até logo\033[m")
        break
    else:
        print ("\033[31mERRO! Digite uma opção válida\033[m")
    sleep(0.7)

