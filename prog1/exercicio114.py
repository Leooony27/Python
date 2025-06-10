import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.youtube.com')
except urllib.error.URLError:
    print ("Deu ERRO! O site não está acessível no momento.")
else:
    print ("Tudo Ok.Você acessou o site com sucesso!")
#Print usado para ver o código HTML do site pesquisado.
    #print (site.read())
