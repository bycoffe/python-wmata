# python-wmata
This is a Python library for accessing data via the WMATA Metro Transparent Data Sets API. More information is available at [http://developer.wmata.com](http://developer.wmata.com)

## Requirements
Python >= 2.6 or (Python >= 2.5 and simplejson)

## Usage

    >>> from pywmata import Wmata

    >>> # Initialize the API with your API key (available from http://developer.wmata.com/):
    >>> api = Wmata(YOUR_API_KEY)

    >>> # Get a list of all WMATA rail lines:
    >>> lines = api.lines()
    >>> print lines[0]
    {u'DisplayName': u'Blue',
     u'EndStationCode': u'G05',
     u'InternalDestination1': u'',
     u'InternalDestination2': u'',
     u'LineCode': u'BL',
     u'StartStationCode': u'J03'}

    >>> # Get a list of all stations on the Green line:
    >>> stations = api.stations('GR')
    >>> print stations[:2]
    [{u'Code': u'F11',
      u'Lat': 38.826446348300003,
      u'LineCode1': u'GR',
      u'LineCode2': None,
      u'LineCode3': None,
      u'LineCode4': None,
      u'Lon': -76.911464217700001,
      u'Name': u'Branch Avenue',
      u'StationTogether1': u'',
      u'StationTogether2': u''},
     {u'Code': u'F10',
      u'Lat': 38.843964554400003,
      u'LineCode1': u'GR',
      u'LineCode2': None,
      u'LineCode3': None,
      u'LineCode4': None,
      u'Lon': -76.931870158899997,
      u'Name': u'Suitland',
      u'StationTogether1': u'',
      u'StationTogether2': u''}]

    >>> # Get a list of station entrances within a radius of a certain point. The radius should be given in meters:
    >>> stations = api.station_entrances(38.906972, -77.042938, 500)
    >>> print stations
    [{u'Description': u'Dupont Circle, South',
      u'ID': u'168',
      u'Lat': 38.908647000000002,
      u'Lon': -77.043339000000003,
      u'Name': u'Dupont Circle South',
      u'StationCode1': u'A03',
      u'StationCode2': u''},
     {u'Description': u'Farragut North, Connecticut & L Sts. (East exit)',
      u'ID': u'105',
      u'Lat': 38.903900999999998,
      u'Lon': -77.039859000000007,
      u'Name': u'Farragut North Connecticut & L Sts. (East exit)',
      u'StationCode1': u'A02',
      u'StationCode2': u''},
     {u'Description': u'Farragut North, Connecticut & L Sts. (West exit)',
      u'ID': u'104',
      u'Lat': 38.903559999999999,
      u'Lon': -77.040413000000001,
      u'Name': u'Farragut North Connecticut & L Sts. (West exit)',
      u'StationCode1': u'A02',
      u'StationCode2': u''},
     {u'Description': u'Dupont Circle, North (Q & Connecticut)',
      u'ID': u'97',
      u'Lat': 38.910969000000001,
      u'Lon': -77.044689000000005,
      u'Name': u'Dupont Circle North (Q & Connecticut)',
      u'StationCode1': u'A03',
      u'StationCode2': u''}]

    >>> # Get the rail path between stations D02 (Smithsonian) and D04 (Federal Center):
    >>> rail_path = api.rail_path('D02', 'D04')
    >>> print rail_path
    [{u'DistanceToPrev': 0,
      u'LineCode': u'BL',
      u'SeqNum': 16,
      u'StationCode': u'D02',
      u'StationName': u'Smithsonian'},
     {u'DistanceToPrev': 2643,
      u'LineCode': u'BL',
      u'SeqNum': 17,
      u'StationCode': u'D03',
      u'StationName': u"L'Enfant Plaza"},
     {u'DistanceToPrev': 1757,
      u'LineCode': u'BL',
      u'SeqNum': 18,
      u'StationCode': u'D04',
      u'StationName': u'Federal Center SW'}]

    >>> # Get the current rail predictions for station F04 (Waterfront/SEU):
    >>> predictions = api.rail_prediction('F04')
    >>> print predictions
    [{u'Car': u'6',
      u'Destination': u'Grnbelt',
      u'DestinationCode': u'E10',
      u'DestinationName': u'Greenbelt',
      u'Group': u'1',
      u'Line': u'GR',
      u'LocationCode': u'F04',
      u'LocationName': u'Waterfront',
      u'Min': u'ARR'},
     {u'Car': u'6',
      u'Destination': u'Grnbelt',
      u'DestinationCode': u'E10',
      u'DestinationName': u'Greenbelt',
      u'Group': u'1',
      u'Line': u'GR',
      u'LocationCode': u'F04',
      u'LocationName': u'Waterfront',
      u'Min': u'6'},
     {u'Car': u'6',
      u'Destination': u'Brnch Av',
      u'DestinationCode': u'F11',
      u'DestinationName': u'Branch Avenue',
      u'Group': u'2',
      u'Line': u'GR',
      u'LocationCode': u'F04',
      u'LocationName': u'Waterfront',
      u'Min': u'8'},
     {u'Car': u'8',
      u'Destination': u'Grnbelt',
      u'DestinationCode': u'E10',
      u'DestinationName': u'Greenbelt',
      u'Group': u'1',
      u'Line': u'GR',
      u'LocationCode': u'F04',
      u'LocationName': u'Waterfront',
      u'Min': u'11'},
     {u'Car': u'6',
      u'Destination': u'Brnch Av',
      u'DestinationCode': u'F11',
      u'DestinationName': u'Branch Avenue',
      u'Group': u'2',
      u'Line': u'GR',
      u'LocationCode': u'F04',
      u'LocationName': u'Waterfront',
      u'Min': u'14'},
     {u'Car': u'6',
      u'Destination': u'Brnch Av',
      u'DestinationCode': u'F11',
      u'DestinationName': u'Branch Avenue',
      u'Group': u'2',
      u'Line': u'GR',
      u'LocationCode': u'F04',
      u'LocationName': u'Waterfront',
      u'Min': u'19'}]

    >>> # Get a list of current rail incidents:
    >>> incidents = api.rail_incidents()
    >>> print incidents
    {u'Incidents': []}

    >>> # Get a list of current elevator incidents:
    >>> elevator_incidents = api.elevator_incidents()
    >>> print elevator_incidents
    {u'ElevatorIncidents': []}
