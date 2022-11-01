from flask import Flask, render_template, jsonify, request

from config import Config
from models import InputSchema, db, ma
from services import get_all_from_input_model, add_input_in_input_model


def create_app():
    """Настройка приложения Flask."""

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    return app


app = create_app()

with app.app_context():
    db.create_all()


@app.route('/')
def home_view():
    """Представление начальной страницы с выводом кнопки ввода, input и кнопки перехода на вторую страницу."""

    return render_template("home_page.html")


@app.route('/api/v1/input', methods=["GET", "POST"])
@app.route('/data')
def data_view():
    """Представление, которое выводит все данные из таблицы InputModel. А так-же обрабатывает api запросы."""

    if request.method == "POST":
        input_schema = InputSchema()
        db.session.add(add_input_in_input_model(input_schema.load(request.json)))
        db.session.commit()

    all_inputs = get_all_from_input_model()

    inputs_schema = InputSchema(many=True)
    output = inputs_schema.dump(all_inputs)
    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
