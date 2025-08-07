import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Verificar si el archivo existe
clientes = 'clientes_electronica.csv'
if os.path.exists(clientes):
    print(f"Archivo '{clientes}' encontrado")
else:
    print(f"Archivo '{clientes}' no encontrado")
    print("Asegúrate de que el archivo esté en el directorio actual")

#============================================================
# BLOQUE 1: EJERCICIOS BÁSICOS DE PANDAS (FAMILIARIZACIÓN)
#============================================================
print("\n" + "="*60)
print("BLOQUE 1: EJERCICIOS BÁSICOS DE PANDAS")
print("="*60)

# 1. Cargar y Explorar
print("\n1. CARGAR Y EXPLORAR")
print("-" * 30)

# Cargar el archivo
df_tienda = pd.read_csv(clientes)
print("DataFrame cargado exitosamente")

# Primeras 7 filas
print("\nPrimeras 7 filas:")
print(df_tienda.head(7))

# Últimas 3 filas
print("\nÚltimas 3 filas:")
print(df_tienda.tail(3))

# Columnas del DataFrame
print("\nColumnas del DataFrame:")
print(df_tienda.columns.tolist())

# Forma del DataFrame
print(f"\nForma del DataFrame (filas, columnas): {df_tienda.shape}")

# Resumen estadístico
print("\nResumen estadístico de columnas numéricas:")
print(df_tienda.describe())

# 2. Selección de Columnas
print("\n2. SELECCIÓN DE COLUMNAS")
print("-" * 30)

# Seleccionar Nombre y Apellido
print("\nColumnas 'Nombre' y 'Apellido':")
print(df_tienda[['Nombre', 'Apellido']])

# Seleccionar Producto Comprado
print("\nColumna 'Producto Comprado':")
print(df_tienda['Producto Comprado'])

# 3. Filtrado de Filas (Condiciones Simples)
print("\n3. FILTRADO DE FILAS")
print("-" * 30)

# Clientes de Rosario
print("\nClientes de Rosario:")
clientes_rosario = df_tienda[df_tienda['Ciudad'] == 'Rosario']
print(clientes_rosario)

# Productos con precio mayor a $1000
print("\nProductos con precio mayor a $1000:")
productos_caros = df_tienda[df_tienda['Precio Producto'] > 1000]
print(productos_caros)

# Clientes menores a 30 años
print("\nClientes menores a 30 años:")
clientes_jovenes = df_tienda[df_tienda['Edad'] < 30]
print(clientes_jovenes)

# ================================================================
# BLOQUE 2: EJERCICIOS INTERMEDIOS DE PANDAS
# ================================================================

print("\n" + "="*60)
print("BLOQUE 2: EJERCICIOS INTERMEDIOS DE PANDAS")
print("="*60)

# 1. Crear una Columna Derivada
print("\n1. CREAR COLUMNA DERIVADA")
print("-" * 30)

# Crear columna 'Venta Total'
df_tienda['Venta Total'] = df_tienda['Precio Producto'] * df_tienda['Cantidad']
print("Columna 'Venta Total' creada")

# Mostrar primeras filas para verificar
print("\nPrimeras filas con la nueva columna:")
print(df_tienda[['Producto Comprado', 'Precio Producto', 'Cantidad', 'Venta Total']].head())

# 2. Agrupaciones Simples
print("\n2. AGRUPACIONES SIMPLES")
print("-" * 30)

# Suma total de Cantidad por Producto Comprado
print("\nCantidad total vendida por producto (ordenado descendente):")
cantidad_por_producto = df_tienda.groupby('Producto Comprado')['Cantidad'].sum().sort_values(ascending=False)
print(cantidad_por_producto)

# Promedio de Edad por Ciudad
print("\nPromedio de edad por ciudad:")
edad_promedio_ciudad = df_tienda.groupby('Ciudad')['Edad'].mean()
print(edad_promedio_ciudad)

# Venta Total por Ciudad
print("\nVenta Total por ciudad (ordenado descendente):")
venta_total_ciudad = df_tienda.groupby('Ciudad')['Venta Total'].sum().sort_values(ascending=False)
print(venta_total_ciudad)

# 3. Filtrado Combinado
print("\n3. FILTRADO COMBINADO")
print("-" * 30)

# Clientes de Mendoza que compraron más de 2 unidades
print("\nClientes de Mendoza que compraron más de 2 unidades:")
mendoza_mas_2 = df_tienda[(df_tienda['Ciudad'] == 'Mendoza') & (df_tienda['Cantidad'] > 2)]
print(mendoza_mas_2)

