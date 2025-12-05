from semana_8_estructuras.rpn_eval import evaluar_postfija

def test_rpn_simple():
    assert evaluar_postfija("3 4 +") == 7.0
    assert evaluar_postfija("3 4 + 2 *") == 14.0
    assert abs(evaluar_postfija("2 3 ^ 4 +") - (2**3 + 4)) < 1e-9

def test_rpn_invalid():
    try:
        evaluar_postfija("3 +")
        assert False, "Debe fallar por operandos insuficientes"
    except ValueError:
        pass
