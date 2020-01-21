import microbit
import random

lugar = random.randint(0, 4)
enemigo = random.randint(0, 4)
turnos_seguidos = 0
elegir_frase = random.randint(0, 1)
frases_heroicas = ["Mejor muerto que rebelde", "Con honor hasta el FINAL!"]
estado_enemigo = 'esperando'
estado_aliado = 'moviendose'
turnos_haciendo_lo_mismo = 0
contador_enemigos_muertos = 0

def armar_imagen(posicion_del_enemigo, posicion_del_aliado):
    texto = ""
    for posicion_actual in range(5):
        if posicion_actual == posicion_del_enemigo:
            texto = texto + "1"
        else:
            texto = texto + "0"
    for fila in range(3):
        texto = texto + ":"
        for posicion_actual in range(5):
            if (posicion_actual == posicion_del_enemigo and estado_enemigo == 'disparando') \
                or (posicion_actual == posicion_del_aliado and estado_aliado == 'disparando'):               
                texto = texto + '1'
            else:
                texto = texto + '0'
    texto = texto + ':'
    for posicion_actual in range(5):
        if posicion_actual == posicion_del_aliado:
            texto = texto + "1"
        else:
            texto = texto + "0" 
    return microbit.Image(texto) 

while estado_aliado != 'muerto':
    if estado_enemigo == 'muerto':
        estado_enemigo = 'esperando'
        enemigo = random.randint(0,4)
        contador_enemigos_muertos = contador_enemigos_muertos + 1 
        turnos_haciendo_lo_mismo = 0

    if microbit.button_b.was_pressed():
        if lugar < 4:
            lugar = lugar + 1
    elif microbit.button_a.was_pressed():
        if lugar > 0:
            lugar = lugar - 1

    if microbit.pin0.is_touched() or microbit.pin1.is_touched() or microbit.pin2.is_touched():
        estado_aliado = 'disparando'
    else:
        estado_aliado = 'moviendose'

    turnos_haciendo_lo_mismo = turnos_haciendo_lo_mismo + 1
    if turnos_haciendo_lo_mismo == 11:
        if estado_enemigo == 'disparando':
            estado_enemigo = 'esperando'
        else:
            estado_enemigo = 'disparando'
        turnos_haciendo_lo_mismo = 0

    if enemigo == lugar and estado_enemigo == 'disparando':
        estado_aliado = 'muerto'
    
    if estado_aliado == 'disparando' and lugar == enemigo:
        estado_enemigo = 'muerto'

    microbit.display.show(armar_imagen(enemigo, lugar))
    microbit.sleep(200)

while True:
    microbit.display.scroll('Mataste a: {} enemigos'.format(contador_enemigos_muertos))
    microbit.display.scroll(frases_heroicas[elegir_frase])
    microbit.sleep(2000)