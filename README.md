# Proyecto-Introduccion-ING
# Base de datos simulada de reservas
reservas = {
    "R001": {
        "nombre": "Juan Pérez",
        "habitacion": "101",
        "disponible": True,
        "fecha_entrada": "2026-04-06",
        "fecha_salida": "2026-04-10"
    },
    "R002": {
        "nombre": "María López",
        "habitacion": "205",
        "disponible": False,
        "fecha_entrada": "2026-04-06",
        "fecha_salida": "2026-04-08"
    }
}

# Lista de turistas registrados en check-in
turistas_registrados = []

def verificar_reserva(numero_reserva):
    return numero_reserva in reservas

def verificar_turista(numero_reserva, nombre):
    return reservas[numero_reserva]["nombre"].lower() == nombre.lower()

def habitacion_disponible(numero_reserva):
    return reservas[numero_reserva]["disponible"]

def realizar_checkin(numero_reserva, nombre):
    reserva = reservas[numero_reserva]
    
    # Registrar turista
    turistas_registrados.append({
        "nombre": nombre,
        "reserva": numero_reserva,
        "habitacion": reserva["habitacion"]
    })
    
    # Marcar habitación como ocupada
    reservas[numero_reserva]["disponible"] = False
    
    # Mostrar comprobante
    print("\n===== COMPROBANTE DE CHECK-IN =====")
    print(f"Turista      : {nombre}")
    print(f"N° Reserva   : {numero_reserva}")
    print(f"Habitación   : {reserva['habitacion']}")
    print(f"Fecha entrada: {reserva['fecha_entrada']}")
    print(f"Fecha salida : {reserva['fecha_salida']}")
    print("Check-in realizado con éxito")
    print("===================================\n")

def checkin():
    print("====== SISTEMA DE CHECK-IN ======")
    nombre = input("Ingrese su nombre completo: ")
    numero_reserva = input("Ingrese su número de reserva: ")

    if not verificar_reserva(numero_reserva):
        print("No se encontró ninguna reserva con ese número.")
        return

    if not verificar_turista(numero_reserva, nombre):
        print("El nombre no coincide con la reserva.")
        return

    if not habitacion_disponible(numero_reserva):
        print("La habitación no está disponible aún.")
        print("Por favor, espere o contacte recepción.")
        return

    realizar_checkin(numero_reserva, nombre)

# Ejecutar el sistema
checkin()
