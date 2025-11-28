# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

# Quick Sort - version iterativa con pila
# La idea es elegir un pivot (el ultimo elemento) y poner todos los menores
# a la izquierda y los mayores a la derecha. Despues repetir con cada mitad.

items = []
n = 0

stack = []       # aca guardo los rangos que me falta ordenar

# estas variables las uso mientras particiono
inicio = 0       # desde donde arranca el rango que estoy ordenando
fin = 0          # hasta donde llega el rango
pivot_val = 0    # el valor del pivot (guardo el valor, no la posicion)
i = 0            # marca hasta donde llegaron los elementos menores que el pivot
j = 0            # voy recorriendo el rango con j

fase = 0         # controla en que parte del proceso estoy


def init(vals):
    global items, n, stack, inicio, fin, pivot_val, i, j, fase

    items = list(vals)
    n = len(items)
    stack = []

    # si hay mas de 1 elemento, meto todo en la pila para empezar
    if n > 1:
        stack.append((0, n - 1))

    # reseteo todo
    inicio = 0
    fin = 0
    pivot_val = 0
    i = 0
    j = 0
    fase = 0


def step():
    global items, n, stack, inicio, fin, pivot_val, i, j, fase

    # si el array tiene 0 o 1 elemento, ya esta ordenado
    if n <= 1:
        return {"done": True}

    # FASE 0: sacar un rango nuevo de la pila para procesar
    if fase == 0:
        # si no quedan rangos, termine
        if not stack:
            return {"done": True}

        inicio, fin = stack.pop()

        # si el rango tiene 1 solo elemento, ya esta ordenado
        if inicio >= fin:
            return {"a": inicio, "b": fin, "swap": False, "done": False}

        # guardo el valor del pivot (es el ultimo del rango)
        pivot_val = items[fin]
        i = inicio  # aca va a empezar la frontera de elementos menores
        j = inicio  # arranco a recorrer desde el inicio

        fase = 1
        # muestro cual es el pivot
        return {"a": j, "b": fin, "swap": False, "done": False}

    # FASE 1: voy recorriendo y moviendo los menores a la izquierda
    if fase == 1:
        # mientras no llegue al pivot, sigo comparando
        if j <= fin - 1:
            # si el elemento actual es menor que el pivot
            if items[j] < pivot_val:
                # lo muevo a la zona de menores (intercambio con i)
                items[i], items[j] = items[j], items[i]
                a = i
                b = j
                i += 1  # avanzo la frontera de menores
                j += 1  # avanzo el cursor
                return {"a": a, "b": b, "swap": True, "done": False}
            else:
                # es mayor o igual, lo dejo donde esta
                a = j
                b = fin  # muestro que lo estoy comparando con el pivot
                j += 1   # solo avanzo el cursor
                return {"a": a, "b": b, "swap": False, "done": False}
        else:
            # llegue al final, ahora pongo el pivot en su lugar definitivo
            items[i], items[fin] = items[fin], items[i]
            pivot_pos = i

            # ahora apilo las dos mitades para ordenarlas despues
            # primero la mitad izquierda (menores que el pivot)
            if inicio < pivot_pos - 1:
                stack.append((inicio, pivot_pos - 1))
            # despues la mitad derecha (mayores que el pivot)
            if pivot_pos + 1 < fin:
                stack.append((pivot_pos + 1, fin))

            fase = 0  # vuelvo a la fase 0 para sacar otro rango
            return {"a": i, "b": fin, "swap": True, "done": False}

    return {"done": True}
