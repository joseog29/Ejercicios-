class Perro: 
    def __init__(self, nombre, color, ojos, altura, largo, peso):
        self.nombre = nombre
        self.color = color
        self.ojos = ojos
        self.altura = altura
        self.largo = largo
        self.peso = peso

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_ojos(self):
        return self.ojos

    def set_ojos(self, ojos):
        self.ojos = ojos

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_largo(self):
        return self.largo

    def set_largo(self, largo):
        self.largo = largo

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso

    def dormir(self):
        return f"{self.name} se ha dormido."

    def recostarse(self):
        return f"{self.name} se ha acostado."

    def meneo(self):
        return f"{self.name} está dando la menea"

    def venir(self):
        return f"{self.name} ha venido."    



   


