# estadisticas_jugadores.py
# Autor: [Paula Tomás Marco]
# Fecha: 14 de junio de 2025
# Descripción: Mini aplicación para gestionar estadísticas de jugadores de baloncesto

# Lista de jugadores (se guarda en memoria mientras corre el programa)
jugadores = []

# Función que muestra el menú principal
def mostrar_menu():
    print("\n---- MENÚ PRINCIPAL ----")
    print("[1] Introducir un nuevo jugador")
    print("[2] Listar jugadores")
    print("[3] Máximo anotador")
    print("[4] Estadísticas del equipo")
    print("[0] Salir del programa")

# Función para añadir un nuevo jugador
def añadir_jugador():
    print("\n---- Introducir un nuevo jugador ----")
    nombre = input("Introduce nombre: ")
    dorsal = input("Introduce dorsal: ")
    canastas_3 = int(input("Introduce canastas de 3: "))
    canastas_2 = int(input("Introduce canastas de 2: "))
    canastas_1 = int(input("Introduce canastas de 1: "))

    jugador = {
        "nombre": nombre,
        "dorsal": dorsal,
        "c3": canastas_3,
        "c2": canastas_2,
        "c1": canastas_1,
        "total": canastas_3 * 3 + canastas_2 * 2 + canastas_1
    }

    jugadores.append(jugador)
    print("\nJugador añadido con éxito.")
    input("Presiona Enter para volver al menú...")

# Función para mostrar todos los jugadores con puntos totales
def listar_jugadores():
    print("\n---- Listar jugadores ----")
    if len(jugadores) == 0:
        print("No hay jugadores registrados.")
    else:
        for jugador in jugadores:
            nombre = jugador["nombre"]
            dorsal = jugador["dorsal"]
            total = jugador["total"]
            print(f"{nombre}[{dorsal}] ptosTotales[{total}]")
    input("\nPresiona Enter para volver al menú...")

# Función para mostrar al jugador con más puntos
def maximo_anotador():
    print("\n---- Máximo anotador ----")
    if len(jugadores) == 0:
        print("No hay jugadores registrados.")
    else:
        mejor = jugadores[0]
        for jugador in jugadores[1:]:
            if jugador["total"] > mejor["total"]:
                mejor = jugador
        print(f'{mejor["nombre"]}[{mejor["dorsal"]}] ptosTotales[{mejor["total"]}]')
    input("\nPresiona Enter para volver al menú...")

# Función para mostrar estadísticas totales del equipo
def estadisticas_equipo():
    print("\n---- Estadísticas del equipo ----")
    if len(jugadores) == 0:
        print("No hay jugadores registrados.")
    else:
        total_puntos = 0
        total_c3 = 0
        total_c2 = 0
        total_c1 = 0

        for jugador in jugadores:
            total_puntos += jugador["total"]
            total_c3 += jugador["c3"]
            total_c2 += jugador["c2"]
            total_c1 += jugador["c1"]

        print(f"Puntos totales del equipo: {total_puntos}")
        print(f"Canastas de 3 puntos: {total_c3}")
        print(f"Canastas de 2 puntos: {total_c2}")
        print(f"Canastas de 1 punto: {total_c1}")
    input("\nPresiona Enter para volver al menú...")

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            añadir_jugador()
        elif opcion == "2":
            listar_jugadores()
        elif opcion == "3":
            maximo_anotador()
        elif opcion == "4":
            estadisticas_equipo()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Iniciar el programa
main()
