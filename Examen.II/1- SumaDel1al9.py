def Suma(Lista):
    if len(Lista) == 1:
        return Lista[0]
    else:
        return Lista[0] + Suma(Lista[1:])

print(Suma([1,2,3,4,5,6,7,8,9]))
