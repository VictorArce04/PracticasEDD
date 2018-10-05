index = 0
a = 0

def create():
    cola = [1, 2, 3, 4, 5]
    index=0
    return cola, index
    
var, index=create()
print(var)
print(len(var))

def pop(var, index):
    if var == [0, 0, 0, 0, 0]:
        print('Cola vacia')
        return var, index
    else:
        var[0] = var[1]
        var[1] = var[2]
        var[2] = var[3]
        var[3] = var[4]
        var[4] = 0
        index-=1
        print(var)
        return var, index

def Menu(var, index):
    while True:
        print("Menu:")
        print("Seleccione una opcion (ejemplo: 1)")
        print("1-.Desencolar")

        opc = int(input())
        if (opc == 1):
            var, index = pop(var, index);

Menu(var, index)
