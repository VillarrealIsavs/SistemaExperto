# -*- coding: utf-8 -*-
"""
Sistema experto: ¿A qué universidad debería ir?
Enfoque: Colombia, pero fácilmente adaptable.
"""

# -----------------------------
# BASE DE CONOCIMIENTO
# -----------------------------

universidades = [
    {
        "nombre": "Universidad Nacional de Colombia",
        "ciudades": ["Bogotá", "Medellín", "Manizales", "Palmira"],
        "tipo": "pública",
        "prestigio": "alto",
        "costo": "bajo",
        "modalidades": ["presencial"],
        "fortalezas": ["ingenieria", "ciencias", "arte", "sociales"]
    },
    {
        "nombre": "Universidad Industrial de Santander (UIS)",
        "ciudades": ["Bucaramanga"],
        "tipo": "pública",
        "prestigio": "alto",
        "costo": "bajo",
        "modalidades": ["presencial"],
        "fortalezas": ["ingenieria", "ciencias", "salud"]
    },
    {
        "nombre": "Universidad de Antioquia (UDEA)",
        "ciudades": ["Medellín"],
        "tipo": "pública",
        "prestigio": "alto",
        "costo": "bajo",
        "modalidades": ["presencial"],
        "fortalezas": ["salud", "sociales", "ingenieria"]
    },
    {
        "nombre": "Universidad de los Andes",
        "ciudades": ["Bogotá"],
        "tipo": "privada",
        "prestigio": "alto",
        "costo": "alto",
        "modalidades": ["presencial"],
        "fortalezas": ["negocios", "ingenieria", "sociales"]
    },
    {
        "nombre": "Pontificia Universidad Javeriana",
        "ciudades": ["Bogotá", "Cali"],
        "tipo": "privada",
        "prestigio": "alto",
        "costo": "alto",
        "modalidades": ["presencial"],
        "fortalezas": ["salud", "negocios", "arte", "sociales"]
    },
    {
        "nombre": "UNAB (Universidad Autónoma de Bucaramanga)",
        "ciudades": ["Bucaramanga"],
        "tipo": "privada",
        "prestigio": "medio",
        "costo": "medio",
        "modalidades": ["presencial", "virtual"],
        "fortalezas": ["negocios", "ingenieria", "comunicacion"]
    },
    {
        "nombre": "UDES (Universidad de Santander)",
        "ciudades": ["Bucaramanga"],
        "tipo": "privada",
        "prestigio": "medio",
        "costo": "medio",
        "modalidades": ["presencial"],
        "fortalezas": ["salud", "negocios"]
    },
    {
        "nombre": "UNAD (Universidad Nacional Abierta y a Distancia)",
        "ciudades": ["virtual"],
        "tipo": "pública",
        "prestigio": "medio",
        "costo": "bajo",
        "modalidades": ["virtual"],
        "fortalezas": ["tecnologia", "administracion"]
    },
    {
        "nombre": "Politécnico Grancolombiano",
        "ciudades": ["Bogotá", "virtual"],
        "tipo": "privada",
        "prestigio": "medio",
        "costo": "bajo",
        "modalidades": ["virtual", "presencial"],
        "fortalezas": ["negocios", "tecnologia"]
    },
    {
        "nombre": "SENA",
        "ciudades": ["todo el país"],
        "tipo": "pública",
        "prestigio": "medio",
        "costo": "muy_bajo",
        "modalidades": ["presencial", "virtual"],
        "fortalezas": ["tecnico", "tecnologo"]
    }
]

# -----------------------------
# FUNCIONES DE APOYO
# -----------------------------

def preguntar_opcion(mensaje, opciones):
    print(mensaje)
    for i, op in enumerate(opciones, 1):
        print(f"{i}. {op}")
    while True:
        try:
            eleccion = int(input("Elige una opción (número): "))
            if 1 <= eleccion <= len(opciones):
                return opciones[eleccion - 1]
            else:
                print("Opción inválida, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida, escribe solo el número.")

def entrada_texto(mensaje):
    return input(mensaje).strip()

# -----------------------------
# MOTOR DE INFERENCIA (FORWARD CHAINING)
# -----------------------------

