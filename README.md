
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

## 📂 Estructura del Proyecto

```
📁 sistema-experto-universidades
│
├── README.md
└── sistema_experto.py
```

---

## ▶️ Cómo Ejecutarlo

1. Instala Python 3.8+  
2. Ejecuta el archivo:

```bash
python sistema_experto.py
```

3. Responde las preguntas en consola.  
4. Recibe las recomendaciones personalizadas.

---

## 🧪 Ejemplo de Uso

```
¿Cuál fue tu puntaje ICFES? 350
Tu puntaje solo permite aplicar a PRIVADAS.

¿En qué ciudad quieres estudiar? Bogotá
¿Qué área te interesa? ingeniería
¿Cuánto puedes pagar al mes? 2500000
¿Qué tan importante es el prestigio? alto
```

**Resultado:**

- Universidad Javeriana  
- Universidad del Rosario  
- Universidad de los Andes  

---

## 🚀 Mejoras Futuras

- Interfaz gráfica (Tkinter o PyQt)
- Versión web (Flask o FastAPI)
- Sistema de becas y financiación
- Recomendación de carreras específicas
- Integración con mapas y geolocalización

---

