from influxdb import InfluxDBClient

INFLUXDB_ADDRESS = 'localhost'
INFLUXDB_USER = 'user'
INFLUXDB_PASSWORD = 'userpass'
INFLUXDB_DATABASE = 'defaultdb'

class DB(object):
    def __init__(self):
        super(DB, self).__init__()
        self.influxdb_client = InfluxDBClient(host=INFLUXDB_ADDRESS, port=8086,
        username = INFLUXDB_USER, password = INFLUXDB_PASSWORD, database = INFLUXDB_DATABASE)

    def write_sensor_data(self, location, measurement, value):
        json_body = [
            {
                'measurement': measurement,
                'tags': {
                    'location': location,
                },
                'fields': {
                    'value': value
                }
            }
        ]
        self.influxdb_client.write_points(json_body)

