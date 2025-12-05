from semana_8_estructuras.huffman import Huffman

def test_huffman_basic():
    texto = "ABRACADABRA"
    h = Huffman()
    h.construir_arbol(texto)
    cod = h.codificar(texto)
    dec = h.decodificar(cod)
    assert dec == texto
    assert len(cod) == 23
