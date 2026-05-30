import json
import os

def generar_escenario_ideal():
    materias = [
        {"id": "M1", "nombre": "Cálculo Diferencial", "nivel": 1, "creditos": 3, "sesiones_semanales": 2, "area_conocimiento": "Ciencias Básicas"},
        {"id": "M2", "nombre": "Programación Básica", "nivel": 1, "creditos": 3, "sesiones_semanales": 2, "area_conocimiento": "Programación"},
        {"id": "M3", "nombre": "Cálculo Integral", "nivel": 2, "creditos": 3, "sesiones_semanales": 2, "area_conocimiento": "Ciencias Básicas"},
        {"id": "M4", "nombre": "Física Mecánica", "nivel": 2, "creditos": 3, "sesiones_semanales": 2, "area_conocimiento": "Física"},
        {"id": "M5", "nombre": "Estructuras de Datos", "nivel": 3, "creditos": 4, "sesiones_semanales": 3, "area_conocimiento": "Programación"}
    ]
    
    profesores = [
        {"id": "P1", "nombre": "Augusto Peña", "tipo_contrato": "Planta", "max_creditos_docencia": 60, "areas_habilitadas": ["Ciencias Básicas"]},
        {"id": "P2", "nombre": "Lucía Castro", "tipo_contrato": "Planta", "max_creditos_docencia": 60, "areas_habilitadas": ["Programación"]},
        {"id": "P3", "nombre": "Javier Ramírez", "tipo_contrato": "Planta", "max_creditos_docencia": 60, "areas_habilitadas": ["Física", "Ciencias Básicas"]}
    ]
    
    grupos_abiertos = [
        {"id_grupo": "GR_M1", "id_materia": "M1", "cupo": 30, "estudiantes_inscritos": []},
        {"id_grupo": "GR_M2", "id_materia": "M2", "cupo": 30, "estudiantes_inscritos": []},
        {"id_grupo": "GR_M3", "id_materia": "M3", "cupo": 30, "estudiantes_inscritos": []},
        {"id_grupo": "GR_M4", "id_materia": "M4", "cupo": 30, "estudiantes_inscritos": []},
        {"id_grupo": "GR_M5", "id_materia": "M5", "cupo": 30, "estudiantes_inscritos": []}
    ]
    
    # Población uniforme de 30 estudiantes (Agrupados estrictamente por nivel)
    for i in range(1, 31):
        est_id = f"EST_{i:03d}"
        if i <= 10:
            # Estudiantes de Nivel 1 (Ven Cálculo Diferencial y Programación Básica)
            grupos_abiertos[0]["estudiantes_inscritos"].append(est_id)
            grupos_abiertos[1]["estudiantes_inscritos"].append(est_id)
        elif i <= 20:
            # Estudiantes de Nivel 2 (Ven Cálculo Integral y Física Mecánica)
            grupos_abiertos[2]["estudiantes_inscritos"].append(est_id)
            grupos_abiertos[3]["estudiantes_inscritos"].append(est_id)
        else:
            # Estudiantes de Nivel 3 (Ven Estructuras de Datos)
            grupos_abiertos[4]["estudiantes_inscritos"].append(est_id)

    datos = {
        "materias": materias,
        "profesores": profesores,
        "historial_reprobacion": [],  # Sin vetos históricos para garantizar flujo óptimo
        "grupos_abiertos": grupos_abiertos
    }

    # Asegurar que el directorio exista antes de escribir
    os.makedirs("infrastructure/dataset", exist_ok=True)

    ruta_archivo = "infrastructure/dataset/facultad_data.json"
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
        
    print(f"✅ Escenario 1 (Flujo Ideal) generado exitosamente en: {ruta_archivo}")

if __name__ == "__main__":
    generar_escenario_ideal()