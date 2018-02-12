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


@app.route("/how_to_calibrate", methods=['GET'])
def how_to_calibrate():

    h = HowTo(u"Lemonscan 5", u"Manual de Calibración")

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
        u"mismos números") \

    h.block([
        u"Iniciar el equipo",
        ])

    return render_template('how_to_template.html', how_to=h, use_button=use_button())


@app.route("/main", methods=['GET'])
def main():
    return how_to_calibrate()


@app.route("/", methods=['GET'])
def welcome():
    return render_template('welcome.html')


if __name__ == "__main__":
    app.run()
