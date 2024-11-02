# Creación de una clase python que representa una matriz.
class Matriz:
    def __init__(self, elementos):
        self.elementos = elementos

    def imprimir(self):
        for fila in self.elementos:
            print(fila)

    def transpuesta(self):
        transpuesta = [[self.elementos[j][i] for j in range(len(self.elementos))] for i in range(len(self.elementos[0]))]
        return Matriz(transpuesta)
    
# Matriz 2x2
m = Matriz([[1, 2], [3, 4]])

# Matriz original
print("Matriz original:")
m.imprimir()

# Matriz transpuesta
print("\nMatriz transpuesta:")
m_transpuesta = m.transpuesta()
m_transpuesta.imprimir()

