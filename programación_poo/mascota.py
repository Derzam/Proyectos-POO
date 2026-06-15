
# Clase Mascota - Programación Orientada a Objetos
# Define los atributos y métodos que tendrá cada mascota

class Mascota:
    """Clase que representa una mascota con sus datos básicos."""

    def __init__(self, nombre, especie, edad):
        """
        Constructor: se ejecuta al crear un objeto Mascota.
        Inicializa los atributos de la instancia.
        """
        self.nombre = nombre  # Atributo: nombre de la mascota
        self.especie = especie  # Atributo: especie (perro, gato, etc.)
        self.edad = edad  # Atributo: edad en años

    def mostrar_informacion(self):
        """Método que imprime los datos de la mascota de forma organizada."""
        print("\n= Información de la Mascota =")
        print(f"Nombre  : {self.nombre}")
        print(f"Especie : {self.especie}")
        print(f"Edad    : {self.edad} años")
        print("=================================")

    def hacer_sonido(self):
        """Método que imprime el sonido característico según la especie."""

        # Diccionario que asocia cada especie con su sonido
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau miau!",
            "pollo": "¡Pío pío!",
        }

        # Buscar el sonido; si la especie no está en el diccionario, usar "..."
        sonido = sonidos.get(self.especie.lower(), "...")

        print(f"{self.nombre} dice: {sonido}")
