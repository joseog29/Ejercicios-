from perro import Perro

if __name__ == "__main__":
    perro1 = Perro("Bobby", "Cafecito", "Almendrita", "55cm", "60cm", "25kg")
    perro2 = Perro("Luna", "Blanquita", "Verdes", "40cm", "50cm", "15kg")
    perro3 = Perro("Pablito", "Negro", "Cafe", "55cm", "60cm", "25kg")
    perro4 = Perro("Migui", "Chocolate", "Almendrita", "40", "30", "10kg")

    print(perro1.dormir())
    print(perro2.venir())
    print(perro3.recostarse())
    print(perro4.meneo())
