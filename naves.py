import microbit
import random

lugar = random.randint(0, 4)

def armar_imagen(posicion_del_uno):
    texto = "00000:00000:00000:00000:"
    for posicion_actual in range(5):
        if posicion_actual == posicion_del_uno:
            texto = texto + "1"
        else:
            texto = texto + "0"            
    return microbit.Image(texto)

while True:
    if microbit.button_b.was_pressed():
        if lugar < 4:
            lugar = lugar + 1
            microbit.sleep(300)

    elif microbit.button_a.was_pressed():
        if lugar > 0:
            lugar = lugar - 1
            microbit.sleep(300)

    microbit.display.show(armar_imagen(lugar))

    
    