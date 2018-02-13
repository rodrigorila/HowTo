# coding=UTF-8

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from how_to import HowTo

app = Flask(__name__)
app.config.from_object(__name__)

Bootstrap(app)
HowTo.init_app(app)


def use_button():
	# import re

	# version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
	# platform = request.user_agent.platform
	# uas = request.user_agent.string

    browser = request.user_agent.browser

    return (browser == 'chrome') or (browser == 'safari')


	# if browser and version:
	# 	if (browser == 'msie' and version < 9) \
     #    or (browser == 'firefox' and version < 4) \
     #    or (platform == 'android' and browser == 'safari' and version < 534) \
     #    or (platform == 'iphone' and browser == 'safari' and version < 7000) \
     #    or ((platform == 'macos' or platform == 'windows') and browser == 'safari' and not re.search('Mobile', uas) and version < 534) \
     #    or (re.search('iPad', uas) and browser == 'safari' and version < 7000) \
     #    or (platform == 'windows' and re.search('Windows Phone OS', uas)) \
     #    or (browser == 'opera') \
     #    or (re.search('BlackBerry', uas)):
     #                return render_template('unsupported.html')


# h.block([
#     u"",
#     u"",
#     u"",
#     ])\
#     .image("") \
#     .text(u"") \
#     .warning(u"") \


def lemonscan5_how_to_calibrate():

    h = HowTo(u"Lemonscan 5", u"Calibrar la rotación de los limones bajo las cámaras")

    h.block([
        u"Preparar un limón marcado con números, uno por octante",
        ])\
        .image("P1310558.JPG") \

    h.block([
        u"Ajustar la velocidad de la línea a [630 G/MN]",
        ])\
        .image("02.png") \

    h.block([
        u"Ir a [Visualización]",
        u"Seleccionar [Visu]",
        u"Elegir la línea en la casilla [Línea]",
        u"Pasar el limón por la línea seleccionada",
        ])\
        .image("01.png") \
        .text(
        u"El limón marcado con 8 números debe rotar 1.2 veces aproximadamente. "
        u"Eso quiere decir que la primera y la última fotografía deben tener los "
        u"mismos números.") \

    h.block([
        u"Revisar las correas y los conos si el limón no ha rotado correctamente",
        ])

    return render_template('how_to.html', how_to=h, use_button=use_button())

def lemonscan5_how_to_adjust_distance_to_camera():

    h = HowTo(u"Lemonscan 5", u"Ajuste de distancia de las cámaras a las salidas")

    h.block([
        u"Ir a [Ajustes]",
        u"En el área de [Ubicación salidas] seleccionar la [Salida] cuyas distancias se desea calibrar",
        ])\
        .image("04_01.png") \
        .text(u"El botón [Igualar] se puede usar para que el valor de la primera línea se "
              u"copie al resto.") \

    h.block([
        u"Preparar un limón en cada línea",
        u"Pasar los limones observando su caída",

        u"Según la inspección visual de la caída de los limones determinar los valores "
        u"mínimo y máximo en los que el limón cae de forma correcta en la salida determinada",

        u"Asignar el valor promedio a la primera salida presionar [Igualar]",
        ])\
        .image("04_02.png") \
        .text(u"Este proceso de búsqueda de valores requiere la observación de la caída de limones "
              u"repetidas veces mientras se varía el valor de la distancia a cada [Línea].") \
        .text(u"Un operador en el equipo va ajustando los números mientras otro observa la caída "
              u"de limones para determinar los valores máximo y mínimo. Una vez obtenidos estos "
              u"valores el promedio será [promedio = (max-min) / 2].") \
        .text(u"Al final del proceso es posible que alguna línea requiera un ajuste particular "
              u"debido a que la cámara no está en exáctamente la misma posición que las demás.") \

    # h.block([
    #     u"",
    #     u"",
    #     u"",
    #     ])\
    #     .image("") \
    #     .text(u"") \
    #     .warning(u"") \


    # h.block([
    #     u"",
    #     u"",
    #     u"",
    #     ])\
    #     .image("") \
    #     .text(u"") \
    #     .warning(u"") \

    return render_template('how_to.html', how_to=h, use_button=use_button())

@app.route("/how_to/<string:group>/<string:name>", methods=['GET'])
def how_to(group, name):
    return eval("{0}_{1}()".format(group, name))


@app.route("/main", methods=['GET'])
def main():
    how_tos = [
        {
            'title': u"Calibrar la rotación de los limones bajo las cámaras",
            'path': "lemonscan5/how_to_calibrate",
        },
        {
            'title': u"Ajuste de distancia de las cámaras a las salidas",
            'path': "lemonscan5/how_to_adjust_distance_to_camera",
        },
    ]
    return render_template('main.html', **locals())


@app.route("/", methods=['GET'])
def welcome():
    return render_template('welcome.html')


if __name__ == "__main__":
    app.run()
