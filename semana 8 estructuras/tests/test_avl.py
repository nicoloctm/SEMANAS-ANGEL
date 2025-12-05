from semana_8_estructuras.avl import AVL

def _recorrer_nodos(nodo, collect):
    if nodo is None:
        return
    collect.append(nodo)
    _recorrer_nodos(nodo.izquierdo, collect)
    _recorrer_nodos(nodo.derecho, collect)

def test_avl_insert_balance():
    avl = AVL()
    seq = [10, 20, 30, 40, 50, 25]
    for v in seq:
        avl.insertar(v)
    # inorden values sorted
    vals = avl.mostrar_valores()
    assert vals == sorted(vals)
    # check factor de balance en todos los nodos abs <= 1
    nodes = []
    _recorrer_nodos(avl.raiz, nodes)
    for n in nodes:
        assert abs(avl.factor_balance(n)) <= 1
