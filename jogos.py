import forca
import advinhacao2

def escolhe_jogo():
    print("************************************")
    print("*********Escolha seu jogo!**********")
    print("************************************")

    print("(1) forca (2) Advinhação")

    jogo = int(input("qual jogo? "))

    if (jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando advinhação")
        advinhacao2.jogar()
if (__name__ == "__main__"): #faz com que seja lido pelo terminal de forma separada
    escolhe_jogo()
