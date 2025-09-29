def det_iterativo(M, eps=1e-12):
    """
    Determinante por eliminación gaussiana con pivoteo parcial (iterativo).
    - M: lista de listas cuadrada (n x n)
    - eps: umbral para considerar un pivote como cero (evita divisiones numéricamente inestables)
    """
    n = len(M)
    if any(len(f) != n for f in M):
        raise ValueError("La matriz debe ser cuadrada")

    # Copia en float para no modificar el original
    A = [list(map(float, fila)) for fila in M]
    signo = 1.0

    for k in range(n):  # columna k
        # 1) pivoteo parcial: elige el mayor en valor absoluto desde la fila k
        i_max = max(range(k, n), key=lambda i: abs(A[i][k]))
        if abs(A[i_max][k]) < eps:
            return 0.0  # pivote ~ 0 ⇒ determinante 0

        # 2) si hay que, intercambia filas y cambia el signo
        if i_max != k:
            A[k], A[i_max] = A[i_max], A[k]
            signo *= -1.0

        # 3) elimina por debajo del pivote en la columna k
        pivote = A[k][k]
        for i in range(k+1, n):
            factor = A[i][k] / pivote
            # resta factor * (fila k) a la fila i a partir de la columna k
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]

    # 4) el determinante es el producto de la diagonal por el signo acumulado
    det = signo
    for i in range(n):
        det *= A[i][i]
    return det

A = [
    [2, 1, 0, 3],
    [4, -1, 2, 1],
    [0, 5, 3, -2],
    [1, 0, -1, 4]
]
print(det_iterativo(A))
