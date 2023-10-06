<div style="text-align:center; color:#FCCf33;"> 
  <h1>Data Analytics</h1>
</div>

<div style="text-align:center;"> 
  <h2>Proyecto Individual N°2 - Data Science Part Time (Henry BootCamp)</h2>
</div>

<p align="center">
  <img src="src/siniestro.jpeg"  height=300>
</p>

# Autor
### Ing. Fernando G. Cofone
<br>


<!-- Enlaces -->
<h3>Enlaces</h3>
<hr>
<table align="center" border="0" style="border-collapse: collapse;">
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/fcofone" style="margin: 0 5px; display: inline-block; padding: 5px; border-radius: 5px;">
        <img src="src/linkedin.png" alt="LinkedIn" width="75" height="75">
        <br>Mi LinkedIn
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/fercof87/PI_DATA_ANALYTICS" style="margin: 0 5px; display: inline-block; padding: 5px; border-radius: 5px;">
        <img src="src/github.png" alt="GitHub" width="75" height="75">
        <br>GitHub
      </a>
    </td>
  </tr>
</table>
<hr>
<br>

## Descripción del Problema a Resolver

### <span style="color: #ff5733;">Contexto</span>

<p style="text-align: justify;">
Este proyecto aborda el desafío de crear un Dashboard Interactivo a partir de datos de siniestros viales provenientes del Gobiernos de la Ciudad Autónoma de Buenos Aires.

Los siniestros viales, también conocidos como accidentes de tráfico o accidentes de tránsito, son eventos que involucran vehículos en las vías públicas y que pueden tener diversas causas, como colisiones entre automóviles, motocicletas, bicicletas o peatones, atropellos, choques con objetos fijos o caídas de vehículos. Estos incidentes pueden tener consecuencias que van desde daños materiales hasta lesiones graves o fatales para los involucrados.

Este Dashboard estará centrado en los siniestros que generan **Victimas Mortales**.
</p>

### <span style="color: #ff5733;">Roles a Desempeñar</span>

<p style="text-align: justify;">
En mi rol como <strong>Data Analyst</strong>, me encontré ante el desafío de construir un Dashboard que permita al Gobierno de la Ciudad disponer de información clara y precisa para tomar acciones que lleven a la disminución de los siniestros y muertes. 

En este rol, en primera medida realice un profundo EDA (Análisis Exploratorio De Los Datos), comprendiendo la estructura y complejidad de los mismos, y preparando los outputs para alimentar el Dashboard mencionado.
</p>

<br></br>

## Etapas del Proyecto


### <span style="color: #ff5733;">1. EDA Preliminar (Análisis Exploratorio de Datos)</span>

<p style="text-align: justify;">
En esta  fase, se llevó a cabo un proceso de Análisis Exploratorio de Datos (EDA) preliminar. El objetivo principal de esta etapa fue cargar los archivos y evaluar su contenido para identificar qué tipo de datos contenían y determinar la calidad de los mismos. Si bien este análisis no fue exhaustivo en su alcance, fue fundamental para obtener una visión general de la información contenida en cada columna y en cada conjunto de datos.

Durante esta tarea de EDA preliminar, se realizó una revisión inicial de las características clave de los archivos, se identificaron las variables relevantes y se obtuvo una comprensión inicial de la estructura y la complejidad de los datos. Este proceso fue esencial para establecer las bases y orientar las acciones posteriores en el proyecto, proporcionando información valiosa sobre el alcance y la naturaleza de los datos con los que se trabajaría.
</p>

### <span style="color: #ff5733;">2. ETL</span>

<p style="text-align: justify;">
Una vez que obtuve una comprensión profunda del vasto conjunto de datos con el que estábamos lidiando, surgió la oportunidad de mejorar significativamente la calidad de los datos llevando a cabo las transformaciones necesarias y aplicando una exhaustiva limpieza de los datos para asegurar un funcionamiento óptimo de nuestro DASHBOARD.

En este proceso mi máxima prioridad fue minimizar al máximo la pérdida de información, incluso trabajando en la reconstrucción de campos en los que la información era especialmente parcial o incompleta. Como resultado de esta etapa logre generar outputs para utilizar como origen de datos en mi dashboard, con datos limpios, bien estructurados y relacionados.
</p>


### <span style="color: #ff5733;">3. Análisis Exploratorio de los Datos (EDA)</span>

<p style="text-align: justify;">
Antes de sumergirnos en el proceso de construcción del tablero en Power BI, se llevó a cabo un análisis exploratorio de datos (EDA) de mayor profundidad. Este proceso fue mucho más que una mera exploración superficial de los datos; implicó una investigación exhaustiva para descubrir relaciones entre variables, detectar la presencia de valores atípicos (outliers) y analizar patrones significativos en el conjunto de datos.

Durante esta etapa avanzada de EDA, se utilizaron diversas técnicas estadísticas y visuales para comprender mejor la estructura y el comportamiento de los datos. Se exploraron las relaciones complejas entre las variables, se identificaron las interacciones clave y se investigaron las causas potenciales de los valores atípicos. Además, se aplicaron transformaciones y ajustes específicos para garantizar que los datos estuvieran en condiciones óptimas para el correcto funcionamiento del DashBoard.

</p>


### <span style="color: #ff5733;">4. DashBoard Interactivo</span>

<p style="text-align: justify;">

