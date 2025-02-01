import json
import plotly.express as px
from collections import defaultdict

def load_data(json_file):
    """Carga los datos desde un archivo JSON."""
    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)

def plot_graph(data, metric, title, top_n=30):
    """Genera una gráfica de barras para una métrica específica."""
    province_totals = defaultdict(int)

    # Acumular métricas por provincia
    for period, province_data in data.items():
        for province, metrics in province_data.items():
            province_totals[province] += metrics[metric]

    # Ordenar por valores y seleccionar las top N
    sorted_totals = sorted(province_totals.items(), key=lambda x: x[1], reverse=True)
    top_provinces = sorted_totals[:top_n]
    other_total = sum(value for _, value in sorted_totals[top_n:])
    provinces = [province for province, _ in top_provinces]
    values = [value for _, value in top_provinces]

    if other_total > 0:
        provinces.append("Otros")
        values.append(other_total)

    # Crear gráfico de barras
    fig = px.bar(
        x=provinces,
        y=values,
        labels={'x': 'Provincias', 'y': 'Cantidad'},
        title=title
    )
    return fig

def plot_pie(data, metric, title, top_n=10):
    """Genera un gráfico interactivo de pastel para una métrica específica."""
    province_totals = defaultdict(int)

    # Sumar métricas por provincia
    for period, province_data in data.items():
        for province, metrics in province_data.items():
            province_totals[province] += metrics[metric]

    # Ordenar y seleccionar top N
    sorted_totals = sorted(province_totals.items(), key=lambda x: x[1], reverse=True)
    top_provinces = sorted_totals[:top_n]
    other_total = sum(value for _, value in sorted_totals[top_n:])
    provinces = [province for province, _ in top_provinces]
    values = [value for _, value in top_provinces]

    if other_total > 0:
        provinces.append("Otros")
        values.append(other_total)

    # Máximos y mínimos
    max_province, max_value = sorted_totals[0]
    min_province, min_value = sorted_totals[-1]

    # Crear gráfico de pastel
    fig = px.pie(
        names=provinces,
        values=values,
        title=f"{title}<br>Máximo: {max_province} ({max_value}), Mínimo: {min_province} ({min_value})",
        hole=0.4
    )
    return fig
