class OrdenadorNumeros:
    def __init__(self, num1, num2, num3):
        self.numeros = [num1, num2, num3]

    def ordenar(self):
        self.numeros.sort()

    def imprimir_numeros(self):
        for numero in self.numeros:
            print(numero)

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Crear una instancia de la clase OrdenadorNumeros
ordenador = OrdenadorNumeros(num1, num2, num3)

# Ordenar los números
ordenador.ordenar()

# Imprimir los números ordenados
ordenador.imprimir_numeros()
