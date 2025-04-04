import pandas as pd

num_libros = int(input("¿Cuántos libros diferentes deseas registrar? "))

titulos = []
prestamos = []

for i in range(num_libros):
    titulo = input(f"Ingrese el título del libro #{i+1}: ")
    cantidad_prestamos = int(input(f"Ingrese la cantidad de préstamos realizados para '{titulo}': "))
    titulos.append(titulo)
    prestamos.append(cantidad_prestamos)

serie_prestamos = pd.Series(prestamos, index=titulos)

print("\nSerie completa de libros y préstamos:")
print(serie_prestamos)

libro_mas_prestado = serie_prestamos.idxmax()
prestamos_mas = serie_prestamos.max()
print("\nLibro más prestado:")
print(f"'{libro_mas_prestado}' con {prestamos_mas} préstamos")

libro_menos_prestado = serie_prestamos.idxmin()
prestamos_menos = serie_prestamos.min()
print("\nLibro menos prestado:")
print(f"'{libro_menos_prestado}' con {prestamos_menos} préstamos")

total_prestamos = serie_prestamos.sum()
print("\nCantidad total de préstamos realizados en el mes:")
print(total_prestamos)

print("\nClasificación de circulación de los libros:")
for libro, cantidad in serie_prestamos.items():
    if cantidad > 15:
        print(f"El libro '{libro}' tuvo alta circulación con {cantidad} préstamos.")
    else:
        print(f"El libro '{libro}' tuvo baja circulación con {cantidad} préstamos.")
