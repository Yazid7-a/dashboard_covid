Dashboard COVID-19
📊 Visualización interactiva de datos COVID-19 en España por provincia.

Descripción del Proyecto
Este dashboard permite visualizar y analizar los datos de COVID-19 en España, proporcionando gráficos interactivos que muestran tendencias por provincia. Utiliza Streamlit para la interfaz y Plotly para la visualización de datos, permitiendo una experiencia intuitiva y dinámica.

🚀 Características
✅ Visualización Interactiva: Gráficos de barras y gráficos de pastel dinámicos con Plotly.
✅ Datos Agrupados: Procesamiento de datos desde CSV a JSON por día de la semana y provincia.
✅ Interfaz Moderna: Desarrollado con Streamlit para una experiencia fluida y en tiempo real.
✅ Análisis Detallado: Identificación de provincias con mayor y menor impacto en cada métrica.
✅ Código Modular: Organización clara con separación de procesamiento de datos y visualización.

📂 Estructura del Proyecto
graphql
Copiar
Editar
dashboard_covid/
│── data/                       # Archivos de datos
│   ├── Proyecto_3.csv          # Archivo CSV con los datos originales
│   ├── data_grouped.json       # Datos procesados en formato JSON
│
│── scripts/                     # Scripts de código
│   ├── data_processing.py       # Procesamiento de datos CSV a JSON
│   ├── visualization.py         # Funciones de visualización (gráficos)
│   ├── dashboard.py             # Interfaz principal con Streamlit
│
│── README.md                    # Documentación del proyecto
│── requirements.txt              # Dependencias necesarias
⚙️ Instalación y Ejecución
1️⃣ Requisitos previos
Tener Python 3.8 o superior instalado.
Instalar Git (opcional, si deseas clonar el repositorio en lugar de descargarlo).
2️⃣ Clonar el repositorio (opcional)
bash
Copiar
Editar
git clone https://github.com/Yazid7-a/dashboard_covid.git
cd dashboard_covid
3️⃣ Instalar dependencias
Ejecuta el siguiente comando en la terminal para instalar todas las librerías necesarias:

bash
Copiar
Editar
pip install -r requirements.txt
4️⃣ Ejecutar el Dashboard
Ejecuta el siguiente comando en la terminal dentro del proyecto:

bash
Copiar
Editar
streamlit run scripts/dashboard.py
Se abrirá automáticamente en tu navegador.

📊 Funcionalidades del Dashboard
🔹 Defunciones, Casos, Hospitalizaciones y UCI: Visualización de datos acumulados por provincia.
🔹 Gráficos de Barras: Comparación de valores por provincia.
🔹 Gráficos de Pastel Interactivos: Distribución de casos por provincia.
🔹 Filtrado y Selección: Posibilidad de cambiar la métrica y tipo de gráfico en el sidebar.

🛠 Tecnologías Usadas
🔹 Python - Lenguaje de programación principal.
🔹 Pandas - Procesamiento y manipulación de datos.
🔹 Plotly - Gráficos interactivos.
🔹 Streamlit - Creación de interfaz gráfica de usuario.
🔹 Git & GitHub - Control de versiones y almacenamiento en la nube.

👨‍💻 Autor
📌 Nombre: Yazid Ikoubaane Slafti
📧 Correo: yazidslafti7@gmail.com
📌 GitHub: Yazid7-a

📜 Licencia
Este proyecto es de código abierto y está disponible bajo la licencia MIT.

🔗 Enlace al Repositorio
📂 Dashboard COVID-19 en GitHub