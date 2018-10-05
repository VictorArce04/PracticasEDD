index = 0
a = 0

def create():
    cola = [1, 2, 3, 4, 5]
    index=0
    return cola, index
    
var, index=create()
print(var)
print(len(var))

def peekAll(var, index):
    print(var)
    return var, index
    

def Menu(var, index):
    while True:
        print("Menu:")
        print("Seleccione una opcion (ejemplo: 1)")
        print("1-.Peek cola")

        opc = int(input())

        if (opc == 1):
            var, index = peekAll(var, index);

Menu(var, index)
