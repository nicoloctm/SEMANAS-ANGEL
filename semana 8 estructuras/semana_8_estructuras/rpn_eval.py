def evaluar_postfija(expresion: str):
    pila = []
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: a ** b,
        '%': lambda a, b: a % b,
    }
    tokens = expresion.split()
    for token in tokens:
        if token in operadores:
            if len(pila) < 2:
                raise ValueError(f"Expresión inválida: faltan operandos para '{token}'")
            b = pila.pop()
            a = pila.pop()
            pila.append(operadores[token](a, b))
        else:
            try:
                num = float(token)
                pila.append(num)
            except ValueError:
                raise ValueError(f"Token inválido: '{token}'")
    if len(pila) != 1:
        raise ValueError("Expresión inválida: sobran operandos")
    return pila[0]
