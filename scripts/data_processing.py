import csv
import json
from collections import defaultdict

def process_csv_to_json(input_file, output_file):
    """
    Procesa un archivo CSV y agrupa los datos por día de la semana y provincias.
    Calcula acumulados de defunciones, nuevos casos, hospitalizados y pacientes en UCI.
    """
    # Estructura de datos agrupados
    data = defaultdict(lambda: defaultdict(lambda: {
        "num_def": 0,
        "new_cases": 0,
        "hospitalized": 0,
        "intensive_care": 0
    }))

    # Leer el archivo CSV
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            day_of_week = row['day_of_week']
            province = row['province']
            data[day_of_week][province]["num_def"] += int(row.get('deceased', 0))
            data[day_of_week][province]["new_cases"] += int(row.get('new_cases', 0))
            data[day_of_week][province]["hospitalized"] += int(row.get('hospitalized', 0))
            data[day_of_week][province]["intensive_care"] += int(row.get('intensive_care', 0))

    # Guardar en un archivo JSON
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    print(f"Datos procesados y guardados en {output_file}")


if __name__ == "__main__":
    process_csv_to_json("data/Proyecto_3.csv", "output/data_grouped.json")
