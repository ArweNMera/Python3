import math

class ConvertidorAngulo:
    def __init__(self, valor):
        self.valor = valor

    def grados_a_radianes(self):
        """Convierte el valor de grados a radianes."""
        return self.valor * (math.pi / 180)

    def radianes_a_grados(self):
        """Convierte el valor de radianes a grados."""
        return self.valor * (180 / math.pi)

if __name__ == "__main__":
    # Menú para que el usuario elija la conversión
    print("Selecciona la conversion:")
    print("1. Grados a Radianes")
    print("2. Radianes a Grados")
    opcion = int(input("Ingrese la opcion (1 o 2): "))

    if opcion == 1:
        valor_grados = float(input("Ingrese el valor en grados: "))
        convertidor = ConvertidorAngulo(valor_grados)
        radianes = convertidor.grados_a_radianes()
        print(f"{valor_grados} grados son {radianes:.4f} radianes.")
    elif opcion == 2:
        valor_radianes = float(input("Ingrese el valor en radianes: "))
        convertidor = ConvertidorAngulo(valor_radianes)
        grados = convertidor.radianes_a_grados()
        print(f"{valor_radianes} radianes son {grados:.4f} grados.")
    else:
        print("Opcion no válida. Por favor, elija 1 o 2.")
