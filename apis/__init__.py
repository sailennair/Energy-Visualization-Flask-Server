from flask_restplus import Api

from .basicGraphs import ns as ns1
from .advancedGraphs import ns as ns2

api = Api(title='The Visualization Application',
          version='1.0',
          description='A general visualization API for energy. The api retrieves data from an influxDB database and '
                      'returns the data as required')

api.add_namespace(ns1)
api.add_namespace(ns2)