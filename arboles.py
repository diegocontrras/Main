class Nodo():
    
    def __init__(self, valor):
        self.hijoDer = None
        self.hijoIzq = None
        self.valor = valor
        self.padre = None
          
class Arbol():
    
    def __init__(self) :
        self.raiz = None
    
    def ObtenerRaiz(self):
        if self.raiz == None:
            print(f"El árbol no existe")
        else:
            print(f"La raíz del árbol es {self.raiz.valor}")
    
    def Agregar(self, valor, nodo):
        if self.raiz == None:   
            self.raiz = Nodo(valor) # Si el árbol está vacío el valor se convierte en la raíz
        else:
            if valor < nodo.valor:
                if nodo.hijoIzq == None:
                    nodo.hijoIzq = Nodo(valor)  # Si la raíz no tiene hijo Izquierdo se le agrega
                else:
                    self.Agregar(valor, nodo.hijoIzq)   # Llama recursivamente Agregar en el subárbol Izquierdo
            if valor > nodo.valor:
                if nodo.hijoDer == None:
                    nodo.hijoDer = Nodo(valor)  # Si la raíz no tiene hijo Derecho se le agrega
                else:
                    self.Agregar(valor, nodo.hijoDer)   # Llama recursivamente Agregar en el subárbol Derecho
            if valor == nodo.valor:
                print(f"El valor {nodo.valor} ya existe en el árbol\n")

    def Buscar(self, valor, nodo):
        if self.raiz == None:
            return False
        else:
            if valor < nodo.valor:
                if nodo.hijoIzq == None:
                    return False
                else:
                    return self.Buscar(valor, nodo.hijoIzq)
            if valor > nodo.valor:
                if nodo.hijoDer == None:
                    return False
                else:
                    return self.Buscar(valor, nodo.hijoDer)
            if valor == nodo.valor:
                return True
        return False

    def PreOrden(self, nodo):
        if nodo != None:
            print(nodo.valor, end= " ")  # Se imprime la raíz
            self.PreOrden(nodo.hijoIzq)
            self.PreOrden(nodo.hijoDer)
    
    def InOrden(self, nodo):
        if nodo != None:
            self.InOrden(nodo.hijoIzq)
            print(nodo.valor, end= " ")  # Se imprime la raíz
            self.InOrden(nodo.hijoDer)

    def PostOrden(self, nodo):
        if nodo != None:
            self.InOrden(nodo.hijoIzq)
            self.InOrden(nodo.hijoDer)
            print(nodo.valor, end= " ")  # Se imprime la raíz
    
    def Anchura(self, nodo):
        if nodo != None:
            cola = [nodo]   # Se crea una cola con nodo
            while cola: # Se inicia un bucle para recorrer toda la lista 
                nodo_actual = cola.pop(0)
                print(nodo_actual.valor, end = " ") # Se imprime el nodo actual
                if nodo_actual.hijoIzq:
                    cola.append(nodo_actual.hijoIzq)    # Se agrega a la cola los hijos izquierdos
                if nodo_actual.hijoDer:
                    cola.append(nodo_actual.hijoDer)     # Se agrega a la cola los hijos derechos
    
    def Limpiar(self):
        self.raiz = None
        
    def Max(self, nodo):
        while nodo.hijoDer != None:
            nodo = nodo.hijoDer
        return nodo.valor

    def Min(self, nodo):
        while nodo.hijoIzq != None:
            nodo = nodo.hijoIzq
        return nodo.valor
            
    def Eliminar(self, valor, nodo):
        if nodo != None:
            if valor < nodo.valor:  # Caso 1: Es menor que el valor de la raíz
                nodo.hijoIzq = self.Eliminar(valor, nodo.hijoIzq)
            else:   # Caso 2: Es mayor o igual que el valor de la raíz
                if valor > nodo.valor:  # Caso 2.1: Es mayor que el valor de la raíz
                    nodo.hijoDer = self.Eliminar(valor, nodo.hijoDer)
                else:   # Caso 3: Es igual al valor de la raíz
                    if nodo.hijoIzq == None:    # Caso 3.1: No tiene hijo izquierdo
                        return nodo.hijoDer
                    elif nodo.hijoDer == None:  # Caso 3.2: No tiene hijo derecho
                        return nodo.hijoIzq
                    else:   # Caso 3.3: Tiene dos hijos
                        sucesor = self.Min(nodo.hijoDer)
                        nodo.valor = sucesor
                        nodo.hijoDer = self.Eliminar(sucesor, nodo.hijoDer)
        return nodo

arbol = Arbol() # Se crea árbol

print("Imprimiendo el árbol:\n")

print("PreOrden:", end=" ")
arbol.PreOrden(arbol.raiz)
print("\n")

print("InOrden:", end=" ")
arbol.InOrden(arbol.raiz)
print("\n")

print("PostOrden:", end=" ")
arbol.PostOrden(arbol.raiz)
print("\n")

print("Anchura:", end=" ")
arbol.Anchura(arbol.raiz)
print("\n")

arbol.Agregar(8, arbol.raiz)
arbol.Agregar(3, arbol.raiz)
arbol.Agregar(10, arbol.raiz)
arbol.Agregar(1, arbol.raiz)
arbol.Agregar(6, arbol.raiz)
arbol.Agregar(14, arbol.raiz)
arbol.Agregar(4, arbol.raiz)
arbol.Agregar(7, arbol.raiz)
arbol.Agregar(13, arbol.raiz)

