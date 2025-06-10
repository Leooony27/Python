contatos = {
    "Maria": "\033[0;32;40m1234-5678\033[m",
    "João": "\033[0;32;40m8765-4321\033[m",
    "Ana": "\033[0;32;40m1357-2468\033[m"}

for nome, numero in contatos.items():
    print("Nome: {}, Telefone: {}".format(nome, numero))
