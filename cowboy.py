import microbit
"""

1. Cada célula que estaba viva pero tenía menos de dos vecinas vivas, se muere (demasiado poca población)
2. Cada célula que estaba viva y tenía dos o tres vecinas vivas, permanece viva
3. Cada célula que estaba viva pero tenía más de tres vecinas vivas, muere (demasiada sobrepoblación)
4. Cada célula que estaba muerta pero tenía exáctamente tres vecinas vivas, pasa a viva ("nace una nueva", por reproducción)

"""
grilla = [
    ['1', '0', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['1', '0', '0', '0', '0'],
]

def reglas(grilla):
    vecinos = 0
    fila = 0
    columna = 0
    grilla_nueva = [
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    for fila in range(5):
        for columna in range(5):
            if grilla[fila][columna] == '1':
                estado = '1'
            else:
                estado = '0'
            
            if fila - 1 >= 0:
                fila_restar = True
            else:
                fila_restar = False
            
            if fila + 1 <= 4:
                fila_sumar = True
            else:
                fila_sumar = False
            
            if columna - 1 >= 0:
                columna_restar = True
            else:
                columna_restar = False
            
            if columna + 1 <= 4:
                columna_sumar = True
            else:
                columna_sumar = False
            
            if fila_sumar == True: 
                if grilla[fila + 1][columna] == '1':
                    vecinos += 1

            if fila_restar == True:
                if grilla[fila - 1][columna] == '1':
                    vecinos += 1
            
            if columna_restar == True:
                if grilla[fila][columna - 1] == '1':
                    vecinos += 1

            if columna_sumar == True:
                if grilla[fila][columna + 1] == '1':
                    vecinos += 1

            if columna_sumar == True and fila_sumar == True:
                if grilla[fila + 1][columna + 1] == '1':
                    vecinos += 1

            if columna_sumar == True and fila_restar == True:
                if grilla[fila - 1][columna + 1] == '1':
                    vecinos += 1

            if columna_restar == True and fila_restar == True:
                if grilla[fila - 1][columna - 1] == '1':
                    vecinos += 1

            if columna_restar == True and fila_sumar == True:
                if grilla[fila + 1][columna - 1] == '1':
                    vecinos += 1

            if estado == '0':
                if vecinos == 3:
                    grilla_nueva[fila][columna] = '1'
                else:
                    grilla_nueva[fila][columna] = '0'
            else:
                if vecinos < 2 or vecinos > 3:
                    grilla_nueva[fila][columna] = '0'
                elif vecinos == 3 or vecinos == 2:
                    grilla_nueva[fila][columna] = '1'

            vecinos = 0
    return grilla_nueva

def devolver(grilla_nueva):
    return microbit.Image(
        ':'.join(''.join(fila)
            for fila in grilla_nueva)
    )

microbit.display.show(devolver(grilla))
microbit.sleep(1000)
while True:
    nueva_grilla = reglas(grilla)
    grilla = nueva_grilla
    microbit.display.show(devolver(grilla))
    microbit.sleep(1000)