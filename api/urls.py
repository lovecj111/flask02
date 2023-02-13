from flask import Blueprint
from flask_restful import Api
from api.views import StuQueryOneView, StuQueryAllView

bp = Blueprint("flask02", __name__, url_prefix="/flask02/")

resource = Api(bp)

resource.add_resource(StuQueryOneView, "stu/query/one")
resource.add_resource(StuQueryAllView, "stu/query/all")
