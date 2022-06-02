def media(nota1, nota2):
    return (nota1 + nota2) / 2

def isAprovado(media):
    if(media>7):
        return "Aprovado"
    else:
        return "Reprovado"

print(isAprovado(media(4,10)))