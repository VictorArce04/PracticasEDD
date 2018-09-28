pila = []
tam = 5
def push(Valor):
    if len(pila) < tam:
        pila.append(Valor)
    else:
        print("Pila llena")
        
def peek():
    if 0 < len(pila):
        print("Tope de pila:")  
        print(pila[len(pila)-1])
    else:
        print("Pila vacia");
        
def pop():
    if 0 < len(pila):
        print("Valor del tope de la pila:")
        print(pila[len(pila)-1])
        del(pila[len(pila)-1])
    else:
        print("Pila vacia");

def ImprimirPila():
    print(pila)
    print("pila completa")
    
def Menu():
    print("Menu de pila")
    print("Ingrese numero(ejemplo: 1)")
    print("1-.push")
    print("2-.pop")
    print("3-.peek")
    print("4-.Imprimir la pila")
    print("5-.salir")
    opc = int(input())
    if (opc==1):
        print("Ingrese el numero para apilar")
        i = input()
        push(i);
        print("Valor ingresado")
        Menu()
    if (opc==2):
        pop();
        Menu();
    if (opc==3):
        peek()
        Menu();
    if (opc==4):
        ImprimirPila()
        Menu()
        
        

Menu()
