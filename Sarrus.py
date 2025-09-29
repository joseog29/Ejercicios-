def sarrus(A):
    """
    Determinante de una matriz 3x3 usando la regla de Sarrus.
    A es una lista de listas 3x3.
    """
    a,b,c = A[0]
    d,e,f = A[1]
    g,h,i = A[2]
    pos = a*e*i + b*f*g + c*d*h
    neg = c*e*g + b*d*i + a*f*h
    return pos - neg

def submatriz(M, fila, col):
    """Devuelve la submatriz al eliminar la 'fila' y la columna 'col'."""
    return [ [ M[r][c] for c in range(len(M)) if c != col ]
             for r in range(len(M)) if r != fila ]

def det_recursivo(M):
    """
    Determinante recursivo:
      - n=1: elemento
      - n=2: ad - bc
      - n=3: Sarrus
      - n>3: expansión por cofactores (primera fila)
    """
    n = len(M)
    if any(len(fila) != n for fila in M):
        raise ValueError("La matriz debe ser cuadrada")

    if n == 1:
        return M[0][0]
    if n == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    if n == 3:
        return sarrus(M)

    # Expansión por cofactores sobre la primera fila
    total = 0
    for j, a_1j in enumerate(M[0]):
        if a_1j == 0:
            continue  # pequeño ahorro
        signo = -1 if (0 + j) % 2 else 1
        minor = submatriz(M, 0, j)
        total += signo * a_1j * det_recursivo(minor)
    return total
