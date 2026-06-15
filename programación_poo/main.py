# ============================================================
# Programa principal - Programación Orientada a Objetos
# Crea objetos de la clase Mascota y ejecuta sus métodos
# ============================================================

# Importar la clase Mascota desde el archivo mascota.py
from mascota import Mascota

# ── Crear objetos (instancias) de la clase Mascota ──────────
# Cada objeto tiene sus propios atributos independientes
mascota1 = Mascota("Rex",   "perro", 3)  # Objeto 1: perro de 3 años
mascota2 = Mascota("Michi", "gato",  5)  # Objeto 2: gato de 5 años

# ── Ejecutar métodos del primer objeto ──────────────────────
mascota1.mostrar_informacion()  # Muestra los datos de Rex
mascota1.hacer_sonido()         # Rex emite su sonido

# ── Ejecutar métodos del segundo objeto ─────────────────────
mascota2.mostrar_informacion()  # Muestra los datos de Michi
mascota2.hacer_sonido()         # Michi emite su sonido