def evaluar_universidad(univ, perfil):
    score = 0

    # Regla: ciudad / región
    ciudad = perfil["ciudad"]
    if ciudad.lower() == "santander":
        # asumimos Bucaramanga como referencia
        if "Bucaramanga" in univ["ciudades"]:
            score += 3
    else:
        # si la ciudad está en la lista
        for c in univ["ciudades"]:
            if ciudad.lower() in c.lower():
                score += 3

    # Regla: tipo (pública/privada)
    if perfil["tipo"] == univ["tipo"]:
        score += 2

    # Regla: presupuesto
    presupuesto = perfil["presupuesto"]
    costo = univ["costo"]
    if presupuesto == "muy_bajo":
        if costo in ["muy_bajo", "bajo"]:
            score += 3
    elif presupuesto == "bajo":
        if costo in ["bajo", "medio"]:
            score += 2
    elif presupuesto == "medio":
        if costo in ["medio", "alto"]:
            score += 2
    elif presupuesto == "alto":
        # cualquier costo es viable
        score += 1

    # Regla: modalidad
    if perfil["modalidad"] in univ["modalidades"]:
        score += 3

    # Regla: prestigio
    if perfil["prestigio"] == "alto":
        if univ["prestigio"] == "alto":
            score += 3
    elif perfil["prestigio"] == "medio":
        if univ["prestigio"] in ["medio", "alto"]:
            score += 2
    elif perfil["prestigio"] == "bajo":
        score += 1  # no es tan importante

    # Regla: área/carrera
    area = perfil["area"]
    if area in univ["fortalezas"]:
        score += 4

    return score

def recomendar_universidades(perfil):
    resultados = []
    for univ in universidades:
        s = evaluar_universidad(univ, perfil)
        resultados.append((univ["nombre"], s))

    # ordenar por puntaje descendente
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados

# -----------------------------
# INTERFAZ DE USUARIO
# -----------------------------

def main():
    print("=======================================")
    print(" SISTEMA EXPERTO: ¿A QUÉ UNIVERSIDAD IR?")
    print("=======================================\n")

    ciudad = entrada_texto("¿En qué ciudad o región quieres estudiar? (ej: Bucaramanga, Bogotá, Santander, virtual): ")

    area = preguntar_opcion(
        "\n¿Qué área se parece más a la carrera que quieres estudiar?",
        ["ingenieria", "ciencias", "salud", "negocios", "arte", "sociales", "tecnologia", "comunicacion", "tecnico/tecnologo"]
    )
    if area == "tecnico/tecnologo":
        area = "tecnico"

    presupuesto = preguntar_opcion(
        "\n¿Cuál es tu nivel de presupuesto aproximado?",
        ["muy_bajo", "bajo", "medio", "alto"]
    )

    tipo = preguntar_opcion(
        "\n¿Prefieres universidad pública o privada?",
        ["pública", "privada"]
    )

    modalidad = preguntar_opcion(
        "\n¿Qué modalidad prefieres?",
        ["presencial", "virtual", "híbrida"]
    )
    # simplificación: si elige híbrida, consideramos que acepta presencial y virtual
    if modalidad == "híbrida":
        modalidad = "virtual"  # para favorecer universidades con virtual

    prestigio = preguntar_opcion(
        "\n¿Qué tan importante es el prestigio de la universidad?",
        ["alto", "medio", "bajo"]
    )

    perfil = {
        "ciudad": ciudad,
        "area": area,
        "presupuesto": presupuesto,
        "tipo": tipo,
        "modalidad": modalidad,
        "prestigio": prestigio
    }

    print("\n\nProcesando tu perfil...\n")

    recomendaciones = recomendar_universidades(perfil)

    print("=======================================")
    print(" RECOMENDACIONES DE UNIVERSIDAD")
    print("=======================================\n")

    # mostramos las top 5
    for nombre, score in recomendaciones[:5]:
        print(f"- {nombre} (puntaje: {score})")

    print("\nInterpretación:")
    print("Mientras más alto el puntaje, más se ajusta la universidad a tu perfil.")
    print("Puedes ajustar la base de conocimiento (lista de universidades y reglas) para hacerlo aún más preciso.\n")

if __name__ == "__main__":
    main()
