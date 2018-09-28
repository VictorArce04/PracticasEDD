pila = [1, 2, 3, 4, 5]
tam = 5

def peek():
    if 0 < len(pila):
        print("Tope de pila:")  
        print(pila[len(pila)-1])
    else:
        print("Pila vacia");

def Menu():
    print("Menu de pila")
    print("Ingrese numero(ejemplo: 1)")
    print("1-.peek")

    opc = int(input())
    if (opc==1):
        peek()
        Menu();

Menu();
