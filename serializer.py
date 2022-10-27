# from app import ma
# from models import InputModel
#
#
# class InputSchema(ma.SQLAlchemySchema):
#     """Сериалайзер для модели InputModel."""
#
#     class Meta:
#         model = InputModel
#
#         id = ma.auto_field()
#         data = ma.auto_field()
#
#     _links = ma.Hyperlinks(
#         {
#             "self": ma.URLFor("input_detail", values=dict(id="<id>")),
#             "collection": ma.URLFor("inputs"),
#         }
#     )
#
#
# input_schema = InputSchema()
# inputs_schema = InputSchema(many=True)
