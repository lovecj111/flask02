from flask_restful import reqparse

stu_query_one_parser = reqparse.RequestParser()
stu_query_one_parser.add_argument("stuId", type=int, default=0, location='args')
