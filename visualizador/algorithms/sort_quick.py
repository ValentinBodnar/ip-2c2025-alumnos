# Quick Sort (Lomuto partition) — implementación por micro-pasos
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
# Estado para Quick Sort
stack = []     # pila de segmentos (lo, hi) pendientes, hi es índice inclusivo
lo = 0
hi = 0
pivot = None
i = 0         # índice i de la partición (posición donde irá el siguiente menor)
j = 0         # índice j que recorre
phase = 0     # 0: obtener segmento, 1: particionar (iterando j), 2: swap pivot y push subsegmentos

def init(vals):
    global items, n, stack, lo, hi, pivot, i, j, phase
    items = list(vals)
    n = len(items)
    stack = []
    if n > 1:
        stack.append((0, n-1))
    lo = 0
    hi = 0
    pivot = None
    i = 0
    j = 0
    phase = 0

def step():
    """Un micro-paso de Quick Sort usando Lomuto partition.

    - Cada comparación entre items[j] y pivot devuelve swap=False
    - Cada intercambio real (items[i] <-> items[j] o swap final con pivot) devuelve swap=True
    - Cuando no hay más segmentos, devuelve {"done": True}
    """
    global items, n, stack, lo, hi, pivot, i, j, phase

    if n <= 1:
        return {"done": True}

    # Obtener siguiente segmento a procesar
    if phase == 0:
        if not stack:
            return {"done": True}
        lo, hi = stack.pop()
        if lo >= hi:
            # segmento trivial: nada que hacer
            return {"a": lo, "b": hi, "swap": False, "done": False}
        # inicializar partición Lomuto
        pivot = items[hi]
        i = lo
        j = lo
        phase = 1
        return {"a": j, "b": hi, "swap": False, "done": False}

    # Fase de partición: recorrer j desde lo..hi-1
    if phase == 1:
        if j <= hi - 1:
            # comparar items[j] con pivot
            if items[j] < pivot:
                # swap items[i] <-> items[j]
                a = i
                b = j
                items[a], items[b] = items[b], items[a]
                i += 1
                j += 1
                return {"a": a, "b": b, "swap": True, "done": False}
            else:
                # no swap, solo avanzamos j
                a = j
                b = hi
                j += 1
                return {"a": a, "b": b, "swap": False, "done": False}
        else:
            # terminar partición: swap items[i] con pivot(items[hi])
            a = i
            b = hi
            items[a], items[b] = items[b], items[a]
            # pivot en su posición final: i
            pivot_index = i
            # agregar subsegmentos pendientes (izquierda y derecha)
            # izquierda: lo..pivot_index-1, derecha: pivot_index+1..hi
            if lo < pivot_index - 1:
                stack.append((lo, pivot_index - 1))
            if pivot_index + 1 < hi:
                stack.append((pivot_index + 1, hi))
            phase = 0
            return {"a": a, "b": b, "swap": True, "done": False}

    return {"done": True}