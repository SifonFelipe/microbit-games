import microbit
import random

punto1 = microbit.Image(
    "00000:"
    "00000:"
    "00000:"
    "00000:"
    "30000"
)

punto2 = microbit.Image(
    "00000:"
    "00000:"
    "00000:"
    "00000:"
    "03000"
)

puntomedio = microbit.Image(
    "00000:"
    "00000:"
    "00000:"
    "00000:"
    "00300"
)

punto4 = microbit.Image(
    "00000:"
    "00000:"
    "00000:"
    "00000:"
    "00030"
)

punto5 = microbit.Image(
    "00000:"
    "00000:"
    "00000:"
    "00000:"
    "00003"
)

lugar = random.randint(0, 4)
puntos = [punto1, punto2, puntomedio, punto4, punto5]

def mostrar_nave(lugar):
    microbit.display.show(puntos[lugar])

while True:
    if microbit.button_b.was_pressed():
        if lugar < 4:
            lugar = lugar + 1
            microbit.sleep(300)

    elif microbit.button_a.was_pressed():
        if lugar > 0:
            lugar = lugar - 1
            microbit.sleep(300)

    mostrar_nave(lugar)

    
    