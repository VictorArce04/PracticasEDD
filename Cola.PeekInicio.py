index = 0
a = 0

def create():
    cola = [1, 2, 3, 4, 5]
    index=0
    return cola, index
    
var, index=create()
print(var)
print(len(var))

def peekI(var, index):
    if var[0] == 0:
        print('no hay ningun dato')
        return(var, index)
    else:
        print(var[0])
        return(var, index)

def Menu(var, index):
    while True:
        print("Menu:")
        print("Seleccione una opcion (ejemplo: 1)")
        print("1-.Peek Inicio")
        
        opc = int(input())
        if (opc == 1):
            var, index = peekI(var, index);

Menu(var, index)
