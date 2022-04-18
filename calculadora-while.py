
opcao=1

while(opcao != 0):
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")

    opcao = int(input("Opção: "))
    a = float(input("Primeiro valor: "))
    b = float(input("Segundo valor: "))

    if(opcao==1):
        print("Soma: ", a + b)
    elif(opcao==2):
        print("Subtracao: ", a - b)
    elif(opcao==3):
        print("Multiplicacao: ", a * b)
    elif(opcao==4):
        print("Divisao: ", a / b)
