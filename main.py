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


def lemonscan5_how_to_calibrate():

    h = HowTo(u"Lemonscan 5", u"Calibrar la rotación de los limones bajo las cámaras")

    h.block([
        u"Preparar un limón marcado con números, uno por octante",
        ])\
        .image("P1310558.JPG") \

    h.block([
        u"Ajustar la velocidad del [Calibrador] a [630 G/MN] aproximadamente",
        ])\
        .image("02_01.png") \

    h.block([
        u"Ir a [Visualización]",
        u"Seleccionar [Visu]",
        u"Elegir la línea en la casilla [Línea]",
        u"Pasar el limón por la línea seleccionada",
        ])\
        .image("01_01.png") \
        .text(
        u"El limón marcado con 8 números debe [rotar 1.2 veces aproximadamente]. "
        u"Eso quiere decir que la primera y la última fotografía deben tener los "
        u"mismos números.") \

    h.block([
        u"Si el giro no es completo se puede calibrar en [Ajustes] el valor de [Coef] para la cámara",
        ]) \
        .image("11_01.png") \

    return render_template('how_to.html', how_to=h, use_button=use_button())

def lemonscan5_how_to_adjust_distance_to_camera():

    h = HowTo(u"Lemonscan 5", u"Ajuste de distancia de las cámaras a las salidas")

    h.block([
        u"Ir a [Programas]",
        u"Asignar un [Programa] de prueba que saque todos los limones por la misma salida",
        u"Asignar el grupo a la salida [S] correspondiente"
        ]) \
        .image("14_01.png")

    h.block([
        u"Ir a [Ajustes]",
        u"En el área de [Ubicación salidas] seleccionar la [Salida] cuyas distancias se desea calibrar",
        ])\
        .image("04_01.png") \

    h.block([
        u"Preparar un limón en cada línea",
        u"Pasar los limones observando su caída varias veces",

        u"Según inspección visual de la caída de los limones determinar los valores "
        u"mínimo y máximo en los que el limón cae de forma correcta en la salida determinada",

        u"Asignar el valor promedio a la primera salida presionar [Igualar]",
        ])\
        .text(u"Este proceso de búsqueda de valores requiere la observación de la caída de limones "
              u"repetidas veces mientras se varía el valor de la distancia a cada línea.") \
        .text(u"Un operador en el equipo va ajustando los números mientras otro observa la caída "
              u"de limones para determinar los valores máximo y mínimo. Una vez obtenidos estos "
              u"valores el promedio será [promedio = (max-min) / 2].") \
        .image("14-b_01.png") \
        .text(u"El botón [Igualar] se puede usar para que el valor de la primera línea se "
              u"copie al resto.") \
        .text(u"Al final del proceso es posible que alguna línea requiera un ajuste particular "
              u"debido a que la cámara no está en exáctamente la misma posición que las demás.") \

    return render_template('how_to.html', how_to=h, use_button=use_button())

def lemonscan5_how_to_detect_phisical_damage():

    h = HowTo(u"Lemonscan 5", u"Detectar daños físicos en los componentes principales")

    h.block([
        u"Identificar el [Encoder], el [Coupler] y las [Tarjetas]",
        ]) \
        .image("03.png") \

    h.block([
        u"Revisar el Encoder",
        ])\
        .text(u"El Encoder mide las RPMs del motor que impulsa las lineas hacia "
              u"el cabezal") \
        .text(u"Si la línea está en movimiento y el software no detecta la velocidad "
              u"revisar la conexión y el encoder") \
        .image("P1310554.JPG") \

    h.block([
        u"Revisar el Coupler",
        ])\
        .image("P1310555.JPG") \
        .text(u"Este dispositivo recibe la informacion del Endoder, la envia al cabezal y "
              u"procesa la respuesta del cabezal para enviar ordenes a las tarjetas que controlan las salidas") \

    h.block([
        u"Revisar las tarjetas",
        ])\
        .text(u"Las tarjetas reciben informacion del Coupler para activar los solenoides "
              u"de cada salida") \
        .text(u"Los [Leds] deben parpadear (alternado 1, 3, 5 con 2, 4, 6 )") \
        .text(u"Con el propósito de diagnosticar el estado de una tarjeta, es posible cambiar "
              u"dos tarjetas de lugar reconfigurando el ID de salida con los [Selectores]") \
        .image("P1310557_01.png") \

    return render_template('how_to.html', how_to=h, use_button=use_button())



def lemonscan5_how_to_test_solenoids_on_each_exit():

    h = HowTo(u"Lemonscan 5", u"Probar el estado de los solenoides en cada salida")

    h.block([
        u"Ir a [Visualización]",
        u"Presionar [Weight visu]",
        u"Escribir en [Test Salida] el número de salida que se desea probar",
        ])\
        .image("12_01.png") \

    h.block([
        u"Verificar visualmente que los todos los eyectores en esa salida estén funcionado bien",
        ]) \
        .text(u"El ruido que generan es subjetivo pero importante. Tiene que sonar bien. Ademas los solenoides deben saltar y regrear a su posición correctamente.") \
        .text(u"Para ver mejor es útil bajar la velocidad del [Calibrador].") \
        .image("02_01.png") \

    return render_template('how_to.html', how_to=h, use_button=use_button())

def lemonscan5_how_to_calibrate_base_diameter():

    h = HowTo(u"Lemonscan 5", u"Calibrar el diámetro base del equipo")

    h.block([
        u"Colocar en la línea una bola de diámetro conocido",
        ])\

    h.block([
        u"Ir a [Ajustes]",
        u"Pasar la bola por la cámara y comparar el [Diámetro] obtenido vs. el conocido",
        u"Para ajustar el diámetro, si es diferente, asignar el valor y luego presionar [Igualar]",
        ])\
        .image("10_01.png") \

    return render_template('how_to.html', how_to=h, use_button=use_button())



# def lemonscan5_how_to_XXX():
#
#     h = HowTo(u"Lemonscan 5", u"YYY")
#
#     h.block([
#         u"",
#         u"",
#         u"",
#         ])\
#         .image("") \
#         .text(u"") \
#         .warning(u"") \
#
#     return render_template('how_to.html', how_to=h, use_button=use_button())
#
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
        {
            'title': u"Detectar daños físicos en los componentes principales",
            'path': "lemonscan5/how_to_detect_phisical_damage",
        },
        {
            'title': u"Probar el estado de los solenoides en cada salida",
            'path': "lemonscan5/how_to_test_solenoids_on_each_exit",
        },
        {
            'title': u"Calibrar el diámetro base del equipo",
            'path': "lemonscan5\how_to_calibrate_base_diameter",
        },

    ]
    return render_template('main.html', **locals())


@app.route("/", methods=['GET'])
def welcome():
    return render_template('welcome.html')


if __name__ == "__main__":
    app.run()
