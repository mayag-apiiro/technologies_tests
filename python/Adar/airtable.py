from airtable import Airtable

base_id = "appXXXXXXXXXXXXXX"
table_name = "Table 1"
api_key = "keyXXXXXXXXXXXXXX"

airtable = Airtable(base_id, table_name, api_key)
records = airtable.get_all()

for record in records:
    print(record['fields'])