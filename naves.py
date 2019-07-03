import microbit
import random

lugar = random.randint(0, 4)
enemigo = random.randint(0, 4)
turnos_seguidos = 0
elegir_frase = random.randint(0, 1)
frases_heroicas = ["Mejor muerto que rebelde", "Con honor hasta el FINAL!"]

def armar_imagen(posicion_del_enemigo, posicion_del_aliado):
    texto = ""
    for posicion_actual in range(5):
        if posicion_actual == posicion_del_enemigo:
            texto = texto + "1"
        else:
            texto = texto + "0"
    texto = texto + ":00000:00000:00000:" 
    for posicion_actual_del_aliado in range(5):
        if posicion_actual_del_aliado == posicion_del_aliado:
            texto = texto + "1"
        else:
            texto = texto + "0"
    return microbit.Image(texto)    

while turnos_seguidos < 3:
    if microbit.button_b.was_pressed():
        if lugar < 4:
            lugar = lugar + 1
            microbit.sleep(200)

    elif microbit.button_a.was_pressed():
        if lugar > 0:
            lugar = lugar - 1
            microbit.sleep(200)

    if lugar == enemigo:
        turnos_seguidos = turnos_seguidos + 1
        microbit.sleep(200)
    else:
        turnos_seguidos = turnos_seguidos = 0

    microbit.display.show(armar_imagen(enemigo, lugar))

while True:
    microbit.display.scroll(frases_heroicas[elegir_frase])
    microbit.sleep(2000)
    
    