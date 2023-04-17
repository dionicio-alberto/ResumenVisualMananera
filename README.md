# Resumen Visual Mañanera

> *Una imagen vale mas que mil palabras*

![Imagen](https://pbs.twimg.com/media/Ft3ORzKakAARwVA?format=jpg&name=4096x4096)

## Introduccion

En México, durante el sexenio actual (2018-2024) el Presidente, Andrés Manuel Lopez Obrador, lleva a cabo en las mañanas una conferencia de prensa matutina, la cual al inicio del sexenio la anuncio como un espacio abierto para hablar con el presidente, un ejercicio de rendición de cuentas diario hacía país, ciudadanos y reporteros. Si actualmente la "mañanera" sigue siendo este espacio abierto al dialogo es un tema controvertido para algunos.

Sin entrar en mas controversia, se hará un analisís diario sobre las mañaneras resaltando las palabras mas usadas para tener una imagen sobre los principales temas de los que se hablo. Crean dos imágenes, una con los comentarios del presidente AMLO y otra que incluye las principales palabras de las preguntas hechas por los periodistas.

-----

## Datos

Las versiones transcriptas de la conferencia matutina de prensa se extraen de la [página](https://www.gob.mx/presidencia/archivo/articulos?idiom=es&&filter_origin=archive&category=764) oficial del gobierno de México.

-----

## Objetivo

La opinión pública en las redes sociales esta cada vez más polarizada, haciendo que sea cada vez más difícil encontrar información objetiva. Es por esto que este *resumen visual* de la *mañanera* puede ser utilidad, ya que muestra visualmente los temas (a través de las palabras claves) de los que se hablaron de una forma objetiva.

-----

## Plataforma

Las imagenes creadas de forma automática se postarean en [Twitter](https://twitter.com/ResumenMananera) en la cuenta @ResumenManera con apoyo de los servicios de AWS de forma automatica todos los días a las 15:00 hrs (UTC -6:00), el codigo de la autamización es el archivo application.py

-----

## ¿Cómo funciona?

De forma manual, con el archivo `todo_listo.py` podemos realizar el posteo cada vez que lo ejecutamos. Funcionada de la siguiente manera

1. Ejecutamos el archivo `todo_listo.py`
    1. Obtiene el url de la mañera actual usando el modulo `url.py`
    2. Con el url, extraemos todos las intervenciones que se hicieron durante la mañanera
    3. Separamos las intervenciones del presidente y de las demás personas que intervienen en ella
    4. Creamos las gráficas
    5. Subimos la imagen a twitter
    6. Creamos un nuevo tweet con la imagen

Podemos automatizar el proceso usando los servicios de AWS y la extensión Elastic Beanstalk, para esto subimos el zip completo a la extensión Elastic Beanstalk.
