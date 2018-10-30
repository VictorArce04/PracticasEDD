class Nodo():
    def __init__(self,dato):
        self.dato = dato
        self.sig = None
        self.ant = None

class Lista():
    def __init__(self):
        self.P = None
        self.U = None
        self.tam = 0

    def vacia(self):
        return self.P == None

    def pushFinal(self,dato):
        if self.vacia():
            self.P = self.U = Nodo(dato)
        else:
            aux = self.U
            self.U = aux.sig = Nodo(dato)
            self.U.ant = aux
        self.tam += 1

    def pushInicio(self,dato):
        if self.vacia():
            self.P = self.U = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.sig = self.P
            self.P.ant = aux
            self.P = aux
        self.tam += 1

    def popDato(self,dato):
        aux = self.P
        for i in range(self.tam):
            if aux.dato == dato:
                aux.dato = None
            else:
                aux = aux.sig

    def peekDato(self,dat):
        aux = self.P
        for i in range(self.tam):
            if aux.dato == dat:
                print("Dato en la cola.")
            else:
                aux = aux.sig

    def peekInicio(self):
        aux = self.P
        while aux:
            print(aux.dato)
            aux = aux.sig

    def peekFin(self):
        aux = self.U
        while aux:
            print(aux.dato)
            aux = aux.ant

List = Lista()

List.pushFinal(1)
List.pushFinal(2)
List.pushFinal(3)
List.pushFinal(4)
List.pushFinal(5)
List.pushFinal(6)
List.pushFinal(7)
List.pushFinal(8)
List.pushFinal(9)


List.peekInicio()

print("------------------")

List.peekFin()

print("------------------")

List.pushFinal(10)
List.pushFinal(11)
List.pushFinal(13)

List.popDato(8)
List.popDato(1)
List.peekInicio()

print("------------------")


