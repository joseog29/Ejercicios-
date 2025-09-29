# perro.py
class Perro:
    def __init__(self, nombre, color, raza, alto, largo, peso):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        self.alto = alto
        self.largo = largo
        self.peso = peso

    def dormir(self):
        return f"{self.nombre} se ha dormido."

    def recostarse(self):
        return f"{self.nombre} se ha acostado."

    def meneo(self):
        return f"{self.nombre} está meneando la cola."

    def venir(self):
        return f"{self.nombre} ha venido."



   


