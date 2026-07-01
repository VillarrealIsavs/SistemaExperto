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
# MOTOR DE INFERENCIA
# -----------------------------

def evaluar_universidad(univ, perfil):
    score = 0

    ciudad = perfil["ciudad"]
    if ciudad.lower() == "santander":
        if "Bucaramanga" in univ["ciudades"]:
            score += 3
    else:
        for c in univ["ciudades"]:
            if ciudad.lower() in c.lower():
                score += 3

    if perfil["tipo"] == univ["tipo"]:
        score += 2

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
        score += 1

    if perfil["modalidad"] in univ["modalidades"]:
        score += 3

    if perfil["prestigio"] == "alto":
        if univ["prestigio"] == "alto":
            score += 3
    elif perfil["prestigio"] == "medio":
        if univ["prestigio"] in ["medio", "alto"]:
            score += 2
    elif perfil["prestigio"] == "bajo":
        score += 1

    area = perfil["area"]
    if area in univ["fortalezas"]:
        score += 4

    return score

def recomendar_universidades(perfil):
    resultados = []
    for univ in universidades:
        s = evaluar_universidad(univ, perfil)
        resultados.append((univ["nombre"], s))

    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados

# -----------------------------
# INTERFAZ DE USUARIO
# -----------------------------

def main():
    print("=======================================")
    print(" SISTEMA EXPERTO: ¿A QUÉ UNIVERSIDAD IR?")
    print("=======================================\n")

    # PRIMERA PREGUNTA: ICFES
    icfes = int(entrada_texto("¿Cuál fue tu puntaje ICFES? (ej: 350, 380): "))

    # REGLA NUEVA: si ICFES <= 370, solo privada
    if icfes > 370:
        tipo = preguntar_opcion(
            "\nTu puntaje te permite escoger entre pública o privada. ¿Cuál prefieres?",
            ["pública", "privada"]
        )
    else:
        print("\nTu puntaje ICFES indica que solo puedes aplicar a universidades PRIVADAS.")
        tipo = "privada"

    ciudad = entrada_texto("\n¿En qué ciudad o región quieres estudiar? (ej: Bucaramanga, Bogotá, Santander, virtual): ")

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

    modalidad = preguntar_opcion(
        "\n¿Qué modalidad prefieres?",
        ["presencial", "virtual", "híbrida"]
    )
    if modalidad == "híbrida":
        modalidad = "virtual"

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

    for nombre, score in recomendaciones[:5]:
        print(f"- {nombre} (puntaje: {score})")

    print("\nInterpretación:")
    print("Mientras más alto el puntaje, más se ajusta la universidad a tu perfil.\n")

if __name__ == "__main__":
    main()
