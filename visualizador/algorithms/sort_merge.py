# Merge Sort (iterativo por tamaños de bloque)
# Implementación por micro-pasos compatible con la UI.
# Durante el merge se usan swaps adyacentes para mover el elemento del bloque derecho
# hacia la posición correcta en el bloque izquierdo; de ese modo cada llamada a step
# puede devolver swap=True cuando realiza un intercambio físico en 'items'.

items = []
n = 0
# Estado para merge sort iterativo usando objetivo temporal por segmento
width = 0
left = 0
mid = 0
right = 0
phase = 0  # 0: iniciar/ajustar width, 1: preparar merge (compute target), 2: aplicar swaps para alcanzar target, 3: avanzar
# dentro del segmento
p = 0       # posición actual en el segmento que queremos fijar
q = None    # índice en uso para desplazamiento durante shifting
target = None  # lista objetivo para el segmento [left:right)

def init(vals):
    global items, n, width, left, mid, right, phase, p, q, target
    items = list(vals)
    n = len(items)
    width = 1
    left = 0
    mid = 0
    right = 0
    phase = 0
    p = 0
    q = None
    target = None

def step():
    """Un micro-paso que realiza un único swap adyacente o una comparación informativa.

    Implementación:
    - Para cada width se procesan segmentos [left:left+width) y [left+width:left+2*width)
    - Para el merge se calcula el `target` = sorted(items[left:right]) y luego se aplica la transformación
      hacia `target` usando swaps adyacentes; cada swap es un micro-paso con swap=True.
    - Esto garantiza que no hay índices fuera de rango y que el merge produce el resultado correcto.
    """
    global width, left, mid, right, phase, p, q, target

    if n <= 1:
        return {"done": True}

    # iniciar/ajustar width
    if phase == 0:
        if width >= n:
            return {"done": True}
        left = 0
        mid = min(left + width, n)
        right = min(left + 2 * width, n)
        target = None
        p = left
        q = None
        phase = 1
        return {"a": left, "b": mid if mid < n else n-1, "swap": False, "done": False}

    # preparar merge: computar target para el segmento actual
    if phase == 1:
        # si no hay segmento derecho, saltar
        if left >= n or mid >= n or left >= right:
            phase = 3
            return {"a": left, "b": left, "swap": False, "done": False}
        target = list(sorted(items[left:right]))
        p = left
        q = None
        phase = 2
        return {"a": p, "b": right - 1, "swap": False, "done": False}

    # aplicar swaps para alcanzar target
    if phase == 2:
        if p >= right:
            # terminado este segmento
            phase = 3
            return {"a": left, "b": right - 1 if right - 1 >= 0 else 0, "swap": False, "done": False}

        # si ya coincide en la posición p, avanzamos
        if items[p] == target[p - left]:
            prev = p
            p += 1
            return {"a": prev, "b": prev, "swap": False, "done": False}

        # buscar el elemento objetivo en la porción actual
        # (debe existir)
        found = None
        for idx in range(p + 1, right):
            if items[idx] == target[p - left]:
                found = idx
                break
        if found is None:
            # Esto no debería ocurrir, pero para seguridad avanzamos p
            p += 1
            return {"a": p - 1, "b": p - 1, "swap": False, "done": False}

        # realizar un único swap adyacente para acercar found hacia p
        a = found - 1
        b = found
        items[a], items[b] = items[b], items[a]
        # si after swap the element moved into position p, we'll increment p next steps
        return {"a": a, "b": b, "swap": True, "done": False}

    # avanzar al siguiente merge o aumentar width
    if phase == 3:
        left += 2 * width
        if left >= n:
            width *= 2
            phase = 0
            return {"a": 0, "b": 0, "swap": False, "done": False}
        else:
            mid = min(left + width, n)
            right = min(left + 2 * width, n)
            p = left
            target = None
            phase = 1
            return {"a": left, "b": mid if mid < n else n-1, "swap": False, "done": False}

    return {"done": True}