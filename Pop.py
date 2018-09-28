pila = [3, 4, 5, 6, 7]
tam = 5

def pop():
    if 0 < len(pila):
        print("Valor del tope de la pila:")
        print(pila[len(pila)-1])
        del(pila[len(pila)-1])
    else:
        print("Pila vacia");

def Menu():
    print("Menu de pila")
    print("Ingrese numero(ejemplo: 1)")
    print("1-.pop")

    opc = int(input())
    if (opc==1):
        pop();
        Menu();

Menu();
