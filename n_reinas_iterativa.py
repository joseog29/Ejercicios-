def _formatear_solucion(pos):
    """pos[r] = columna de la reina en la fila r; devuelve tablero en strings."""
    n = len(pos)
    tablero = []
    for r in range(n):
        fila = ['.'] * n
        fila[pos[r]] = 'Q'
        tablero.append(''.join(fila))
    return tablero

def n_reinas_iterativo(n):
    """
    Backtracking iterativo (sin recursión).
    Usa un vector pos y avanza/retrocede filas buscando la
    siguiente columna válida.
    """
    soluciones = []
    pos = [-1] * n
    r = 0  # fila actual

    while r >= 0:
        # prueba siguiente columna en la fila r
        pos[r] += 1

        # avanza hasta una columna válida o hasta salir del tablero
        while pos[r] < n and any(
            pos[r] == pos[k] or abs(pos[r] - pos[k]) == r - k
            for k in range(r)
        ):
            pos[r] += 1

        if pos[r] < n:
            if r == n - 1:
                # solución completa en pos
                soluciones.append(_formatear_solucion(pos))
                # sigue buscando en la misma fila (probar siguiente columna)
            else:
                # baja a la siguiente fila
                r += 1
                pos[r] = -1
        else:
            # no hay columna válida en esta fila; retrocede
            pos[r] = -1
            r -= 1

    return soluciones


