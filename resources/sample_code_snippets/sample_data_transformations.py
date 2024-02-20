from aladdinsdk.common.datatransformation import json_to_pandas
import json

json_raw = [{
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters":
        {
            "batter":
                [
                    {"id": "1001", "type": "Regular", "testleafarr": [1, 2, 3]},
                    {"id": "1002", "type": "Chocolate", "testleafarr": [1, 2, 3]},
                    {"id": "1003", "type": "Blueberry", "testleafarr": [1, 2, 3]},
                    {"id": "1004", "type": "Devil's Food", "testleafarr": [1, 2, 3]},
                    {"id": "1005", "type": "Vanilla", "testleafarr": [1, 2, 3]}
                ]
        },
    "topping":
        [
            {"id": "5001", "type": "None"},
            {"id": "5002", "type": "Glazed"},
            {"id": "5005", "type": "Sugar"},
            {"id": "5007", "type": "Powdered Sugar"},
            {"id": "5006", "type": "Chocolate with Sprinkles"},
            {"id": "5003", "type": "Chocolate"},
            {"id": "5004", "type": "Maple"}
        ]
}, {
    "id": "0002",
    "type": "donut2",
    "name": "Cake2",
    "ppu": 0.55,
    "batters":
        {
            "batter":
                [
                    {"id": "2001", "type": "2Regular", "testleafarr": [1, 2, 3]},
                    {"id": "2002", "type": "2Chocolate", "testleafarr": [1, 2, 3]},
                    {"id": "2003", "type": "2Blueberry", "testleafarr": [1, 2, 3]},
                    {"id": "2004", "type": "2Devil's Food", "testleafarr": [1, 2, 3]}
                ]
        },
    "topping":
        [
            {"id": "5001", "type": "None"},
            {"id": "5002", "type": "Glazed"},
            {"id": "5005", "type": "Sugar"},
            {"id": "5007", "type": "Powdered Sugar"},
            {"id": "5006", "type": "Chocolate with Sprinkles"},
            {"id": "5003", "type": "Chocolate"},
            {"id": "5004", "type": "Maple"}
        ]
}
]

# Flatten at testleafarr
df_resp = json_to_pandas.convert(json.dumps(json_raw), "[*].batters.batter.[*].testleafarr.[*]")
print(df_resp)

# Get more options to flatten on
flatten_options = json_to_pandas.conversion_options(json.dumps(json_raw))
print(f'Flatten on: {flatten_options[4]}')
print(json_to_pandas.convert(json.dumps(json_raw), flatten_options[4]))
