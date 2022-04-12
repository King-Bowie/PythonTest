
opcao=1

while(opcao != 0):
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")

    opcao = int(input("Opção: "))

    if(opcao==1):
        a = float(input("Primeiro valor: "))
        b = float(input("Segundo valor: "))
        print("Soma: ", a + b)
    elif(opcao==2):
        a = float(input("Primeiro valor: "))
        b = float(input("Segundo valor: "))
        print("Subtracao: ", a - b)
    elif(opcao==3):
        a = float(input("Primeiro valor: "))
        b = float(input("Segundo valor: "))
        print("Multiplicacao: ", a * b)
    elif(opcao==4):
        a = float(input("Primeiro valor: "))
        b = float(input("Segundo valor: "))
        print("Divisao: ", a / b)