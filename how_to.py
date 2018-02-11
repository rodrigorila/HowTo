from flask import url_for
from jinja2 import Markup, escape
from re import compile


class Details:

    def __init__(self, type, value):
        self.type = type
        self.value = value


class Block:
    def __init__(self, items):
        self.items = items
        self.details = []

    def text(self, text):
        self.details.append(Details("text", text))
        return self

    def warning(self, message):
        self.details.append(Details("warning", message))
        return self

    def image(self, image_name):
        path = url_for('static', filename='images/{}'.format(image_name))
        self.details.append(Details("image", path))
        return self

    @property
    def has_details(self):
        return len(self.details) > 0


class HowTo:

    _brackets_to_html_ = compile(r'\[(.*?)\]')

    @staticmethod
    def init_app(app):

        @app.context_processor
        def jinja2_template_utilities():

            def highlighted_text(value):
                matches = HowTo._brackets_to_html_.finditer(value)

                index = 0
                result = None

                for m in matches:
                    w1, w2 = m.span(0)
                    p1, p2 = m.span(1)

                    normal_text = escape(value[index: w1])
                    highlighted = escape(value[p1: p2])
                    index = w2

                    result = normal_text if result is None else result + normal_text
                    result += Markup('<code>') + highlighted + Markup('</code>')

                return value if result is None else result

            return dict(highlighted_text=highlighted_text)

    def __init__(self, heading, title):
        self.heading = heading
        self.title = title
        self.blocks = []

    def block(self, items):
        b = Block(items)
        self.blocks.append(b)
        return b
