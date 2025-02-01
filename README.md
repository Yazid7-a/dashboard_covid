Dashboard COVID-19

Descripción

Dashboard COVID-19 es un proyecto interactivo diseñado para visualizar datos relacionados con la pandemia de COVID-19 en diferentes provincias. Este dashboard permite analizar tendencias clave, como defunciones, nuevos casos, hospitalizaciones y pacientes en UCI. Es una herramienta intuitiva que combina visualizaciones de datos en tiempo real con una interfaz de usuario sencilla y funcional.

Este proyecto fue desarrollado como parte de un Trabajo de Fin de Grado (TFG).

Características principales

Visualización interactiva: Explora múltiples métricas clave, como defunciones, casos nuevos, hospitalizaciones y pacientes en UCI.

Gráficos dinámicos: Visualizaciones disponibles en formato de barras y pastel interactivo.

Fácil navegación: Opciones seleccionables desde una barra lateral.

Análisis rápido: Identifica las provincias con valores máximos y mínimos en cada métrica.

Procesamiento eficiente: Los datos se agrupan y procesan automáticamente desde un archivo CSV a formato JSON.

Tecnologías utilizadas

Python 3.13: Lenguaje principal utilizado para desarrollar el proyecto.

Streamlit: Herramienta para crear dashboards interactivos y fáciles de usar.

Plotly: Biblioteca de visualización interactiva para crear gráficos avanzados.

Pandas: Para el procesamiento y manipulación de datos.

Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

Python 3.13 o superior.

Las siguientes bibliotecas de Python:

streamlit
plotly
pandas

Puedes instalar las dependencias ejecutando:

pip install -r requirements.txt

Instalación y ejecución

Sigue los pasos a continuación para configurar y ejecutar el proyecto:

Clona el repositorio:

git clone https://github.com/Yazid7-a/dashboard_covid.git

Accede al directorio del proyecto:

cd dashboard_covid

Instala las dependencias necesarias:

pip install -r requirements.txt

Ejecuta el dashboard:

streamlit run dashboard.py

Interactúa con el dashboard: Abre el enlace que aparecerá en la terminal (generalmente: http://localhost:8501) y selecciona las opciones deseadas desde la barra lateral.

Estructura del proyecto

El proyecto está organizado de la siguiente manera:

.
├── data
│   ├── Proyecto_3.csv            # Archivo CSV original con los datos
│
├── output
│   ├── data_grouped.json         # Archivo JSON procesado y agrupado
│
├── scripts
│   ├── data_processing.py        # Procesamiento de datos CSV a JSON
│   ├── visualization.py          # Funciones para generar gráficos
│   ├── dashboard.py              # Archivo principal del dashboard
│
├── README.md                     # Documentación del proyecto
├── requirements.txt              # Lista de dependencias

Uso del dashboard

Selecciona una métrica a visualizar desde la barra lateral:

Defunciones

Casos nuevos

Hospitalizados

Pacientes en UCI

Selecciona el tipo de gráfico:

Barras

Pastel interactivo

Analiza las visualizaciones y los valores máximos y mínimos para cada métrica.

Contribución

Si deseas contribuir a este proyecto:

Abre un issue para informar errores o sugerir mejoras.

Realiza un fork del repositorio y envía un pull request.

Autor

Yazid Ikoubaane Slafti

Correo: yazidslafti7@gmail.com

GitHub: Yazid7-a

Licencia

Este proyecto está licenciado bajo la licencia MIT. Puedes consultar el archivo LICENSE para más detalles.