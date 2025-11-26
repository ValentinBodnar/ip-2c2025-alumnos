# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # inicio de la parte no ordenada
j = 0          # cursor que recorre buscando el mínimo
min_idx = 0    # índice del mínimo en la pasada actual

def init(vals):
    global items, n, i, j, min_idx
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i

def step():
    global items, n, i, j, min_idx

    if i >= n - 1:
        return {"done": True}

    a = min_idx
    b = j
    swap = False

    if j < n:
        if items[j] < items[min_idx]:
            min_idx = j
        j += 1
        return {"a": a, "b": b, "swap": swap, "done": False}
    else:
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            swap = True
        # Pasada completa: avanzamos al inicio de la parte no ordenada
        a, b = i, min_idx
        i += 1
        j = i + 1
        min_idx = i
        return {"a": a, "b": b, "swap": swap, "done": False}