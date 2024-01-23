# Sample ADC Calls

## Simple ADC Client - Provides snowflake connection

### Instantiate ADC Client

- Connect using credentials and ADC connection options provided in user configuration yaml

    ```py
    from aladdinsdk.adc.client import ADCClient
    
    adc_client = ADCClient()
    ```

- Connect using credentials and ADC connection options provided by user

    ```py
    from aladdinsdk.adc.client import ADCClient
    
    adc_client = ADCClient(account="sample.sf.privatelink", role="ADC_ROLE", warehouse="ADC_WAREHOUSE", database="ADC_DB", schema="ADC_SCHEMA, api_key="XYZ", username="uname", password="secret")
    ```

### Query from ADC

```py
from aladdinsdk.adc.client import ADCClient

adc_client = ADCClient()
df = adc_client.query_sql('SELECT * FROM "CASH_ENTRY" LIMIT 10')
```

Get Snowflake connector to use with pandas

```py
from aladdinsdk.adc.client import ADCClient
import pandas as pd

adc_client = ADCClient()
df = pd.read_sql('SELECT * FROM "CASH_ENTRY" LIMIT 10', adc_client.get_connection())
```

### Write to ADC

```py
from aladdinsdk.adc.client import ADCClient

df_to_insert = pandas.DataFrame()

adc_client = ADCClient()
is_success, chunks_count, ingested_row_count = adc_client.write_frame(df=df_to_insert, table_name='TABLE_NAME')
```
