# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global i, j, min_idx, fase, items

    # Si ya lo recorrio completa la parte no ordenada
    if i >= n - 1:
        return {"done": True}

    # Buscar el mínimo en la parte no ordenada
    if fase == "buscar":
        # Comparar el actual con el mínimo
        if j < n:
            if items[j] < items[min_idx]:
                min_idx = j
            a, b = min_idx, j
            j += 1
            return {"a": a, "b": b, "swap": False, "done": False}
        else:
            # Terminamos de recorrer la parte no ordenada
            fase = "swap"

    # --- Fase 2: Hacer el swap del mínimo encontrado con la posición i ---
    if fase == "swap":
        if min_idx != i:
            # Intercambio
            items[i], items[min_idx] = items[min_idx], items[i]
            res = {"a": i, "b": min_idx, "swap": True, "done": False}
        else:
            # Si ya estaba en su lugar, no hay swap
            res = {"a": i, "b": min_idx, "swap": False, "done": False}

        # Avanzamos a la siguiente posición y reiniciamos el estado
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"
        ##return {"done": True}
        return res