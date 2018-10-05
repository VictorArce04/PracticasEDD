index = 0
a = 0

def create():
    cola = [0, 0, 0, 0, 0]
    index=0
    return cola, index
    
var, index=create()
print(var)
print(len(var))

def push(var, a, index):
    
    if index == 0:
        var[index] = a;
        index+=1
        print("Valor agregado")
        return (var, a, index)
    elif index == 1:
        var[index] = a;
        index+=1
        print("Valor agregado")
        return (var, a, index)
    elif index == 2:
        var[index] = a;
        index+=1
        print("Valor agregado")
        return (var, a, index)
    elif index == 3:
        var[index] = a;
        index+=1
        print("Valor agregado")
        return (var, a, index)
    elif index == 4:
        var[index] = a;
        index+=1
        print("Valor agregado")
        return (var, a, index)
    else:
        print("La cola esta llena")
        return (var, a, index)

def Menu(var, index):
    while True:
        print("Menu:")
        print("Seleccione una opcion (ejemplo: 1)")
        print("1-.Encolar")


        opc = int(input())
        if (opc == 1):
            print("Ingrese un numero a la cola")
            a = input()
            var, a, index = push(var, a, index);
            print(var)

Menu(var, index)
