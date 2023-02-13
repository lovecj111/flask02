from api.parser import stu_query_one_parser
from flask_restful import Resource
from utils.view_base import make_response


class StuQueryOneView(Resource):
    data_parser = stu_query_one_parser

    def post(self):
        args = self.data_parser.parse_args()
        data = {"id": args["stuId"]}
        return make_response(body=data)
        # return make_response(body="success")


class StuQueryAllView(Resource):

    def get(self):
        return make_response(body="success")