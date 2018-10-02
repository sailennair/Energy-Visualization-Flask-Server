from flask_restplus import Namespace, Resource
from core.services import query_database_single_input, query_database_range, query_one_day_pie_chart

ns = Namespace('range', description='Choose range of dates for data to be collected.')

@ns.route('/<string:name>/<string:startDate>/<string:endDate>')
class RangeGraph(Resource):

    def get(self, name, startDate, endDate):
        """This gets some advanced graphs"""
        return query_database_range(name, startDate, endDate)


@ns.route('/<string:name>')
class AllData(Resource):
    def get(self, name):
        """This gets some advanced graphs"""
        return query_database_single_input(name)


@ns.route('/pi/<string:name>/<string:startDate>/<string:endDate>')
class PiChartSingleDay(Resource):
    def get(self, name, startDate, endDate):
        """Returns data for a pie chart where each hour gives the total energy consumed in the hour"""
        return query_one_day_pie_chart(name, startDate, endDate)