He desarrollado un Dashboard con el propósito de brindar a las autoridades locales una herramienta integral para analizar indicadores clave de rendimiento (KPIs) vinculados a la seguridad vial. Este tablero interactivo, construido con Power BI, posibilita la visualización dinámica y la interpretación sencilla de datos cruciales, facilitando así la toma de decisiones informadas.

El enfoque central se orienta a identificar áreas críticas, tendencias y patrones que inciden en los siniestros viales, con el objetivo último de implementar estrategias efectivas que reduzcan la incidencia de accidentes y, en última instancia, preserven vidas. Este dashboard representa un paso significativo hacia la mejora continua de la seguridad vial en la ciudad, proporcionando a los responsables de la toma de decisiones una herramienta potente para impulsar cambios positivos y salvar vidas en nuestras calles.

</p>

### <span style="color: #ff5733;">5. KPIs</span>

<p style="text-align: justify;">
Se tenia como consigna la elaboración de 2 KPIs obligatorios a los cuales he sumado otros dos para hacer un tablero mas completo y robusto para la toma de decisiones por parte de los usuarios del sector/stakeholders.

**El DASHBOARD visualiza los siguientes KPIs:**

- `tasa de homicidios en siniestros viales de los últimos seis meses`: El objetivo es medir la tasa de homicidios semestral, comparando el semestre a analizar con el anterior y evaluar si se ha reducido o no en un 10%. 

- `cantidad de accidentes mortales de motociclistas en el último año`: El objetivo es medir la cantidad anual de accidentes mortales de Motociclistas, comparando el año a analizar con el anterior y evaluar si se ha reducido o no en un 7%. 

- `cantidad de peatones fallecidos  en el último año`: El objetivo es medir la cantidad anual de peatones fallecidos en siniestros viales, comparando el año a analizar con el anterior y evaluar si se ha reducido o no en un 10%. 

- `cantidad de accidentes mortales en Avenidas en el último año`: El objetivo es medir la cantidad anual de accidentes mortales en Avenidas, comparando el año a analizar con el anterior y evaluar si se ha reducido o no en un 7%. 
</p>

### <span style="color: #ff5733;">6. Conclusiones </span>

<p style="text-align: justify;">
Se ha elaborado un documento que encapsula las conclusiones extraídas en cada fase previamente mencionada, centrando especialmente la atención en la utilización y análisis de los indicadores presentes en el Dashboard interactivo. Con el propósito de no exceder las dimensiones previstas para este readme, todas las conclusiones y aproximaciones se encuentran detalladas de manera exhaustiva en dicho documento.
</p>

<table align="center" border="0" style="border-collapse: collapse;">
  <tr>
    <td align="center">
      <a href="https://github.com/fercof87/PI_DATA_ANALYTICS/blob/main/Conclusiones.pdf" style="margin: 0 5px; display: inline-block; padding: 5px; border-radius: 5px;">
        <img src="src/reporte.png" alt="Render" width="75" height="75">
        <br>Conclusiones
      </a>
    </td>
  </tr>
</table>

<br></br>


## Librerías Utilizadas

<p style="text-align: justify;">
  
- **warnings**: Utilizada en la sección de construcción de gráficos para ignorar FutureWarnings.

- **Pandas/Numpy**:  Se utilizó esta librería de Python para el volcado y manipulación de los archivos.

- **Geopandas**:  Se utilizó esta librería para graficar la distribución de los siniestros en las comunas de CABA utilizando el archivo .shp correspondiente (disponible en la carpeta Datos/Shape-Comunas).

- **matplotlib/Seaborn**: Utilizadas para graficar en mi análisis exploratorio (EDA).

- **openpyxl**: Para la lectura y manipulacion de archivos xlsx.

</p>

<br></br>

## Organización del Repositorio

<p style="text-align: justify;">
  
- **Datos**: Aquí están todos los archivos generados en el proceso de ETL/EDA como asi también los inputs de provenientes del Gobierno de la Ciudad Autónoma de Buenos Aires.

- **Funciones**: Conjunto de todas las funciones desarrolladas, las cuales son utilizadas a lo largo del proyecto.

- **Logs**: Algunas funciones generan logs en caso de error. Estos logs son guardados en este folder.

- **EDA.ipynb**: Análisis exploratorio, transformación de datos, imputaciones y generación de archivos a utilizar como origen de datos en POWER BI.

- **Conclusiones.pdf**: Archivo que detalla las conclusiones y aproximaciones derivadas de cada etapa, destacando el análisis de indicadores en el Dashboard interactivo.
  
</p>

<br>
<br>
<br>


<!-- Enlaces -->
<h3>Enlaces</h3>
<hr>
<table align="center" border="0" style="border-collapse: collapse;">
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/fcofone" style="margin: 0 5px; display: inline-block; padding: 5px; border-radius: 5px;">
        <img src="src/linkedin.png" alt="LinkedIn" width="75" height="75">
        <br>Mi LinkedIn
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/fercof87/PI_DATA_ANALYTICS" style="margin: 0 5px; display: inline-block; padding: 5px; border-radius: 5px;">
        <img src="src/github.png" alt="GitHub" width="75" height="75">
        <br>GitHub
      </a>
    </td>
  </tr>
</table>

<hr>
<br>

<table align="center" border="0" style="border-collapse: collapse;">
  <tr>
    <td align="center">
      <div style="color:#FCCf33;"> 
        <p style="text-align: center;">
           <strong>¡Gracias por su interés en mi trabajo!</strong>
        </p>
      </div>
    </td>
  </tr>
</table>
