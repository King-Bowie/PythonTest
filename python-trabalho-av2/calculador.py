import numpy as np
opcao=1
while(opcao != 0):
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")
    opcao = int(input("Opção: "))
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if(opcao==1):
        print("Soma: ", np.add(a,b))
    elif(opcao==2):
        print("Subtracao: ", np.subtract(a,b))
    elif(opcao==3):
        print("Multiplicacao: ", np.multiply(a,b))
    elif(opcao==4):
        print("Divisao: ", np.divide(a,b))

