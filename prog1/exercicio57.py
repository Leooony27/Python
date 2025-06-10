#VALIDACAO DE DADOS

sexo = str(input("Informe seu sexo: [M/F]" )).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados invalidos. Por favor informe seu sexo: ")).strip().upper()
print ("Sexo {} registrado com sucesso.".format(sexo))
idade = int(input("Informe sua idade: "))
print ("Idade registrada com sucesso.")