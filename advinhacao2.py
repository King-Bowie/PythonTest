import random
def jogar():
    print("************************************")
    print("Bem vindo no jogo de adivinhação!")
    print("************************************")

    numero_sereto = random.randrange(1,101) # random (normal) gera um numero entra 0.0 ate 1.0
    total_de_tentativas = 0                 #random randrange faz com que ele faça um numerop ate o outro (100 nesse caso)101 nao vai ter

    pontos = 1000


    print("qual o nivel de dificuldade?")
    print("(1)Facil (2)Medio (3)Dificil")
    nivel = int(input("difina seu nivel: "))
    if(nivel == 1 ):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 3

    for rodadas in range(1, total_de_tentativas +1): #precisa ter +1 no limite pra chegar no 3 certo
        print("tentativa {} de {}" .format(rodadas, total_de_tentativas)) #o nome disso é string interpolation
        chute_str = input("Digite um número entre 1 e 100 : ")
        print("Voce digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = numero_sereto == chute
        maior = chute > numero_sereto
        menor = chute < numero_sereto

        if (acertou) :
            print ("Você acertou e fez {} pontos".format(pontos))
            break
        else :
            if(maior):
                print("Você errou! o seu chute foi maior que o numero secreto")
            elif(menor):
                print("Você errou! o seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_sereto - chute) #exemplo: 40-20 = 20 pontos perdidos
            pontos = pontos - pontos_perdidos   #abs nao deixa o numero ser negativo



    print(("Fim do jogo!!"))

    #for rodada in range(1,10,2):  nos parenteses é 1=o começo, 10=o limite, 2=a quantidade de casas que vai ser somada
            #print(rodada)
if(__name__ == "__main__"):#faz com que seja lido pelo terminal de forma separada
    jogar()