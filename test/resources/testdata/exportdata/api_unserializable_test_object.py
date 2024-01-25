import datetime


class ApiUnserializableTestObject:
    def __init__(self):
        self.departing_station_facilities_slice = None
        self.departing_station_summary_slice = None
        self.departing_train_station_id = 'TS_1441'
        self.destination_station_facilities_slice = None
        self.destination_station_summary_slice = None
        self.destination_train_station_id = 'TS_786'
        self.id = 'TJ_0'
        self.journey_date = datetime.date(2020, 1, 5)
        self.journey_duration = '18000s'
        self.journey_time = datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)
        self.pass_through_station_ids = ['TS_1441', 'TS_2557', 'TS_747', 'TS_1650', 'TS_224', 'TS_786']
        self.short_code = 'KGXEDB2020150'
        self.train_id = 'T_0'
        self.train_summary = None

    def to_dict(self):
        return {}
