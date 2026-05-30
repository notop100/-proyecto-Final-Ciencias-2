import json
import random
import os

from seed_data1 import generar_escenario_ideal

def generar_escenario_saturacion():
    print("Iniciando generación de datos para el Escenario 3 (Saturación Crítica)...")

    # 1. Catálogo de Materias Ampliado (Muchos niveles para generar cruces en cadena)
    materias = [
        { "id": "M1", "nombre": "Cálculo Diferencial", "nivel": 1, "creditos": 3 },
        { "id": "M2", "nombre": "Programación Básica", "nivel": 1, "creditos": 3 },
        { "id": "M3", "nombre": "Cálculo Integral", "nivel": 2, "creditos": 3 },
        { "id": "M4", "nombre": "Física Mecánica", "nivel": 2, "creditos": 3 },
        { "id": "M5", "nombre": "Cálculo Multivariado", "nivel": 3, "creditos": 3 },
        { "id": "M6", "nombre": "Estructuras de Datos", "nivel": 3, "creditos": 4 },
        { "id": "M7", "nombre": "Ecuaciones Diferenciales", "nivel": 4, "creditos": 3 },
        { "id": "M8", "nombre": "Programación Orientada a Objetos", "nivel": 2, "creditos": 4 },
        { "id": "M9", "nombre": "Métodos Numéricos", "nivel": 4, "creditos": 3 },
        { "id": "M10", "nombre": "Arquitectura de Computadores", "nivel": 5, "creditos": 3 }
    ]

    # 2. Catálogo de Profesores muy Reducido (Escasez severa de personal)
    profesores = [
        { "id": "P_001", "nombre": "Profesor Sobrecargado 1" },
        { "id": "P_002", "nombre": "Profesor Sobrecargado 2" },
        { "id": "P_003", "nombre": "Profesor Sobrecargado 3" }
    ]

    # 3. Masa Estudiantil Grande (250 estudiantes para colapsar los cupos y generar cliques)
    estudiantes = []
    for i in range(1, 251):
        estudiantes.append({ "id": f"EST_{i:03d}", "nombre": f"Estudiante Masa {i}" })

    # 4. Creación de una Oferta Excesiva de Grupos (4 grupos por materia = 40 grupos)
    grupos_abiertos = []
    for materia in materias:
        for num_grupo in (1, 2, 3, 4):
            grupos_abiertos.append({
                "id_grupo": f"G0{num_grupo}_{materia['id']}",
                "id_materia": materia['id'],
                "cupo": 40,
                "estudiantes_inscritos": [],
                "_creditos": materia['creditos']
            })

    # 5. Inscripción Masiva y Caótica (Forzando colisiones de estudiantes compartidos)
    # Cada estudiante inscribe materias de forma indiscriminada (adelantando/atrasando)
    for estudiante in estudiantes:
        # Intenta inscribir 6 grupos aleatorios para estar al límite de créditos
        grupos_random = random.sample(grupos_abiertos, k=6)
        
        for grupo in grupos_random:
            materia_id = grupo['id_materia']
            inscrito_en_materia = any(
                estudiante['id'] in g['estudiantes_inscritos'] 
                for g in grupos_abiertos if g['id_materia'] == materia_id
            )
            
            if not inscrito_en_materia and len(grupo['estudiantes_inscritos']) < grupo['cupo']:
                grupo['estudiantes_inscritos'].append(estudiante['id'])

    # Limpiar campo temporal
    for grupo in grupos_abiertos:
        del grupo['_creditos']

    # 6. Historial Masivo de Reprobaciones (80 Vetos para asfixiar la Fase 1)
    historial_reprobacion = []
    for _ in range(80):
        veto = {
            "id_estudiante": random.choice(estudiantes)['id'],
            "id_materia": random.choice(materias)['id'],
            "id_profesor_vetado": random.choice(profesores)['id']
        }
        if veto not in historial_reprobacion:
            historial_reprobacion.append(veto)

    # 7. Guardar en JSON
    dataset_final = {
        "materias": materias,
        "profesores": profesores,
        "estudiantes": estudiantes,
        "grupos_abiertos": grupos_abiertos,
        "historial_reprobacion": historial_reprobacion
    }

    ruta_salida = "infrastructure/dataset/facultad_data.json"
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        json.dump(dataset_final, f, indent=2, ensure_ascii=False)

    print(f"⚠️ Éxito: Dataset de SATURACIÓN CRÍTICA generado en {ruta_salida}")
    print(f"Total Grupos en oferta: {len(grupos_abiertos)} (Para solo 3 profesores)")
    print(f"Total Alumnos distribuidos: {len(estudiantes)}")
    print(f"Total Vetos inyectados: {len(historial_reprobacion)}")

if __name__ == "__main__":
    generar_escenario_ideal()