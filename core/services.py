from influxdb import InfluxDBClient
import json
from flask import make_response

databaseName = 'WITS_DATA'

client = InfluxDBClient('localhost', 8086, 'root', 'root', databaseName)


def convert_date_to_full_TZ(date):
    return date + ' 00:00:00'



def convert_to_json(result):
    outputString = "["
    for item in result:
        print(item)
        y = json.dumps(item)
        outputString = outputString + y + ','
    outputString = outputString[:-1] + ']'
    return make_response(outputString)



def query_database_single_input(name):
    query = 'select * from '+ name+ ' limit 10'
    #print(query)
    result = client.query(query)
    result = result.get_points()

    x = []
    for item in result:
        x.append(item)

    testfinal = []
    for z in range(len(x)):
        temp = {'x': x[z]['time'][:-1], 'y': x[z]['kW']}
        testfinal.append(temp)

    return convert_to_json(result)



def query_database_range(name, startdate, enddate):
    startdate = convert_date_to_full_TZ(startdate)
    enddate = convert_date_to_full_TZ(enddate)
    query = "select * from " + name + " where time >= '" + startdate + "'  and time < '" + enddate + "'"
    #print(query)
    result = client.query(query)
    result = result.get_points()

    x = []
    for item in result:
        x.append(item)

    testfinal = []
    for z in range(len(x)):
        temp = {'x': x[z]['time'][:-1], 'y': x[z]['kW']}
        testfinal.append(temp)





    return convert_to_json(testfinal)

def query_one_day_pie_chart(name, startdate, enddate):
    query = "select * from " + name + " where time >= '" + startdate + "'  and time < '" + enddate + "'"
    result = client.query(query)
    result = result.get_points()
    data = []

    for item in result:
        data.append(item)

    powerfinal = []
    timefinal = []
    z = 0
    for c in range(int(len(data) / 2)):
        temp = data[z]['kW'] + data[z + 1]['kW']
        tempTime = data[z]['time']
        timefinal.append(tempTime)
        powerfinal.append(temp)
        z = z + 2

    final_result = []
    for i in range(len(powerfinal)):
        temp = {'x': timefinal[i][:-1], 'y': powerfinal[i]}
        final_result.append(temp)

    return convert_to_json(final_result)


