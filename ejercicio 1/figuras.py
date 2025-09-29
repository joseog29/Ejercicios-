class Figura:
    def __init__(self, color: str):
        self.color = color
    def __str__(self) -> str:
        return f'Color = "{self.color}"'

class Circulo(Figura):
    def __init__(self, color: str, diametro: float):
        super().__init__(color)
        self.diametro = diametro
    def __str__(self) -> str:
        return f'{super().__str__()}\nDiámetro = {self.diametro}'

class Cuadrado(Figura):
    def __init__(self, color: str, longitud: float):
        super().__init__(color)
        self.longitud = longitud
    def __str__(self) -> str:
        return f'{super().__str__()}\nLongitud = {self.longitud}'