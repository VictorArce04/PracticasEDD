indice = 0
fr = 0
dato = 0

def crear():
    anillo = [0, 0, 0, 0, 0]
    indice = 0
    fr = 0

    return anillo, indice, fr

ring, ind, fr= crear()
print(ring)
print(len(ring))

def push(ring, dato, ind):
    if ind == 0:
        if ring[0] != 0:
            print("Cola Llena")
            return ring, dato, ind
        else:
            ring[ind] = dato
            ind+=1
            print("Valor Agregado")
            return ring, dato, ind
    elif ind == 1:
        if ring[1] != 0:
            print("Cola Llena")
            return ring, dato, ind
        else:
            ring[ind] = dato
            ind+=1
            print("Valor Agregado")
            return ring, dato, ind
    elif ind == 2:
        if ring[2] != 0:
            print("Cola Llena")
            return ring, dato, ind
        else:
            ring[ind] = dato
            ind+=1
            print("Valor Agregado")
            return ring, dato, ind
    elif ind == 3:
        if ring[3] != 0:
            print("Cola Llena")
            return ring, dato, ind
        else:
            ring[ind] = dato
            ind+=1
            print("Valor Agregado")
            return ring, dato, ind
    elif ind == 4:
        if ring[4] != 0:
            print("Cola Llena")
            return ring, dato, ind
        else:
            ring[ind] = dato
            ind-=4
            print("Valor Agregado")
            return ring, dato, ind

def Menu(ring, ind, fr):
    while True:
        print("Menu:")
        print("Seleccione una opcion (ejemplo: 1)")
        print("1-.Encolar")
        print("2-.desencolar")


        opc = int(input())
        if (opc == 1):
            print("Ingrese un numero a la cola")
            dato = input()
            ring, dato, ind = push(ring, dato, ind);
            print(ring)

Menu(ring, ind, fr)
