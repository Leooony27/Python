#TABUADA V2.0
num = int(input("\033[0;32;40mDigite um numero para ver sua tabuada:\033[m "))
for c in range(1, 11):
    print ("\033[0;33;40m-=-\033[m" * 5)
    print ("{} X {:2} = \033[0;32;40m{}\033[m".format(num, c, num*c))