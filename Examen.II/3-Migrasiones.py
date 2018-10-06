pila = []
def push(ver):
    pila.append(ver)

def peek():
    if 0 < len(pila):
        print(pila[len(pila)-1])
        pila.pop()
    else:
        print("Pila vacia");

def noVersiones():
    print(len(pila))

def imprimirPila():
    print(pila)
    print("pila completa")
    
def menu():
    while True:
        print('Seleccione una opcion: (ejemplo: 1)')
        print('1-.Agregar migracion de la version')
        print('2-.Mostrar migraciones')
        print('3-.Cuantas versiones hay?')
        print("4-.Imprimir la pila")

        opc = int(input())
        if opc == 1:
            print('Ingrese la version a migrar: (Ejemplo: 2.11')
            ver = float(input())
            push(ver)
            print('Version ingresada')
            menu()
        if opc == 2:
            peek()
            menu()
        if opc == 3:
            noVersiones()
            menu()
        if (opc==4):
            imprimirPila()
            menu()

menu()

                                
