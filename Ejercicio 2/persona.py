class Persona:
    def __init__(self, nombre: str, apellido: str, sexo: str,
                 apellido_nacimiento: Optional[str] = None):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.apellido_nacimiento = apellido_nacimiento

        self.conyuge: Optional[Persona] = None
        self.progenitores: List[Persona] = []
        self.hijos: List[Persona] = []

    def __str__(self) -> str:
        base = [f"Nombre = \"{self.nombre}\"",
                f"Apellido = \"{self.apellido}\"",
                f"Sexo = \"{self.sexo}\""]
        if self.apellido_nacimiento:
            base.insert(2, f"Apellido Nacimiento = \"{self.apellido_nacimiento}\"")
        return "\n".join(base)

    # --- Relaciones ---
    def casarse_con(self, otra: Persona) -> None:
        # Rompemos relaciones previas si existieran (modelo simple, 1 cónyuge)
        if self.conyuge is not None:
            self.conyuge.conyuge = None
        if otra.conyuge is not None:
            otra.conyuge.conyuge = None
        self.conyuge = otra
        otra.conyuge = self

    def anadir_hijo(self, hijo: Persona) -> None:
        if hijo not in self.hijos:
            self.hijos.append(hijo)
        if self not in hijo.progenitores and len(hijo.progenitores) < 2:
            hijo.progenitores.append(self)

    def es_hijo_de(self, p1: Persona, p2: Optional[Persona] = None) -> None:
        # Atajo para rellenar la relación en ambos sentidos de forma clara
        for p in (p1, p2) if p2 else (p1,):
            if p is not None:
                p.anadir_hijo(self)
