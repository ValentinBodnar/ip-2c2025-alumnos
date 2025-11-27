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

    if i >= n - 1:
        return {"done": True}

    # Defino el par a comparar:
    a = j
    b = j + 1
    swap = False

    # Si están en el orden incorrecto, intercambiamos:
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    # Avanzamos al siguiente par:
    j += 1
    # Completa un ciclo:
    if j >= n - i - 1:
        j = 0
        i += 1
        
    return {"a": a, "b": b, "swap": swap, "done": False}

