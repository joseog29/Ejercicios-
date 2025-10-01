class Lugar:
    def __init__(self, ciudad: str, comunidad: str, pais: str):
        for campo, nombre in ((ciudad, "ciudad"), (comunidad, "comunidad"), (pais, "pais")):
            if not isinstance(campo, str) or not campo.strip():
                raise ValueError(f"{nombre} debe ser texto no vacío")
        self.ciudad = ciudad.strip()
        self.comunidad = comunidad.strip()
        self.pais = pais.strip()

    def __str__(self) -> str:
        return f'Ciudad = "{self.ciudad}"\nComunidad = "{self.comunidad}"\nPaís = "{self.pais}"'


class EtapaDeConstruccion:
    def __init__(self, fecha_inicio: int, fecha_fin: int | None = None):
        if not isinstance(fecha_inicio, int):
            raise ValueError("fecha_inicio debe ser int (año)")
        if fecha_fin is not None and not isinstance(fecha_fin, int):
            raise ValueError("fecha_fin debe ser int o None")
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self) -> str:
        fin = "nulo" if self.fecha_fin is None else str(self.fecha_fin)
        return f"Fecha inicio = {self.fecha_inicio}\nFecha fin = {fin}"


class Edificio:
    def __init__(
        self,
        nombre: str,
        culto: str,
        consagracion_1: int | None = None,
        consagracion_2: str | None = None,
        fecha_declaracion_bic: int | None = None,
        material_principal: str | None = None,
        estilos: list[str] | None = None,   # <- ¡None en la firma!
        lugar: Lugar | None = None,
        etapas: list[EtapaDeConstruccion] | None = None
    ):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("nombre debe ser texto no vacío")
        self.nombre = nombre.strip()
        self.culto = culto  # podrías validar contra un conjunto permitido

        self.consagracion_1 = consagracion_1
        self.consagracion_2 = consagracion_2
        self.fecha_declaracion_bic = fecha_declaracion_bic
        self.material_principal = material_principal

        # Evitar mutables por defecto: crea SIEMPRE una lista nueva aquí.
        self.estilos = list(estilos) if estilos else []
        self.lugar = lugar
        self.etapas = list(etapas) if etapas else []

    def anadir_etapa(self, etapa: EtapaDeConstruccion) -> None:
        self.etapas.append(etapa)

    def __str__(self) -> str:
        partes = [
            f'Nombre = "{self.nombre}"',
            f'Culto = {self.culto}',
        ]
        if self.consagracion_1 is not None:
            partes.append(f"Fecha primera consagración = {self.consagracion_1}")
        if self.consagracion_2 is not None:
            partes.append(f"Fecha segunda consagración = {self.consagracion_2}")
        if self.fecha_declaracion_bic is not None:
            partes.append(f"Fecha declaración BIC = {self.fecha_declaracion_bic}")
        if self.material_principal is not None:
            partes.append(f"Material = {self.material_principal}")
        if self.estilos:
            partes.append(f"Estilo = {', '.join(self.estilos)}")
        return "\n".join(partes)
