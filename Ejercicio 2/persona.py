class Persona:
    def __init__(self, nombre, apellido, sexo, apellido_nacimiento=None):
        # Validaciones básicas
        for valor, nom in ((nombre, "nombre"), (apellido, "apellido"), (sexo, "sexo")):
            if not isinstance(valor, str) or not valor.strip():
                raise ValueError(f"{nom} debe ser texto no vacío")

        self.nombre = nombre.strip()
        self.apellido = apellido.strip()
        self.sexo = sexo.strip()
        self.apellido_nacimiento = (apellido_nacimiento.strip()
                                    if isinstance(apellido_nacimiento, str) and apellido_nacimiento.strip()
                                    else None)

        # Relaciones
        self.conyuge = None          # una Persona o None
        self.progenitores = []       # lista de Persona (0..2)
        self.hijos = []              # lista de Persona (0..*)

    def __str__(self):
        partes = [
            f'Nombre = "{self.nombre}"',
            f'Apellido = "{self.apellido}"',
            f'Sexo = "{self.sexo}"'
        ]
        if self.apellido_nacimiento:
            partes.insert(2, f'Apellido Nacimiento = "{self.apellido_nacimiento}"')
        return "\n".join(partes)

    # -------- Relaciones --------
    def casarse_con(self, otra):
        if not isinstance(otra, Persona):
            raise TypeError("conyuge debe ser Persona")
        # Romper vínculos anteriores (modelo simple: 1 cónyuge)
        if self.conyuge is not None:
            self.conyuge.conyuge = None
        if otra.conyuge is not None:
            otra.conyuge.conyuge = None
        self.conyuge = otra
        otra.conyuge = self

    def anadir_hijo(self, hijo):
        if not isinstance(hijo, Persona):
            raise TypeError("hijo debe ser Persona")
        if hijo not in self.hijos:
            self.hijos.append(hijo)
        if self not in hijo.progenitores and len(hijo.progenitores) < 2:
            hijo.progenitores.append(self)

    def es_hijo_de(self, p1, p2=None):
        # Azúcar sintáctico para rellenar ambos lados
        if p1 is not None:
            p1.anadir_hijo(self)
        if p2 is not None:
            p2.anadir_hijo(self)
