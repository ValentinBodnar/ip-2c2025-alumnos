# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # arrancar en el segundo elemento
    j = None

def step():
    global items, n, i, j

    if i >= n:
        return {"done": True}

    if j is None:
        j = i
        return {"a": j-1, "b": j, "swap": False, "done": False}

    if j > 0 and items[j-1] > items[j]:
        items[j-1], items[j] = items[j], items[j-1]
        j -= 1
        return {"a": j, "b": j+1, "swap": True, "done": False}

    i += 1
    j = None
    return {"a": i-1, "b": i, "swap": False, "done": False}
