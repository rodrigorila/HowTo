# coding=UTF-8

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from how_to import HowTo

app = Flask(__name__)
app.config.from_object(__name__)

Bootstrap(app)
HowTo.init_app(app)

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

    return render_template('how_to_template.html', how_to=h)


@app.route("/main", methods=['GET'])
def main():
    return how_to_calibrate()


@app.route("/", methods=['GET'])
def welcome():
    return render_template('welcome.html')


if __name__ == "__main__":
    app.run()
