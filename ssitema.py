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
        "nombre": "UNAB",
        "ciudades": ["Bucaramanga"],
        "tipo": "privada",
        "prestigio": "medio",
        "costo": "medio",
        "modalidades": ["presencial", "virtual"],
        "fortalezas": ["negocios", "ingenieria", "comunicacion"]
    },
    {
        "nombre": "UDES",
        "ciudades": ["Bucaramanga"],
        "tipo": "privada",
        "prestigio": "medio",
        "costo": "medio",
        "modalidades": ["presencial"],
        "fortalezas": ["salud", "negocios"]
    },
    {
        "nombre": "UNAD",
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

    # Ciudad estricta
    if perfil["ciudad"].lower() not in [c.lower() for c in univ["ciudades"]]:
        return -999  # descarta totalmente

    # Tipo estricta
    if perfil["tipo"] != univ["tipo"]:
        return -999  # descarta totalmente

    # Reglas normales
    if perfil["modalidad"] in univ["modalidades"]:
        score += 3

    if perfil["prestigio"] == "alto" and univ["prestigio"] == "alto":
        score += 3
    elif perfil["prestigio"] == "medio" and univ["prestigio"] in ["medio", "alto"]:
        score += 2
    else:
        score += 1

    presupuesto = perfil["presupuesto"]
    costo = univ["costo"]
    if presupuesto == "muy_bajo" and costo in ["muy_bajo", "bajo"]:
        score += 3
    elif presupuesto == "bajo" and costo in ["bajo", "medio"]:
        score += 2
    elif presupuesto == "medio" and costo in ["medio", "alto"]:
        score += 2
    elif presupuesto == "alto":
        score += 1

    if perfil["area"] in univ["fortalezas"]:
        score += 4

    return score

def recomendar_universidades(perfil):
    resultados = []
    for univ in universidades:
        s = evaluar_universidad(univ, perfil)
        if s >= 0:  # solo universidades válidas
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

    # REGLA NUEVA
    if icfes > 370:
        tipo = preguntar_opcion(
            "\nTu puntaje te permite escoger entre pública o privada. ¿Cuál prefieres?",
            ["pública", "privada"]
        )
    else:
        print("\nTu puntaje ICFES indica que solo puedes aplicar a universidades PRIVADAS.")
        tipo = "privada"

    ciudad = entrada_texto("\n¿En qué ciudad quieres estudiar? (ej: Bucaramanga, Bogotá, Medellín, virtual): ")

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

    if not recomendaciones:
        print("No se encontraron universidades que cumplan con tus criterios.")
    else:
        for nombre, score in recomendaciones[:5]:
            print(f"- {nombre} (puntaje: {score})")

    print("\nInterpretación:")
    print("Mientras más alto el puntaje, más se ajusta la universidad a tu perfil.\n")

if __name__ == "__main__":
    main()

