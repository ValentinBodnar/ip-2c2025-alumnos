# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

# Merge Sort - version iterativa (bottom-up)
# En lugar de dividir recursivamente, arranco con bloques chicos (tamaño 1)
# y los voy mezclando de a pares. Despues duplico el tamaño y repito.
# Asi voy: 1 -> 2 -> 4 -> 8 -> ... hasta que el bloque sea todo el array.

items = []
n = 0

# variables para controlar que bloques estoy procesando
tam_bloque = 1    # tamaño actual de los bloques que estoy mezclando
izq = 0           # inicio del primer bloque
med = 0           # fin del primer bloque (y comienzo del segundo)
der = 0           # fin del segundo bloque

# para mezclar uso una estrategia simple:
# calculo como deberia quedar el segmento ordenado (lo guardo en "objetivo")
# y voy haciendo swaps de a uno para alcanzar ese estado
fase = 0          # me dice en que etapa estoy: 0=preparar, 1=calcular, 2=mezclar
pos = 0           # posicion actual dentro del segmento que estoy ordenando
objetivo = []     # aca guardo como tiene que quedar el segmento


def init(vals):
    global items, n, tam_bloque, izq, med, der, fase, pos, objetivo

    items = list(vals)
    n = len(items)

    # si tiene 0 o 1 elemento, ya esta ordenado
    if n <= 1:
        return

    # empiezo con bloques de tamaño 1
    tam_bloque = 1
    izq = 0
    med = 0
    der = 0
    fase = 0
    pos = 0
    objetivo = []


def step():
    global items, n, tam_bloque, izq, med, der, fase, pos, objetivo

    # array vacio o de 1 elemento ya esta listo
    if n <= 1:
        return {"done": True}

    # FASE 0: preparar el siguiente par de bloques para mezclar
    if fase == 0:
        # si el tamaño de bloque llego al tamaño del array, termine
        if tam_bloque >= n:
            return {"done": True}

        # si procese todos los bloques de este nivel, paso al siguiente
        if izq >= n:
            tam_bloque *= 2  # duplico el tamaño de bloque
            izq = 0          # arranco de nuevo desde el principio
            return step()    # llamo de vuelta para seguir

        # configuro los limites de los bloques a mezclar
        med = min(izq + tam_bloque, n)      # hasta donde llega el bloque izq
        der = min(izq + tam_bloque * 2, n)  # hasta donde llega el bloque der

        # si no hay bloque derecho, paso al siguiente par
        if med >= n or izq >= der:
            izq += tam_bloque * 2  # salto al siguiente par de bloques
            return step()

        # listo para calcular el objetivo
        fase = 1
        return {"a": izq, "b": med if med < n else n - 1, "swap": False, "done": False}

    # FASE 1: calcular como deberia quedar el segmento ordenado
    if fase == 1:
        # simplemente ordeno el segmento completo y lo guardo
        objetivo = sorted(items[izq:der])
        pos = izq  # empiezo desde el inicio del segmento
        fase = 2   # paso a la fase de mezclar
        return {"a": pos, "b": der - 1, "swap": False, "done": False}

    # FASE 2: ir haciendo swaps hasta alcanzar el objetivo
    if fase == 2:
        # si llegue al final del segmento, paso al siguiente par de bloques
        if pos >= der:
            izq += tam_bloque * 2
            fase = 0
            return step()

        # si el elemento ya esta donde tiene que estar, avanzo
        if items[pos] == objetivo[pos - izq]:
            pos += 1
            return {"a": pos - 1, "b": pos - 1, "swap": False, "done": False}

        # busco donde esta el elemento que deberia ir en esta posicion
        idx_correcto = None
        for k in range(pos + 1, der):
            if items[k] == objetivo[pos - izq]:
                idx_correcto = k
                break

        # si no lo encuentro (raro, pero por las dudas), avanzo
        if idx_correcto is None:
            pos += 1
            return {"a": pos - 1, "b": pos - 1, "swap": False, "done": False}

        # hago un swap adyacente para acercar el elemento a su lugar
        # esto es como ir "burbujeando" el elemento hacia donde tiene que ir
        items[idx_correcto - 1], items[idx_correcto] = items[idx_correcto], items[idx_correcto - 1]

        return {"a": idx_correcto - 1, "b": idx_correcto, "swap": True, "done": False}

    return {"done": True}
