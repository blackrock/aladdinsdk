# Sample Calls For Export Data

- Import the export utility from aladdinsdk.common
- Arguments to be passed in: input data to be exported, file path for exporting, export type (currently supported - csv, excel, json, pickle)

    ```py
    import datetime
    from aladdinsdk.common.exports import export
    import json
    
    input_obj = {
    'obj'  : 1,
    'obj2' : True,
    'obj3' : datetime.date(2020, 1, 5).isoformat(),
    'obj4' : [1,2,3],
    'obj5' : datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc).isoformat()
    }

    export.export_data(input_obj, ADD_FILE_LOCATION_HERE, "csv")

    # code snippet when user want to overwrite existing data in the file via function param
    export.export_data(input_obj, ADD_FILE_LOCATION_HERE, "csv", True)

    ```

