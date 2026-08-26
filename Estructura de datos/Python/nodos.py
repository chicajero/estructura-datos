class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

n1 = Nodo(42)
n2 = Nodo(78)
n3 = Nodo(106)

n1.siguiente = n2
n2.siguiente = n3

actual = n1
i = 1 

while actual is not None:
   print(f"Nodo {i} || dato: {actual.dato} || ID: {id(actual)} || siguiente: {(actual.siguiente)}")
   actual = actual.siguiente
   i += 1

