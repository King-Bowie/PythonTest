import math

#FUNCOES:  A expressão entre parênteses é chamada de argumento da função. Para esta função, o resultado é o tipo do argumento.

livro = 24.95

print (int (livro)) #funçao pra transformar qlqr numero em int

#===================================================================================================================================


def print_lyrics():      #CRIACAO DE FUNCAO
    print("-------------------------------------------")
    print("Imagine all the people")
    print("Living life in peace")
    print("-------------------------------------------")
      

print( print_lyrics)
type (print_lyrics)  
print_lyrics()

def repeat_lyrics():    # ORDEM DE FUNCOES NAO ALTERA A FLUXO  DE EXECUCAO DO PROGRAMA


    print_lyrics()
    print_lyrics()


repeat_lyrics()  # O QUE FICA DENTRO DESSES PARENTESES SE CHAMA ARGUMENTO   

def print_twice(King) :  #CRIEI ARGUMENTO E OQ EU COLOCAR VAI REPETIR NESSE EXEMPLO
    #funções,como print_twice, executam uma ação, mas não devolvem um valor. Elas são chamadas de funções nulas.
    print(King)
    print(King)

print_twice('Teste')

print_twice(math.pi)

print_twice('spam '*4)

print_twice(math.cos(math.pi)) 

michael = "ze que manda o fino"

print_twice(michael)  #O nome da variável que passamos como argumento (michael) não tem nada a ver com o
                       #nome do parâmetro (bruce). Não importa que o valor tenha sido chamado de volta (em
                       #quem chama); aqui em print_twice, chamamos todo mundo de bruce.



def cat_twice(part1 , part2) :  # A ordem das funções no traceback é a mesma que a ordem dos frames no diagrama da pilha
        cat = part1 + part2     #    ^           ^           ^            ^            ^       ^          ^
        print_twice (cat)       #   | |         | |         | |          | |          | |     | |        | |
       
line1 = 'alguma palavra '
line2 = 'palavra alguma .'
cat_twice(line1,line2) # Quando cat_twice é encerrada, a variável cat é destruída


x = math.cos(35)
plata = (math.sqrt(5) + 1) /2

print(plata)

print(math.sqrt(5))


s = "monty"
def right_justify(s) :   #Escreva uma função chamada right_justify, que receba uma string chamada s como 
                          #parâmetro e exiba a string com espaços suficientes à frente para que a última letra da
                          #string esteja na coluna 70 da tela
    print( "                                                        " + s)
    

print(len(s))

right_justify(s)


def do_twice(func, arg):
    func(arg)
    func(arg)

def print_twice(func , arg ):  
    func(arg)
    func(arg)

def print_spam():
    print('spam')

print_twice(print, 'BOUNASERA KATUXA')

def do_four(func , arg):
    do_twice(func, arg)
    do_twice(func, arg)
    
bb = 'vem '
do_four(print,bb)  #"arg" funciona como variavel e com string

def linha(func):
    print("+ - - - - + - - - - +")

def coluna(func):
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')

linha(print)
coluna(print)
linha(print)
coluna(print)
linha(print)

