indice = 0
valor = 'Vacio'

def create():
    fila = ['Vacio', 'Vacio', 'Vacio', 'Vacio', 'Vacio']
    indice = 0
    return fila, indice

cola, indice = create()
print('-' * 25)
print(cola)
print(len(cola))
print('-' * 25)

def push(cola, valor, indice):

    if indice == 0:
        cola[indice] = valor;
        indice+=1
        print('-' * 25)
        print('Cliente en la cola')
        print('-' * 25)
        return cola, valor, indice
    elif indice == 1:
        cola[indice] = valor;
        indice+=1
        print('-' * 25)
        print('Cliente en la cola')
        print('-' * 25)
        return cola, valor, indice
    elif indice == 2:
        cola[indice] = valor;
        indice+=1
        print('-' * 25)
        print('Cliente en la cola')
        print('-' * 25)
        return cola, valor, indice
    elif indice == 3:
        cola[indice] = valor;
        indice+=1
        print('-' * 25)
        print('Cliente en la cola')
        print('-' * 25)
        return cola, valor, indice
    elif indice == 4:
        cola[indice] = valor;
        indice+=1
        print('-' * 25)
        print('Cliente en la cola')
        print('-' * 25)
        return cola, valor, indice
    else:
        print('-' * 25)
        print("fila llena")
        print('-' * 25)
        return cola, valor, indice

def pop(cola, indice):
    cola[0] = cola[1]
    cola[1] = cola[2]
    cola[2] = cola[3]
    cola[3] = cola[4]
    cola[4] = 'Vacio'
    indice-=1
    print('-' * 25)
    print(cola)
    print('-' * 25)
    return cola, indice

def peekI(cola, indice):
    if cola[0] == 'Vacio':
        print('-' * 25)
        print('no hay nadie en la cola')
        print('-' * 25)
        return cola, indice
    else:
        print('-' * 25)
        print(cola[0])
        print('-' * 25)
        return cola, indice

def peekAll(cola, indice):
    print('-' * 25)
    print(cola)
    print('-' * 25)
    return cola, indice

def Menu(cola, indice):
    while True:
        print("Menu:")
        print("Seleccione una opcion (ejemplo: 1)")
        print("1-.Mostrar al primer cliente de la fila")
        print("2-.Pasar al cliente")
        print("3-.Meter al cliente a la fila")
        print("4-.Mostrar fila completa")
        print('-' * 25)

        opc = int(input())
        if (opc == 1):
            cola, indice = peekI(cola, indice);
        if (opc == 2):
            cola, indice = pop(cola, indice);
            if indice < 0:
                print("fila vacia")
                print('-' * 25)
        if (opc == 3):
            print("""Ingrese "Cliente y su numero" para llenar el espacio al final de la cola""")
            valor = str(input())
            cola, valor, indice = push(cola, valor, indice);
            print(cola)
            print('-' * 25)
        if (opc == 4):
            cola, indice = peekAll(cola, indice);

    
Menu(cola, indice)
          
