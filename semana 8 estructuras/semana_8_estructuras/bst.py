class NodoBST:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class BST:
    """
    Árbol Binario de Búsqueda sin duplicados.
    Métodos principales: insertar, buscar, eliminar, inorden, preorden, postorden, minimo, maximo.
    """
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = NodoBST(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoBST(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = NodoBST(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)
        # duplicados: no insertamos

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            # Caso 1: hoja
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            # Caso 2: un hijo (derecho)
            if nodo.izquierdo is None:
                return nodo.derecho
            # Caso 2: un hijo (izquierdo)
            if nodo.derecho is None:
                return nodo.izquierdo
            # Caso 3: dos hijos -> sucesor inorden (mínimo del subárbol derecho)
            sucesor = self._encontrar_minimo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.valor)
        return nodo

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)

    def preorden(self):
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierdo, resultado)
            self._preorden_recursivo(nodo.derecho, resultado)

    def postorden(self):
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado

    def _postorden_recursivo(self, nodo, resultado):
        if nodo:
            self._postorden_recursivo(nodo.izquierdo, resultado)
            self._postorden_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.valor)

    def minimo(self):
        if not self.raiz:
            return None
        return self._encontrar_minimo(self.raiz).valor

    def maximo(self):
        if not self.raiz:
            return None
        nodo = self.raiz
        while nodo.derecho:
            nodo = nodo.derecho
        return nodo.valor
