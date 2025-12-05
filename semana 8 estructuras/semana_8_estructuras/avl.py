class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1  # altura de hoja = 1

class AVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        return nodo.altura if nodo else 0

    def factor_balance(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierdo) - self.altura(nodo.derecho)

    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.altura(nodo.izquierdo),
                              self.altura(nodo.derecho))

    def rotacion_derecha(self, z):
        y = z.izquierdo
        T3 = y.derecho

        y.derecho = z
        z.izquierdo = T3

        self.actualizar_altura(z)
        self.actualizar_altura(y)
        return y

    def rotacion_izquierda(self, z):
        y = z.derecho
        T2 = y.izquierdo

        y.izquierdo = z
        z.derecho = T2

        self.actualizar_altura(z)
        self.actualizar_altura(y)
        return y

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if not nodo:
            return NodoAVL(valor)

        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor)
        else:
            return nodo  # sin duplicados

        self.actualizar_altura(nodo)
        fb = self.factor_balance(nodo)

        # Casos de rotación
        # LL
        if fb > 1 and valor < nodo.izquierdo.valor:
            return self.rotacion_derecha(nodo)
        # RR
        if fb < -1 and valor > nodo.derecho.valor:
            return self.rotacion_izquierda(nodo)
        # LR
        if fb > 1 and valor > nodo.izquierdo.valor:
            nodo.izquierdo = self.rotacion_izquierda(nodo.izquierdo)
            return self.rotacion_derecha(nodo)
        # RL
        if fb < -1 and valor < nodo.derecho.valor:
            nodo.derecho = self.rotacion_derecha(nodo.derecho)
            return self.rotacion_izquierda(nodo)

        return nodo

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append((nodo.valor, self.factor_balance(nodo)))
            self._inorden(nodo.derecho, resultado)

    def mostrar_valores(self):
        """Devuelve lista de valores en inorden (solo valores)."""
        return [v for v, _ in self.inorden()]
