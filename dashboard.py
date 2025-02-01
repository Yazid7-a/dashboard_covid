import streamlit as st
from scripts.visualization import plot_graph, plot_pie, load_data

# Cargar los datos procesados
data = load_data("output/data_grouped.json")

# Configurar la página
st.set_page_config(page_title="Dashboard Científico COVID-19", layout="wide")

# Título del dashboard
st.title("📊 Dashboard Científico COVID-19")

# Sidebar para opciones de visualización
st.sidebar.header("Opciones de Visualización")
st.sidebar.write(
    """
    Este dashboard interactivo permite visualizar las estadísticas del impacto del COVID-19
    en distintas provincias de España. Puedes seleccionar la métrica que deseas explorar y
    el tipo de gráfico que prefieres para una representación visual más clara.
    """
)
st.sidebar.write("**Métricas disponibles:**")
st.sidebar.write(
    """
    - **Defunciones:** Total de fallecimientos registrados por provincia.
    - **Casos Nuevos:** Nuevos casos confirmados de COVID-19.
    - **Hospitalizados:** Pacientes hospitalizados.
    - **Pacientes en UCI:** Pacientes ingresados en la Unidad de Cuidados Intensivos.
    """
)
st.sidebar.write("**Tipos de gráficos:**")
st.sidebar.write(
    """
    - **Barras:** Muestra el total por provincia en un gráfico de barras.
    - **Pastel Interactivo:** Representa la distribución proporcional por provincia en un gráfico interactivo.
    """
)

# Selección de métrica
metric = st.sidebar.radio(
    "Selecciona la métrica a visualizar:",
    ["Defunciones", "Casos Nuevos", "Hospitalizados", "Pacientes en UCI"]
)

# Selección de tipo de gráfico
chart_type = st.sidebar.radio(
    "Selecciona el tipo de gráfico:",
    ["Barras", "Pastel Interactivo"]
)

# Asignar métrica a la clave del JSON
metric_key = {
    "Defunciones": "num_def",
    "Casos Nuevos": "new_cases",
    "Hospitalizados": "hospitalized",
    "Pacientes en UCI": "intensive_care"
}[metric]

# Título dinámico del gráfico
chart_title = f"{metric} totales por provincia (Distribución)"

# Mostrar el gráfico dinámicamente
if chart_type == "Barras":
    fig = plot_graph(data, metric_key, chart_title)
    st.plotly_chart(fig, use_container_width=True)
elif chart_type == "Pastel Interactivo":
    fig = plot_pie(data, metric_key, chart_title)
    st.plotly_chart(fig, use_container_width=True)
