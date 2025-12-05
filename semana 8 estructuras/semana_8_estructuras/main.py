# main.py
"""
Demostración de las estructuras de la semana 8:
- BST (insertar, buscar, eliminar, recorridos)
- AVL (insertar, verificar factores de balance)
- Huffman (construir, codificar, decodificar)
- Evaluador RPN (evaluar expresiones postfijas)

Ejecutar:
    python main.py
"""

from .bst import BST
from .avl import AVL
from .huffman import Huffman
from .rpn_eval import evaluar_postfija

def demo_bst():
    print("=== BST Demo ===")
    bst = BST()
    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        bst.insertar(v)
    print("Inorden tras inserciones:", bst.inorden())
    assert bst.inorden() == sorted(valores)

    print("Buscar 60 (debe ser True):", bst.buscar(60))
    print("Buscar 99 (debe ser False):", bst.buscar(99))
    assert bst.buscar(60) is True and bst.buscar(99) is False

    print("Minimo:", bst.minimo(), "Maximo:", bst.maximo())
    assert bst.minimo() == min(valores) and bst.maximo() == max(valores)

    # Eliminar hoja
    print("Eliminar 20 (hoja).")
    bst.eliminar(20)
    print("Inorden:", bst.inorden())
    assert 20 not in bst.inorden()

    # Insertar 25 y eliminar nodo con un hijo
    print("Insertar 25 y eliminar 30 (tendrá un hijo).")
    bst.insertar(25)
    bst.eliminar(30)
    print("Inorden:", bst.inorden())
    assert 30 not in bst.inorden()

    # Eliminar raíz (caso 2/3)
    print("Eliminar 50 (raíz con dos hijos).")
    bst.eliminar(50)
    print("Inorden:", bst.inorden())
    assert 50 not in bst.inorden()

    print("BST demo completado.\n")

def demo_avl():
    print("=== AVL Demo ===")
    avl = AVL()
    seq = [10, 20, 30, 40, 50, 25]
    for v in seq:
        avl.insertar(v)
        print(f"Insertado {v} -> inorden (value, FB):", avl.inorden())

    # Valores ordenados
    valores_inorden = [v for v, _ in avl.inorden()]
    assert valores_inorden == sorted(valores_inorden)

    # Verificar FB abs <= 1 en todos los nodos
    def recorrer(nodo, collect):
        if nodo is None:
            return
        collect.append(nodo)
        recorrer(nodo.izquierdo, collect)
        recorrer(nodo.derecho, collect)

    nodes = []
    recorrer(avl.raiz, nodes)
    for n in nodes:
        fb = avl.factor_balance(n)
        if abs(fb) > 1:
            raise AssertionError(f"Nodo {n.valor} con FB fuera de rango: {fb}")
    print("Todos los factores de balance están dentro de |FB| <= 1.")
    print("AVL demo completado.\n")

def demo_huffman():
    print("=== Huffman Demo ===")
    texto = "ABRACADABRA"
    h = Huffman()
    h.construir_arbol(texto)
    print("Códigos generados:")
    for c, code in sorted(h.codigos.items(), key=lambda x: (len(x[1]), x[1])):
        print(f"  '{c}': {code} (len={len(code)})")

    codificado = h.codificar(texto)
    decodificado = h.decodificar(codificado)
    print("Texto:", texto)
    print("Codificado:", codificado)
    print("Decodificado:", decodificado)
    assert decodificado == texto
    print("Bits totales codificados:", len(codificado))
    print("Huffman demo completado.\n")

def demo_rpn():
    print("=== RPN Evaluator Demo ===")
    casos = [
        ("3 4 +", 7.0),
        ("3 4 + 2 *", 14.0),
        ("5 1 2 + 4 * + 3 -", 14.0),  # 5 + (1+2)*4 -3 = 14
        ("2 3 ^ 4 +", 12.0),         # 2**3 + 4 = 12
    ]
    for expr, esperado in casos:
        resultado = evaluar_postfija(expr)
        print(f"  {expr} = {resultado} (esperado {esperado})")
        assert abs(resultado - esperado) < 1e-9

    # Caso inválido (debe lanzar ValueError)
    try:
        evaluar_postfija("3 +")
        raise AssertionError("Expresión inválida no lanzó ValueError")
    except ValueError:
        print("  Caso inválido '3 +' correctamente produjo ValueError.")
    print("RPN demo completado.\n")

def main():
    print("Demostración completa - Semana 8\n")
    try:
        demo_bst()
        demo_avl()
        demo_huffman()
        demo_rpn()
    except AssertionError as e:
        print("ERROR - aserción fallida:", e)
    except Exception as ex:
        print("ERROR - excepción durante la demo:", type(ex).__name__, ex)
    else:
        print("Todas las demos completadas correctamente.")

if __name__ == "__main__":
    main()
