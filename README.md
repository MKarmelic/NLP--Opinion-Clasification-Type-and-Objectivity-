# Opinion clasification with NLP - Bootcamp Data Science UDD

*Bootcamp UDD: Ciencia de Datos e Inteligencia Artificial Proyecto del Módulo 7: Técnicas avanzadas para ciencia de datos y empleabilidad*

Se construyó una API que cumple con la función de evaluar comentarios, entregando el sentimiento evaluado y el nivel de subjetividad del comentario mismo.

## ¿Cómo consumir la API?

Ingresar al siguiente link: https://mkarmelic.pythonanywhere.com/
La API se encuentra alojada en dicha pagina web que cuple con la función sencilla de permitir que cualquier persona escriba un comentario y este será evaluado, entregando el resultado en la misma página web.

En este repositorio de GitHub se pueden encontrar todos los archivos alojados en la web, esto consta de:
- index.html
- style.css
- script.js
- app.py

La misma app.py puede montarse en cualquier otro servidor y obtener los mismos resultados via POST, ya que ese es el método que se está utilizando a través de Javascript.

## ¿Cómo funciona?

La API toma el texto que se ingresa en el recuadro una vez que se clickea el boton. Todo ese texto es preprocesado y traspasado a dos modelos diferentes:
- Un modelo de Regresión Logística, calcula el sentimiento general del comentario.
- Un modelo de Regresión de Bosque Aleatorio, calcula que tan subjetivo es el comentario, de 0 a 1.

## ¿Qué aplicaciones tiene?

Esta API podría utilizarse como punto intermedio en cualquier encuesta o sección de toma de comentarios digital. Al ser una API intermediaria, nos permite rellenar las bases de datos con más información de la que originalmente se publica en el comentario, permitiendo bases de datos más robustas y que nos permitan mejor toma de decisiones.
