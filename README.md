# Python-para-análisis-de-datos-csv
El trabajo tiene como finalidad aplicar lo aprendido en el cursado de Python, en este caso el análisis de datos por medio de las librerías Pandas y Matplotlib. También se incorpora el uso del módulo OS para la verificación del archivo objeto del análisis.

# Tecnologías usadas
## Python
### Inicio
Aca se redacta todo el código del análisis, lo primero que se realizó fue la declaración de librerías y métodos a usar. Luego usamos el módulo OS para verificar la ruta del archivo csv y que se encontrara en la misma carpeta que mi archivo python. Por medio de un condicional mandamos un mensaje a la terminal si el archivo fue encontrado o no.
### Familiarización
A continuación se procede a realizar un análisis básico para familiarizarnos con la librería Pandas, dentro de ello cargamos el archivo csv, pedimos las primeras 7 filas, las últimas 3, los nombres de las columnas, la forma que tiene, y un resumen estadístico de la base de datos o Dataframe. Después procedemos a separar columnas y filtrar información por filas.
### Intermedio
Aca vemos como crear nuevas columnas en el Dataframe, estas derivadas de la combinación de columnas ya existentes. También hacemos un análisis por medio de agrupar columnas con el fin de obtener datos más concretos y específicos, como por ejemplo el promedio de edad de los compradores según la ciudad, o la suma de la cantidad de productos comprados. Además se hace un filtrado combinado, usando la selección de columnas y dándoles dos o más condiciones a cumplir.
## Matplotlib
Primero se establece la configuración que deseamos para los gráficos que nos muestra matplotlib.
### Gráfico de barras
Tenemos dos gráficos uno de ventas por ciudad y otro por top de 5 productos más vendidos. Primero se establece el tamaño de la figura del gráfico, después se redujo todo a las ventas totales por ciudad y un top de 5 productos más vendidos, se le da el tipo de gráfico a usar, color, y un color al borde del gráfico. También se define en nombre del gráfico, el nombre de cada eje y su tamaño de letra, para dar un mejor aspecto visual rotamos los nombres en un ángulo de 45 grados, damos una pequeña cuadrícula para un mejor aspecto y ajustamos los espacios para que no se superponga en el gráfico.
### Gráfico de torta
Procedemos parecido al anterior, filtrando por ciudad, por la cantidad de clientes por ciudad y las tres ciudades con más clientes. Le damos un tamaño al gráfico, indicamos que es un gráfico de torta, al cual le damos parámetros como los valores según la cantidad de clientes, los nombres de las ciudades, que muestre en porcentaje de clientes, como queremos que inicie el gráfico, y los colores a usar. Obviamente le damos un título y un elemento para que el gráfico no se deforme. Además del ajuste automático.
## Análisis Integrado
Se realiza un análisis enfocado solo en el grupo de edad y ventas por productos claves. Hacemos uso de todo lo que se aprendió al inicio del documento, filtrado y creación de columnas, agrupaciones y por último un gráfico.
## Agradecimiento
A los profesores Carolina Riveros y Gustavo Rojas por sus enseñanzas sobre Python y a Punto Digital San Martín por dictar el curso.
