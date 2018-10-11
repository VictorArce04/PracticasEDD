indice = 0
fr = 0
dato = 0
dat = 0

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
        
def peekFront(ring, fr):
    print(ring[fr])
    return ring, fr

def peekFinal(ring, ind):
    print(ring[ind-1])
    return ring, ind

def peekDato(ring, dat):
    if ring[0] == dat:
        print("El dato esta en la cola")
        return ring, dat
    elif ring[1] == dat:
        print("El dato esta en la cola")
        return ring, dat
    elif ring[2] == dat:
        print("El dato esta en la cola")
        return ring, dat
    elif ring[3] == dat:
        print("El dato esta en la cola")
        return ring, dat
    elif ring[4] == dat:
        print("El dato esta en la cola")
        return ring, dat
    else:
        print("El dato no esta en la cola")
        return ring, dat

def Menu(ring, ind, fr):
    while True:
        print("Menu:")
        print("Seleccione una opcion (ejemplo: 1)")
        print("1-.Encolar")
        print("2-.Desencolar")
        print("3-.Peek Frente")
        print("4-.Peek Final")
        print("5-.Peek Dato")


        opc = int(input())
        if (opc == 1):
            print("Ingrese un numero a la cola")
            dato = input()
            ring, dato, ind = push(ring, dato, ind);
            print(ring)
        if (opc == 2):
            ring, fr = pop(ring, fr);
            print(ring)
        if (opc == 3):
            ring, fr = peekFront(ring, fr);
        if (opc == 4):
            ring, ind = peekFinal(ring, ind)
        if (opc == 5):
            print("Ingrese un numero a comprobar")
            dat = input()
            ring, dato = peekDato(ring, dat)
            
Menu(ring, ind, fr)

