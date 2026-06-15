
# Programa 1: Gestión de Mascotas - Programación Tradicional
# Utiliza variables y funciones (sin clases ni objetos)
# ============================================================

def registrar_mascota():
    """Solicita los datos de la mascota por teclado y los retorna."""
    print("=== Registro de Mascota ===")

    # Solicitar datos al usuario mediante teclado
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (perro, gato, etc.): ")
    edad = int(input("Ingrese la edad en años: "))  # Convertir a entero

    # Retornar los datos ingresados
    return nombre, especie, edad


def mostrar_informacion(nombre, especie, edad):
    """Muestra la información de la mascota de forma organizada."""
    print("\n=== Información de la Mascota ===")
    print(f"Nombre  : {nombre}")
    print(f"Especie : {especie}")
    print(f"Edad    : {edad} años")
    print("=================================")


# ── Programa principal ──────────────────────────────────────
# Llamar a la función de registro y recibir los datos
nombre, especie, edad = registrar_mascota()

# Mostrar la información registrada
mostrar_informacion(nombre, especie, edad)