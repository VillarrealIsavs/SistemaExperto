
# 🧠 Sistema Experto: ¿A Qué Universidad Debería Ir?

Este proyecto implementa un **sistema experto basado en reglas** que recomienda universidades de Colombia según el perfil académico y económico del estudiante.  
Utiliza información real de 10 universidades colombianas (costos, ICFES recomendado, fortalezas, prestigio y ciudad).

---

## 📌 Características Principales

- Pregunta primero el **puntaje ICFES** y filtra universidades según el mínimo recomendado.
- Filtra estrictamente por:
  - **Tipo de universidad** (pública o privada).
  - **Ciudad** donde el estudiante desea estudiar.
  - **Presupuesto mensual real** (valor en COP).
  - **Área de interés** (ingeniería, medicina, derecho, etc.).
  - **Prestigio** (alto o medio).
- Motor de inferencia basado en reglas que asigna puntajes y descarta universidades que no cumplen criterios.
- Devuelve una lista ordenada de universidades recomendadas.

---

## 🏫 Universidades Incluidas

El sistema utiliza datos reales de:

- Universidad Nacional  
- Universidad de los Andes  
- Pontificia Universidad Javeriana  
- Universidad de Antioquia (UdeA)  
- Universidad del Valle (Univalle)  
- Universidad Industrial de Santander (UIS)  
- EAFIT  
- Universidad del Rosario  
- Universidad de La Sabana  
- Universidad del Norte (Uninorte)

Cada una incluye:

- Tipo (pública/privada)  
- Ciudad  
- Rango de costo mensual  
- ICFES mínimo recomendado  
- Fortalezas académicas  
- Nivel de prestigio  

---

## ⚙️ Cómo Funciona

El sistema sigue un flujo de preguntas:

1. Puntaje ICFES  
2. Tipo de universidad (si aplica)  
3. Ciudad donde desea estudiar  
4. Área de interés  
5. Presupuesto mensual  
6. Importancia del prestigio  

Luego:

- Filtra universidades que **no cumplen** los criterios mínimos.
- Evalúa las restantes con un sistema de puntaje.
- Ordena las opciones y muestra las mejores recomendaciones.

---

## 🧩 Motor de Inferencia

El motor aplica reglas como:

- **ICFES mínimo:** si el puntaje es menor al recomendado → descartada.  
- **Ciudad estricta:** solo universidades en la ciudad elegida.  
- **Tipo:** si el usuario elige pública, no se muestran privadas (y viceversa).  
- **Presupuesto:** debe estar dentro del rango mensual de la universidad.  
- **Área:** suma puntos si coincide con las fortalezas.  
- **Prestigio:** suma puntos si coincide con la preferencia del usuario.

---

1. Nodos de entrada (preguntas del sistema experto)
Nodos de entrada:
•	Puntaje ICFES
•	Tipo de universidad (pública / privada / indiferente)
•	Carrera deseada
•	Departamento
•	Municipio
•	Disposición a mudarse
•	Presupuesto por semestre
•	Interés en beca
•	Interés en crédito educativo
•	Puntaje histórico en el colegio
2. Nodos de reglas (base de conocimiento)
Nodos de reglas:
•	R1: Puntaje alto + pública → alta demanda
•	R2: Puntaje bajo + pública → revisar ponderado / repetir examen
•	R3: Privada + presupuesto alto → acceso amplio
•	R4: Privada + presupuesto bajo → buscar becas/financiación
•	R5: Puntaje alto + beca → becas por mérito
•	R6: No mudarse → universidades cercanas
•	R7: Sí mudarse → universidades de todo el país
•	R8: Ingeniería → prioridad universidades fuertes en ingeniería
•	R9: Medicina → prioridad universidades con hospitales
•	R10: Derecho → prioridad universidades fuertes en derecho


3. Nodos de salida (universidades recomendadas)
Nodos de salida:
•	Universidad Nacional
•	Universidad de los Andes
•	Pontificia Universidad Javeriana
•	Universidad de Antioquia
•	Universidad del Valle
•	Universidad Industrial de Santander (UIS)
•	Universidad EAFIT
•	Universidad del Rosario
•	Universidad de La Sabana
•	Universidad del Norte
4. Nodos conceptuales del problema (del documento Problematica.pdf)
Nodos conceptuales:
•	Problema: elección de carrera y universidad
•	Causas: falta de información, presión social, desconocimiento de habilidades
•	Consecuencias: deserción, mala elección, pérdida de tiempo/dinero
•	Objetivo del sistema: orientar con base en reglas y conocimiento experto
•	Usuarios: estudiantes, bachilleres, orientadores
•	Beneficios: reducir deserción, mejorar decisiones, ahorrar tiempo



---

