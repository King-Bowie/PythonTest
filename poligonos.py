from __future__ import print_function, division

import math
import turtle
jose = turtle.Turtle()

def square(t, length):
    """desenha um quadrado com lados dados pelo lenght
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def poligono(t, n, length):
    """desenha um poligono com os parametros sendo controlado pela quantidade de lados
    t: Turtle
    n: quantidade de lados
    lenght = tamanho
    """
    angle = 360.0/n
    polyline(t, n, length, angle)




def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circulo(t, r):
    """desenha um circulo com o raio
    t: Turtle
    r: radius
    """
    arc(t, r, 360)



if __name__ == '__main__':
    print(poligono(jose, 6, 30))

    raio = 100
    jose.pu()
    jose.fd(raio)
    jose.lt(90)
    jose.pd()
    circulo(jose, raio)


    turtle.mainloop()