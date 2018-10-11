fr = 0
dato = 0

def crear():
    anillo = [1, 2, 3, 4, 5]
    fr = 0

    return anillo, fr

ring, fr= crear()
print(ring)
print(len(ring))

def pop(ring, fr):
    if fr == 0:
        if ring[fr] != 0:
            ring[0] = 0
            fr+=1
            return ring, fr
        else:
            print("Espacio Vacio")
            return ring, fr
    elif fr == 1:
        if ring[fr] != 0:
            ring[1] = 0
            fr+=1
            return ring, fr
        else:
            print("Espacio Vacio")
            return ring, fr
    elif fr == 2:
        if ring[fr] != 0:
            ring[2] = 0
            fr+=1
            return ring, fr
        else:
            print("Espacio Vacio")
            return ring, fr
    elif fr == 3:
        if ring[fr] != 0:
            ring[3] = 0
            fr+=1
            return ring, fr
        else:
            print("Espacio Vacio")
            return ring, fr
    elif fr == 4:
        if ring[fr] != 0:
            ring[4] = 0
            fr-=4
            return ring, fr
        else:
            print("Espacio Vacio")
            return ring, fr

def Menu(ring, fr):
    while True:
        print("Menu:")
        print("Seleccione una opcion (ejemplo: 1)")
        print("1-.desencolar")


        opc = int(input())
        if (opc == 1):
            ring, fr = pop(ring, fr);
            print(ring)

Menu(ring, fr)
