# Actividad Semana 3 Programacion Tradicional y Programacion Orientada a Objetos

**Estudiante:** Derly Alexander Zambrano Moreira
**Materia:** Programación Orientada a Objetos
**Fecha:** 14 de Junio del 2026

---

## Descripción de los programas

### Programa 1 — Programación Tradicional (`programacion_tradicional/tradicional.py`)

Gestiona la información básica de una mascota utilizando únicamente
variables y funciones. El programa solicita al usuario los datos
(nombre, especie y edad) mediante el teclado, y los muestra de forma
organizada en pantalla. No se utilizan clases ni objetos en ninguna
parte del código.

### Programa 2 — Programación Orientada a Objetos (`programacion_poo/`)

Resuelve el mismo problema utilizando el paradigma orientado a objetos.
El código está dividido en dos archivos:

- **`mascota.py`**: define la clase `Mascota` con sus atributos
  (`nombre`, `especie`, `edad`) y sus métodos (`mostrar_informacion()`
  y `hacer_sonido()`).
- **`main.py`**: importa la clase, crea dos objetos distintos y ejecuta
  los métodos definidos para cada uno.

---

## Reflexión: diferencias encontradas

Al desarrollar ambos programas para resolver el mismo problema noté
diferencias importantes entre los dos enfoques.

En la **Programación Tradicional** los datos y las funciones existen de
forma separada. Las variables que guardan el nombre, la especie y la
edad no tienen ninguna conexión directa con las funciones que las
procesan, simplemente se pasan como parámetros cada vez que se las
necesita. Esto funciona bien para programas pequeños, pero si se
quisiera manejar varias mascotas al mismo tiempo el código se volvería
difícil de organizar y mantener.

En la **Programación Orientada a Objetos**, en cambio, los datos y el
comportamiento están agrupados dentro de la clase `Mascota`. Cada objeto
creado a partir de esa clase lleva consigo su propia información y sabe
exactamente qué hacer con ella a través de sus métodos. Esto hace que
agregar una tercera o cuarta mascota sea tan simple como escribir una
nueva línea, sin modificar nada más.

La diferencia más importante que encontré es la **abstracción**: en POO
el archivo `main.py` no necesita saber cómo funciona internamente
`mostrar_informacion()` ni `hacer_sonido()`; simplemente los llama.
Eso hace el código más legible, más reutilizable y más fácil de ampliar
en el futuro.
## Estructura del proyecto

```
Proyectos-POO/
│
├── README.md
│
├── programacion_tradicional/
│   └── tradicional.py
│
└── programacion_poo/
    ├── main.py
    └── mascota.py
```
