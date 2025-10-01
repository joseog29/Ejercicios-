class Figura:
    def __init__(self, color):
        self.color = color

class Circulo(Figura):
    def __init__(self, color, diametro):
        super().__init__(color)
        self.diametro = diametro

class Rectangulo(Figura):
    def __init__(self, color, longitud, anchura):
        super().__init__(color)
        self.longitud = longitud
        self.anchura = anchura

class Cuadrado(Rectangulo):  # El cuadrado ES un rectángulo especial
    def __init__(self, color, lado):
        super().__init__(color, lado, lado)

class Elipse(Figura):
    def __init__(self, color, eje_mayor, eje_menor):
        super().__init__(color)
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
