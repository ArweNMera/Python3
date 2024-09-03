class EvaluadorCalificacion:
    def __init__(self, calificacion):
        self.calificacion = calificacion

    def obtener_calificacion_letra(self):
        """Determina la letra de calificación basada en el valor numérico."""
        if self.calificacion > 9.0:
            return "A"
        elif self.calificacion > 8.0:
            return "B"
        elif self.calificacion >= 7.5:
            return "C"
        else:
            return "R"

    def mostrar_calificacion(self):
        """Muestra la calificación en formato de letra."""
        calificacion_letra = self.obtener_calificacion_letra()
        print(f"La calificación es {calificacion_letra}.")

if __name__ == "__main__":
    # Solicita la calificación al usuario
    try:
        calificacion = float(input("Ingrese la calificación: "))
        evaluador = EvaluadorCalificacion(calificacion)
        evaluador.mostrar_calificacion()
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