print("Imprimiendo el árbol:\n")

print("PreOrden:", end=" ")
arbol.PreOrden(arbol.raiz)
print("\n")

print("InOrden:", end=" ")
arbol.InOrden(arbol.raiz)
print("\n")

print("PostOrden:", end=" ")
arbol.PostOrden(arbol.raiz)
print("\n")

print("Anchura:", end=" ")
arbol.Anchura(arbol.raiz)
print("\n")

arbol.Agregar(14, arbol.raiz) #Repetido, debe mostrar mensaje de error
arbol.Agregar(1, arbol.raiz) #Repetido, debe mostrar mensaje de error

m = arbol.Min(arbol.raiz)
M = arbol.Max(arbol.raiz)
print(f"El valor mínimo del árbol es: {m}")
print(f"El valor máximo del árbol es: {M}")
print("\n")

resultado = arbol.Buscar(4, arbol.raiz)
print(f"Existe el valor 4? {resultado}")

resultado = arbol.Buscar(8, arbol.raiz)
print(f"Existe el valor 8? {resultado}")

resultado = arbol.Buscar(13, arbol.raiz)
print(f"Existe el valor 13? {resultado}")

resultado = arbol.Buscar(2, arbol.raiz)
print(f"Existe el valor 2? {resultado}")

resultado = arbol.Buscar(15, arbol.raiz)
print(f"Existe el valor 15? {resultado}")

print("----------------")
arbol.Eliminar(7, arbol.raiz)
print("\nEliminando el número 7\n")

print("Imprimiendo el árbol:\n")

print("PreOrden:", end=" ")
arbol.PreOrden(arbol.raiz)
print("\n")

print("InOrden:", end=" ")
arbol.InOrden(arbol.raiz)
print("\n")

print("PostOrden:", end=" ")
arbol.PostOrden(arbol.raiz)
print("\n")

print("Anchura:", end=" ")
arbol.Anchura(arbol.raiz)
print("\n")

print("----------------")
arbol.Eliminar(10, arbol.raiz) # Borrando el 10 (solo hijo der)
print("Eliminando el número 10\n")

print("Imprimiendo el árbol:\n")

print("PreOrden:", end=" ")
arbol.PreOrden(arbol.raiz)
print("\n")

print("InOrden:", end=" ")
arbol.InOrden(arbol.raiz)
print("\n")

print("PostOrden:", end=" ")
arbol.PostOrden(arbol.raiz)
print("\n")

print("Anchura:", end=" ")
arbol.Anchura(arbol.raiz)
print("\n")

print("----------------")
arbol.Eliminar(6, arbol.raiz) # Borrando el 6 (solo hijo izq)
print("Eliminando el número 6\n")

print("Imprimiendo el árbol:\n")

print("PreOrden:", end=" ")
arbol.PreOrden(arbol.raiz)
print("\n")

print("InOrden:", end=" ")
arbol.InOrden(arbol.raiz)
print("\n")

print("PostOrden:", end=" ")
arbol.PostOrden(arbol.raiz)
print("\n")

print("Anchura:", end=" ")
arbol.Anchura(arbol.raiz)
print("\n")

print("----------------")
arbol.Eliminar(3, arbol.raiz) # Borrando el 3 (ambos hijos)
print("Eliminando el número 3\n") 

print("Imprimiendo el árbol:\n")

print("PreOrden:", end=" ")
arbol.PreOrden(arbol.raiz)
print("\n")

print("InOrden:", end=" ")
arbol.InOrden(arbol.raiz)
print("\n")

print("PostOrden:", end=" ")
arbol.PostOrden(arbol.raiz)
print("\n")

print("Anchura:", end=" ")
arbol.Anchura(arbol.raiz)
print("\n")

print("----------------")
arbol.Eliminar(3, arbol.raiz) # Borrando el 3 (ambos hijos)
print("Eliminando el número 3\n") 

print("Imprimiendo el árbol:\n")

print("PreOrden:", end=" ")
arbol.PreOrden(arbol.raiz)
print("\n")

print("InOrden:", end=" ")
arbol.InOrden(arbol.raiz)
print("\n")

print("PostOrden:", end=" ")
arbol.PostOrden(arbol.raiz)
print("\n")

print("Anchura:", end=" ")
arbol.Anchura(arbol.raiz)
print("\n")

print("----------------")
arbol.Eliminar(8, arbol.raiz) # Borrando el 3 (ambos hijos)
print("Eliminando el número 8\n") 

print("Imprimiendo el árbol:\n")

print("PreOrden:", end=" ")
arbol.PreOrden(arbol.raiz)
print("\n")

print("InOrden:", end=" ")
arbol.InOrden(arbol.raiz)
print("\n")

print("PostOrden:", end=" ")
arbol.PostOrden(arbol.raiz)
print("\n")

print("Anchura:", end=" ")
arbol.Anchura(arbol.raiz)
print("\n")

print("----------------")
arbol.Agregar(100, arbol.raiz) # Borrando el 3 (ambos hijos)
print("Agregando el número 100\n") 

print("Imprimiendo el árbol:\n")

print("PreOrden:", end=" ")
arbol.PreOrden(arbol.raiz)
print("\n")

print("InOrden:", end=" ")
arbol.InOrden(arbol.raiz)
print("\n")

print("PostOrden:", end=" ")
arbol.PostOrden(arbol.raiz)
print("\n")

print("Anchura:", end=" ")
arbol.Anchura(arbol.raiz)
print("\n")

print("----------------")

