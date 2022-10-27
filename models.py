from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import JSONB

db = SQLAlchemy()
ma = Marshmallow()


class InputModel(db.Model):
    """Модель для данных полученных нажатием кнопки input, содержит в себе поле для jsonb формата."""

    __tablename__ = 'input_data'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"


class InputSchema(ma.SQLAlchemySchema):
    """Сериалайзер для модели InputModel."""

    class Meta:
        model = InputModel
        fields = ("id", "data")
