def exp(dos, pot):
    if pot == 0:
        return 1;
    elif pot == 1:
        return dos
    else:
        return dos*exp(dos,pot-1);

def consultaDato():
    print("Ingrese el valor de n para 2^n:")
    pot = int(input())
    print(exp(2,pot))
    consultaDato()

consultaDato()
