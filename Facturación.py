class SistemaFacturacionHotel:
    def __init__(self):
        # Tarifas de habitaciones por noche
        self.tarifas_habitaciones = {
            "simple": 50.00,
            "doble": 80.00,
            "suite": 150.00,
            "presidencial": 300.00
        }
        
        # Tarifas de servicios adicionales
        self.tarifas_servicios = {
            "desayuno": 15.00,
            "spa": 40.00,
            "lavanderia": 20.00,
            "minibar": 25.00,
            "transporte": 30.00
        }
        
        self.tasa_impuesto = 0.16  # IVA 16%
    
    def calcular_costo_habitacion(self, tipo_habitacion, numero_noches):
        """Calcula el costo total de la habitación"""
        if tipo_habitacion not in self.tarifas_habitaciones:
            raise ValueError(f"Tipo de habitación '{tipo_habitacion}' no válido")
        
        costo_noche = self.tarifas_habitaciones[tipo_habitacion]
        return costo_noche * numero_noches, costo_noche
    
    def calcular_costo_servicios(self, servicios):
        """Calcula el costo total de servicios adicionales"""
        total_servicios = 0
        desglose = {}
        
        for servicio in servicios:
            if servicio in self.tarifas_servicios:
                costo = self.tarifas_servicios[servicio]
                total_servicios += costo
                desglose[servicio] = costo
        
        return total_servicios, desglose
    
    def generar_factura(self, nombre_cliente, tipo_habitacion, numero_noches, servicios=[]):
        """Genera la factura completa de la reserva"""
        print("\n" + "="*50)
        print("          FACTURA DE RESERVA - HOTEL GRAND")
        print("="*50)
        
        # Datos del cliente
        print(f"\nCliente: {nombre_cliente}")
        print(f"Fecha: {self.obtener_fecha_actual()}")
        
        print("\n" + "-"*50)
        print("DETALLES DE LA RESERVA")
        print("-"*50)
        
        # Calcular costos de habitación
        total_habitacion, costo_noche = self.calcular_costo_habitacion(tipo_habitacion, numero_noches)
        print(f"Tipo de habitación: {tipo_habitacion.capitalize()}")
        print(f"Número de noches: {numero_noches}")
        print(f"Costo por noche: ${costo_noche:.2f}")
        print(f"Total habitación: ${total_habitacion:.2f}")
        
        # Servicios adicionales
        total_servicios, desglose_servicios = self.calcular_costo_servicios(servicios)
        if servicios:
            print("\n" + "-"*50)
            print("SERVICIOS ADICIONALES")
            print("-"*50)
            for servicio, costo in desglose_servicios.items():
                print(f"{servicio.capitalize()}: ${costo:.2f}")
            print(f"Total servicios: ${total_servicios:.2f}")
        
        # Cálculos finales
        subtotal = total_habitacion + total_servicios
        impuestos = subtotal * self.tasa_impuesto
        total_final = subtotal + impuestos
        
        print("\n" + "-"*50)
        print("RESUMEN DE PAGO")
        print("-"*50)
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Impuestos ({int(self.tasa_impuesto * 100)}%): ${impuestos:.2f}")
        print(f"\nTOTAL A PAGAR: ${total_final:.2f}")
        print("="*50 + "\n")
        
        return {
            "cliente": nombre_cliente,
            "tipo_habitacion": tipo_habitacion,
            "numero_noches": numero_noches,
            "total_habitacion": total_habitacion,
            "total_servicios": total_servicios,
            "subtotal": subtotal,
            "impuestos": impuestos,
            "total_final": total_final
        }
    
    def obtener_fecha_actual(self):
        """Retorna la fecha actual"""
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M")
    
    def mostrar_menu(self):
        """Muestra el menú de opciones"""
        print("\n=== TIPOS DE HABITACIÓN DISPONIBLES ===")
        for tipo, precio in self.tarifas_habitaciones.items():
            print(f"{tipo.capitalize()}: ${precio:.2f} por noche")
        
        print("\n=== SERVICIOS ADICIONALES DISPONIBLES ===")
        for servicio, precio in self.tarifas_servicios.items():
            print(f"{servicio.capitalize()}: ${precio:.2f}")


# Ejemplo de uso
def main():
    sistema = SistemaFacturacionHotel()
    
    # Mostrar opciones disponibles
    sistema.mostrar_menu()
    
    # Solicitar datos al usuario
    print("\n" + "="*50)
    print("NUEVA RESERVA")
    print("="*50)
    
    nombre = input("\nIngrese el nombre del cliente: ")
    
    tipo_hab = input("Tipo de habitación (simple/doble/suite/presidencial): ").lower()
    
    while tipo_hab not in sistema.tarifas_habitaciones:
        print("❌ Tipo de habitación no válido")
        tipo_hab = input("Tipo de habitación (simple/doble/suite/presidencial): ").lower()
    
    noches = int(input("Número de noches: "))
    
    # Servicios adicionales
    print("\n¿Desea agregar servicios adicionales? (s/n): ", end="")
    respuesta = input().lower()
    
    servicios = []
    if respuesta == 's':
        print("Ingrese los servicios separados por comas (desayuno,spa,lavanderia,minibar,transporte):")
        servicios_input = input()
        servicios = [s.strip().lower() for s in servicios_input.split(',') if s.strip()]
    
    # Generar factura
    factura = sistema.generar_factura(nombre, tipo_hab, noches, servicios)


if __name__ == "__main__":
    main()

