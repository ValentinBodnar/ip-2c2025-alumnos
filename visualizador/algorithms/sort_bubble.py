# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j

    # Si ya terminamos todas las pasadas:
    if i >= n - 1:
        return {"done": True}

    # Definimos los índices actuales a comparar:
    a = j
    b = j + 1
    swap = False

    # Si están en el orden incorrecto, intercambiamos:
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    # Avanzamos al siguiente par:
    j += 1

    # Si llegamos al final de esta pasada:
    if j >= n - i - 1:
        j = 0
        i += 1

    # Devolvemos el estado actual del paso:
    return {"a": a, "b": b, "swap": swap, "done": False}
