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

def pop(var, index):
    var[0] = var[1]
    var[1] = var[2]
    var[2] = var[3]
    var[3] = var[4]
    var[4] = 0
    index-=1
    print(var)
    return var, index
        
def peekI(var, index):
    if var[0] == 0:
        print('no hay ningun dato')
        return(var, index)
    else:
        print(var[0])
        return(var, index)
    
def peekF(var, index):
    if var[4] != 0:
        print(var[4])
        return(var, index)
    elif var[3] != 0:
        print(var[3])
        return(var, index)
    elif var[2] != 0:
        print(var[2])
        return(var, index)
    elif var[1] != 0:
        print(var[1])
        return(var, index)
    elif var[0] != 0:
        print(var[0])
        return(var, index)
    

def peekInd(var, dat, index):
    if var[4] or var[3] or var[2] or var[1] or var[0]== dat:
        print('El dato esta en la cola')
        return(var, dat, index)
    else:
        print('El dato no se encuentra en la cola')
    
def peekAll(var):
    print(var)
    

def Menu(var, index):
    while True:
        print("Menu:")
        print("Seleccione una opcion (ejemplo: 1)")
        print("1-.Encolar")
        print("2-.Desencolar")
        print("3-.Peek Inicio")
        print("4-.Peek Final")
        print("5-.Peek dato")
        print("6-.Peek cola")

        opc = int(input())
        if (opc == 1):
            print("Ingrese un numero a la cola")
            a = input()
            var, a, index = push(var, a, index);
            print(var)
        if (opc == 2):
            var, index = pop(var, index);

            if index < 0:
                print("Cola vacia")
        if (opc == 3):
            var, index = peekI(var, index);
        if (opc == 4):
            var, index = peekF(var, index);
        if (opc == 5):
            print("Ingrese un numero a comprobar")
            dat = input()
            var, index = peekInd(var, dat, index);
        if (opc == 6):
            var, index = peekAll(var, index);

    
Menu(var, index)
