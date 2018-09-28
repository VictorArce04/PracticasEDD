pila = []#se crea el arreglo
tam = 5#se le asigna un tamano

def push(Valor):#Metodo push con el cual se agrega un numero a la pila
    if len(pila) < tam:#Aqui el programa identifica que el tamano de la pila no se mas grande al que asignamos
        pila.append(Valor)#en esta linea se agrega el numero que el usuario desea
    else:#Si el tamano excede al que asignamos lanza el siguiente mensaje
        print("Pila llena")

def Menu():#Metodo para el menu
    print("Menu de pila")
    print("Ingrese numero(ejemplo: 1)")
    print("1-.push")

    opc = int(input())#Se ingresa el numero para seleccionar la opcion del menu
    if (opc==1):#aqui si el numero ingresado es igual a "1" se ejecuta la siguiente parte del codigo que hace qu ele push funcione
        print("Ingrese el numero para apilar")
        i = input()
        push(i);
        print("Valor ingresado")
        Menu()
Menu()
