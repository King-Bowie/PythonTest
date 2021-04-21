class Conta:
    def __init__(self, numero, titular, saldo, limite): #se eu quisersse padronizar o limite por exemplo era so colocar nessa linha q ele recebe 1000.0
        print("Construindo objeto...{}".format(self))   #e nos exemplos eu posso deixar em branco e n cai dar erro e se eu quiser criar um diferente eu so tenho q passar esse diferente
        self.__numero = numero  #EU DIGO NESSA LINHA: esse objeto conta tem um atributo numero
        self.__titular = titular
        self.__saldo = saldo
        self.__tarifaTransferencia = 8.0
        self.__limite = limite #quando tem 2 underscores (sublinhado) significa que esse atributo é privado
                               #mas ele so avisa que é privado mas n proibe
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor): #todo metodo q eu for fazer tem q ter o self pq ele faz referencia pra conta
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): #METODO PRIVADO , É O PRIVATE DO JAVA , VAI FUNCIONAR APENAS NA CLASSE CONTA
        valor_disponivel_para_sacar = self.saldo + self.__limite
        return valor_a_sacar <= (valor_disponivel_para_sacar) #RESPONDE EM BOOLEANA SE PODE SACAR  (EXEMPLO = conta._Conta__pode_sacar(100.0))


    def saca(self, valor):  #O SELF SIGNIFICA CONTA(QUE ESTA NA REFERENCIA DO OBJETO)
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("o valor {} passou o limite".format(valor))

    def tranferir(self, valor, destino):
        valor_total = valor + self.__tarifaTransferencia

        if valor_total < (self.__saldo + self.__limite):

            self.__saldo -= valor_total
            destino.deposita(valor)

            print("Transferencia efetuada.")
        else:
            print("Saldo insuficiente")

       # self.saca(valor)
       # destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property      #JOGAR NO CONSOLE: (EXEMPLO) conta.limite
    def limite(self):
        return self.__limite

    @limite.setter           #JOGAR NO CONSOLE :(EXEMPLO) conta.limite = 2000.0
    def limite(self, limite):
        self.__limite = limite

    @staticmethod  #TEM CHEIRO DE LINGUAGEM PROCEDURAL, JA QUE É INDEPENDENTE DE OBJETO PARA SER CHAMADO E NÃO MANIPULA INFORMAÇOES/ATRIBUTOS DE OBJETOS
    def codigos_bancos(): #static method, pertence a classe e nao precisa d objeto
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}   #EXEMPLO :codigos ['Caixa']

    #@staticmethod
    #def codigos_bancos():
    #return "001"  SE TODAS AS CONTAS FEITAS FOSSEM DO BANCO DO BRASIL