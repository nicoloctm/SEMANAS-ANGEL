import heapq
from collections import Counter

class NodoHuffman:
    def __init__(self, caracter, frecuencia, orden):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.orden = orden
        self.izquierdo = None
        self.derecho = None

    def es_hoja(self):
        return self.izquierdo is None and self.derecho is None

class Huffman:
    def __init__(self):
        self.raiz = None
        self.codigos = {}
        self.codigos_inversos = {}

    def construir_arbol(self, texto):
        frecuencias = Counter(texto)
        if not frecuencias:
            return

        # Un solo símbolo
        if len(frecuencias) == 1:
            c = next(iter(frecuencias))
            nodo = NodoHuffman(c, frecuencias[c], 0)
            self.raiz = nodo
            self.codigos[c] = "0"
            self.codigos_inversos["0"] = c
            return

        heap = []
        orden = 0

        # Insertar hojas ORDENADAS solo por frecuencia y por orden
        for c, f in sorted(frecuencias.items()):
            heapq.heappush(heap, (f, orden, NodoHuffman(c, f, orden)))
            orden += 1

        # Construcción EXACTA estilo HTML: reinsertar con NUEVO orden incremental
        while len(heap) > 1:
            f1, o1, n1 = heapq.heappop(heap)
            f2, o2, n2 = heapq.heappop(heap)

            padre = NodoHuffman(None, f1 + f2, orden)
            orden += 1

            padre.izquierdo = n1
            padre.derecho = n2

            heapq.heappush(heap, (padre.frecuencia, padre.orden, padre))

        _, _, self.raiz = heap[0]
        self._generar_codigos(self.raiz, "")

    def _generar_codigos(self, nodo, pref):
        if nodo.es_hoja():
            self.codigos[nodo.caracter] = pref
            self.codigos_inversos[pref] = nodo.caracter
            return
        self._generar_codigos(nodo.izquierdo, pref + "0")
        self._generar_codigos(nodo.derecho, pref + "1")

    def codificar(self, texto):
        return ''.join(self.codigos[c] for c in texto)

    def decodificar(self, bits):
        res = []
        n = self.raiz
        for b in bits:
            n = n.izquierdo if b == "0" else n.derecho
            if n.es_hoja():
                res.append(n.caracter)
                n = self.raiz
        return ''.join(res)
