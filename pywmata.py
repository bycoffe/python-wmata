import datetime
from urllib import urlencode
from urllib2 import urlopen

try:
    import json
except ImportError:
    import simplejson as json


class WmataException(Exception):
    pass


class Wmata(object):

    base_url = 'http://api.wmata.com/%(svc)s.svc/json/%(endpoint)s'

    def __init__(self, apikey):
        self.apikey = apikey

    def _build_url(self, svc, endpoint, query={}):
        query.update({'api_key': self.apikey})
        query.update({'subscription-key': self.apikey})
        url = self.base_url % {'svc': svc, 'endpoint': endpoint}
        return '%s?%s' % (url, urlencode(query))

    def _get(self, svc, endpoint, query={}):
        self.url = self._build_url(svc, endpoint, query)
        response = urlopen(self.url)

        if response.msg == 'OK':
            self.data = json.loads(response.read())
            return self.data

        raise WmataException('Got invalid response from WMATA server: %s' % response.msg)

    def lines(self):
        return self._get('Rail', 'JLines')['Lines']

    def stations(self, line_code):
        return self._get('Rail', 'JStations', {'LineCode': line_code})['Stations']

    def station_info(self, station_code):
        return self._get('Rail', 'JStationInfo', {'StationCode': station_code})

    def rail_path(self, from_station_code, to_station_code):
        return self._get('Rail', 'JPath', {'FromStationCode': from_station_code, 'ToStationCode': to_station_code})['Path']

    def rail_predictions(self, station_code='All'):
        return self._get('StationPrediction', 'GetPrediction/%s' % station_code)['Trains']

    def rail_incidents(self):
        return self._get('Incidents', 'Incidents')

    def elevator_incidents(self, station_code='All'):
        return self._get('Incidents', 'ElevatorIncidents', {'StationCode': station_code})

    def station_entrances(self, latitude=0, longitude=0, radius=0):
        return self._get('Rail', 'JStationEntrances', {'lat': latitude, 'lon': longitude, 'radius': radius})['Entrances']

    def bus_routes(self):
        return self._get('Bus', 'JRoutes')['Routes']

    def bus_stops(self):
        return self._get('Bus', 'JStops')['Stops']

    def bus_schedule_by_route(self, route_id, date=None, including_variations=False):
        if date is None:
            date = datetime.date.today().strftime('%Y-%m-%d')
        if including_variations:
            including_variations = 'true'
        else:
            including_variations = 'false'
        return self._get('Bus', 'JRouteSchedule', {'routeId': route_id, 'date': date, 'includingVariations': including_variations})

    def bus_route_details(self, route_id, date=None):
        if date is None:
            date = datetime.date.today().strftime('%Y-%m-%d')
        return self._get('Bus', 'JRouteDetails', {'routeId': route_id, 'date': date})

    def bus_positions(self, route_id, including_variations=False):
        if including_variations:
            including_variations = 'true'
        else:
            including_variations = 'false'
        return self._get('Bus', 'JBusPositions', {'routeId': route_id, 'includingVariations': including_variations})['BusPositions']

    def bus_schedule_by_stop(self, stop_id, date=None):
        if date is None:
            date = datetime.date.today().strftime('%Y-%m-%d')
        return self._get('Bus', 'JStopSchedule', {'stopId': stop_id, 'date': date})

    def bus_prediction(self, stop_id):
        return self._get('NextBusService', 'JPredictions', {'stopId': stop_id})
