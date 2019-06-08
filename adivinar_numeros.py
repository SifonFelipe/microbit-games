import microbit

import random

lives = 3
numero = 5

x = random.randint(0, 9)

while lives > 0:
    if microbit.button_b.was_pressed():
        if numero < 9:
            numero = numero + 1

    if microbit.button_a.was_pressed():
        if numero > 0:
            numero = numero - 1

    if microbit.pin0.is_touched():
        if numero == x:
            #aca significa igual.
            microbit.display.show(microbit.Image.YES)
            microbit.sleep(2000)
            lives = lives = 0
        else:
            microbit.display.show(microbit.Image.NO)
            microbit.sleep(2000)
            lives = lives - 1   

        if numero < x:
            microbit.display.show("+")
            microbit.sleep(2000)

        if numero > x:
            microbit.display.show("-")
            microbit.sleep(2000)
        
    if microbit.pin1.is_touched and microbit.pin2.is_touched():
        lives = lives + 1
              
    microbit.display.show(numero)

while True:
    microbit.display.scroll("El numero era. . . . .")
    microbit.display.show(x)
    microbit.sleep(2000)
