class Matematica:

    def __init__(self, numero1 = float, numero2 = float):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(numero1, numero2):
         soma = (numero1 + numero2)
         print("o resultado da soma foi {}".format(soma))

    def subtracao(numero1, numero2):
        subtracao = (numero1 - numero2)
        print("o resultado da subtracao foi {}".format(subtracao))

    def multiplicacao(numero1, numero2):
        multiplicacao = (numero1 * numero2)
        print("o resultado da multiplicacao foi {}".format(multiplicacao))

    def divisao(numero1, numero2):
        recebe = (numero1 / numero2)
        print("o resultado da divisao foi {}".format(recebe))

matematica = Matematica
matematica.soma(2.0, 4.0)
matematica.subtracao(2.0, 4.0)
matematica.divisao(2.0, 4.0)
matematica.multiplicacao(2.0, 4.0)

