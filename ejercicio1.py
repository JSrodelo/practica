import pandas as pd

ventas_mensuales = pd.Series(
    [2100, 1300, None, 2800, 1900, None],
    index=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
)

print("Serie original de ventas durante estos meses:")
print(ventas_mensuales)

print("\nDatos faltantes (NaN): El mes de marzo y junio no tienen datos.")

promedio_sin_nan = ventas_mensuales.dropna().mean()
ventas_mensuales.fillna(promedio_sin_nan, inplace=True)
print("\nSerie luego del tratamiento de los datos faltantes:")
print(ventas_mensuales)

ventas_ordenadas = ventas_mensuales.sort_values()
print("\nVentas ordenadas de menor a mayor:")
print(ventas_ordenadas)

promedio_ventas = ventas_mensuales.mean()
minimo_ventas = ventas_mensuales.min()
maximo_ventas = ventas_mensuales.max()

print("\nEstadísticas básicas de las ventas:")
print(f"Promedio de ventas: {promedio_ventas:.2f}")
print(f"Venta mínima: {minimo_ventas}")
print(f"Venta máxima: {maximo_ventas}")


print("\nMeses con ventas por encima y por debajo del promedio:")
for mes, venta in ventas_mensuales.items():
    if venta > promedio_ventas:
        print(f"{mes}: {venta} (Por encima del promedio)")
    else:
        print(f"{mes}: {venta} (Por debajo del promedio)")
