class Pessoa:
    def __init__(self, nome, sobrenome, cpf, dia_nascimento, mes_nascimento, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.dia_nascimento = dia_nascimento
        self.mes_nascimento = mes_nascimento
        self.ano_nascimento = ano_nascimento

    def exibe_nome_e_sobrenome(self):
        print("O nome completo:{0} {1}".format(self.nome.title(), self.sobrenome.title()))# title() coloca a primeira palavra em maiusculo

    def sua_idade(self):
        print("{}/{}/{}".format(self.dia_nascimento, self.mes_nascimento, self.ano_nascimento))

    def calcular_idade(self, ano_nascimento):
        idade = (2021 - ano_nascimento)
        print("sua idade é {}".format(idade))

pessoa = Pessoa("augusto", "simoes", 300, 12, 4, 1972)
pessoa.calcular_idade(1959)
pessoa.exibe_nome_e_sobrenome()