# Productos comprados por clientes de Buenos Aires mayores a 40 años
print("\nProductos comprados por clientes de Buenos Aires mayores a 40 años:")
ba_mayores_40 = df_tienda[(df_tienda['Ciudad'] == 'Buenos Aires') & (df_tienda['Edad'] > 40)]
print(ba_mayores_40[['Nombre', 'Apellido', 'Edad', 'Producto Comprado']])

# ================================================================
# BLOQUE 3: EJERCICIOS DE VISUALIZACIÓN CON MATPLOTLIB
# ================================================================

print("\n" + "="*60)
print("BLOQUE 3: VISUALIZACIÓN CON MATPLOTLIB")
print("="*60)

# Configurar el estilo de matplotlib
plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 8)

# 1. Gráfico de Barras - Ventas por Ciudad
print("\n1. GRÁFICO DE BARRAS - VENTAS POR CIUDAD")
print("-" * 40)

plt.figure(figsize=(10, 6))
venta_total_ciudad.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Ventas Totales por Ciudad', fontsize=16, fontweight='bold')
plt.xlabel('Ciudad', fontsize=12)
plt.ylabel('Venta Total ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# 2. Gráfico de Barras - Productos Más Vendidos
print("\n2. GRÁFICO DE BARRAS - TOP 5 PRODUCTOS MÁS VENDIDOS")
print("-" * 50)

plt.figure(figsize=(12, 6))
top_5_productos = cantidad_por_producto.head(5)
top_5_productos.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Top 5 Productos Más Vendidos por Cantidad', fontsize=16, fontweight='bold')
plt.xlabel('Producto', fontsize=12)
plt.ylabel('Cantidad Vendida', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# 3. Gráfico de Torta - Distribución de Clientes por Ciudad (Top 3)
print("\n3. GRÁFICO DE TORTA - TOP 3 CIUDADES CON MÁS CLIENTES")
print("-" * 50)

clientes_por_ciudad = df_tienda['Ciudad'].value_counts().head(3)
plt.figure(figsize=(8, 8))
plt.pie(clientes_por_ciudad.values, labels=clientes_por_ciudad.index, autopct='%1.1f%%', 
        startangle=90, colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Distribución de Clientes por Ciudad (Top 3)', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.show()

# ================================================================
# BLOQUE 4: EJERCICIO FINAL - ANÁLISIS INTEGRADO
# ================================================================

print("\n" + "="*60)
print("BLOQUE 4: ANÁLISIS INTEGRADO")
print("="*60)

# Ventas por Grupo de Edad y por Producto Clave
print("\n1. ANÁLISIS POR GRUPO DE EDAD Y PRODUCTOS CAROS")
print("-" * 45)

# 1 Crear columna 'Grupo de edad'
bins_edad = [0, 25, 40, 60, 100]
labels_edad = ["Menor de 25 años", "25-40 años", "41-60 años", "Mayor de 60 años"]
df_tienda["Grupo de Edad"] = pd.cut(df_tienda["Edad"], bins=bins_edad, labels=labels_edad, right=False)

# 2 Identificar top 3 de los productos mas caros vendidos
productos_unicos = df_tienda.drop_duplicates(subset=["Producto Comprado"])
top_3_productos_caros_df = productos_unicos.nlargest(3, "Precio Producto")
nombres_productos_caros = top_3_productos_caros_df["Producto Comprado"].tolist()
print(f"\n El top 3 de productos mas caros es : {nombres_productos_caros}")

# 3 Filtrar el DataFrame para incluir solo estos productos caros
df_productos_caros = df_tienda[df_tienda["Producto Comprado"].isin(nombres_productos_caros)]

# 4 Calcular la venta total de estos productos por grupo de edad
ventas_por_producto_y_edad = df_productos_caros.groupby(["Grupo de Edad", "Producto Comprado"],
                                                         observed=True)["Venta Total"].sum()

# Asegurar que todos los grupos de edad esten presentes, por si uno falta por agrupacion
# ademas es util para ver si un grupo no compro uno de los productos caros
#ventas_por_producto_y_edad = ventas_por_producto_y_edad.reindex(labels_edad, axis=0)
#la deje comentada porque si esta activa no me muestra el grafico, me diria el error que cometi?

# 5 Visualizacion de Grafico de barras agrupada
plt.figure(figsize= (14,8))
ventas_por_producto_y_edad.plot(kind='bar', figsize = (14,8), colormap= 'viridis')
plt.title("Ventas Totales del Top 3 de Productos mas caros por Grupo de edad")
plt.xlabel('Grupo de Edad')
plt.ylabel('Venta Total($)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.legend(title='Producto Comprado')
plt.show()

