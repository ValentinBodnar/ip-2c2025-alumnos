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

def step():
    global items, n, i, j
    print(f"Inicio: i={i}, j={j}, items={items}, n={n}")

    # Si ya terminamos todas las pasadas:
    if i >= n - 1:
        return {"done": True}

    # Definimos el par a comparar:
    a = j
    b = j + 1
    swap = False

    # Si están en el orden incorrecto, intercambiamos:
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    # Avanzamos al siguiente par:
    j += 1
    print(f"Validacion swap: i={i}, j={j}, items={items}, swap= {swap}")
    # Completa un ciclo:
    if j >= n - i - 1:
        print(f"Completa recorrido porque: j={j} >= n - i - 1= {n - i - 1} (i={i})")
        j = 0
        i += 1

    print(f"Final: i={i}, j={j}, items={items}, swap= {swap}")
    print("\n")
    return {"a": a, "b": b, "swap": swap, "done": False}

