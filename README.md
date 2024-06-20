# Opinion clasification with NLP - Bootcamp Data Science UDD

*Bootcamp UDD: Ciencia de Datos e Inteligencia Artificial Proyecto del Módulo 7: Técnicas avanzadas para ciencia de datos y empleabilidad*

Se construyó una API que cumple con la función de evaluar comentarios, entregando el sentimiento evaluado y el nivel de subjetividad del comentario mismo.

## ¿Cómo consumir la API?

Previamente alojada en https://mfkarmelic.pythonanywhere.com/ por limitantes del servidor se presenta ahora Offline.
La API se encuentra ahora en este Github, con todo lo necesario para poder correrla.

En este repositorio de GitHub se pueden encontrar todos los archivos necesario, esto consta de:
- index.html
- style.css
- script.js
- app.py
- carpeta 'data' con modelos previamente trabajados

Esta API uede montarse en un servidor y obtener los mismos resultados via POST, ya que ese es el método que se está utilizando a través de Javascript en la web html propuesta.

## ¿Cómo funciona?

La API toma el texto que se ingresa en el recuadro una vez que se clickea el boton. Todo ese texto es preprocesado y traspasado a dos modelos diferentes:
- Un modelo de Regresión Logística, calcula el sentimiento general del comentario.
- Un modelo de Regresión de Bosque Aleatorio, calcula que tan subjetivo es el comentario, de 0 a 1.

## ¿Qué aplicaciones tiene?

Esta API podría utilizarse como punto intermedio en cualquier encuesta o sección de toma de comentarios digital. Al ser una API intermediaria, nos permite rellenar las bases de datos con más información de la que originalmente se publica en el comentario, permitiendo bases de datos más robustas y que nos permitan mejor toma de decisiones.

### ¿Como la hago funcionar Offline?

- Debes descagar todo lo que se encuentra en este Github a excepción del archivo 'Pres PM7'.
- En una carpeta Ubica todos los contenidos y extrae data.rar, esto quedará en una subcarpeta.
- Debes instalar utilizando ``$pip install requirements.txt``
- Una vez instalado, puedes iniciar app.py (Personalmente utilizo PyCharm, pero puede ser directamente)
- Obtén el servidor local donde está corriendo, el default es ``http://127.0.0.1:5000``
- Si el servidor local es diferente al default, haz de cambiarlo en el archivo 'script.js' en la linea ``fetch("http://127.0.0.1:5000/predict", {``
- Abre el archivo 'index.html'
- Rellena la caja de comentarios, pincha "Enviar"
- Obtén tus resultados

### Imagenes referenciales
*Web App homepage*

![image](https://github.com/MKarmelic/NLP--Opinion-Clasification-Type-and-Objectivity-/assets/167670728/a89c07f6-c898-403e-94e3-09c6de96c3fb)

*Web App Resultados*

![image](https://github.com/MKarmelic/NLP--Opinion-Clasification-Type-and-Objectivity-/assets/167670728/85869f55-a5ae-4305-aa6d-1a4a0bddf3de)


