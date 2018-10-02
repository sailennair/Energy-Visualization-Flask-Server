
from flask_restplus import Namespace, Api, Resource



ns = Namespace('basic', description='Basic implementation')




@ns.route('/test')
class testing(Resource):
    def get(self):
        """Just a test"""
        return "hello world"

    def post(self):
        """this would be to post something"""
        pass