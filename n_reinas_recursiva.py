def _formatear_solucion(pos):
    """pos[r] = columna de la reina en la fila r; devuelve tablero en strings."""
    n = len(pos)
    tablero = []
    for r in range(n):
        fila = ['.'] * n
        fila[pos[r]] = 'Q'
        tablero.append(''.join(fila))
    return tablero


# ----------------- Versión RECURSIVA -----------------
def n_reinas_recursivo(n):
    """
    Backtracking recursivo:
      - cols: columnas ocupadas
      - d1: diagonales r-c
      - d2: diagonales r+c
    """
    soluciones = []
    cols, d1, d2 = set(), set(), set()
    pos = [-1] * n  # para reconstruir el tablero

    def backtrack(r):
        if r == n:
            soluciones.append(_formatear_solucion(pos))
            return
        for c in range(n):
            if c in cols or (r - c) in d1 or (r + c) in d2:
                continue
            pos[r] = c
            cols.add(c); d1.add(r - c); d2.add(r + c)
            backtrack(r + 1)
            cols.remove(c); d1.remove(r - c); d2.remove(r + c)
            pos[r] = -1

    backtrack(0)
    return soluciones