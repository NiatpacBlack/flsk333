from models import InputModel


def get_all_from_input_model():
    """Возвращает QuerySet со всеми данными из таблицы InputModel."""

    return InputModel.query.all()


def add_input_in_input_model(request_dict: dict):
    return InputModel(**request_dict)
