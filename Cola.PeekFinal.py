index = 0
a = 0

def create():
    cola = [1, 2, 3, 4, 5]
    index=0
    return cola, index
    
var, index=create()
print(var)
print(len(var))

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

def Menu(var, index):
    while True:
        print("Menu:")
        print("Seleccione una opcion (ejemplo: 1)")
        print("1-.Peek Final")


        opc = int(input())
        if (opc == 1):
            var, index = peekF(var, index);

Menu(var, index)
