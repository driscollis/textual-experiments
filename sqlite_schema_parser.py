import sqlite3
import sqlite_utils

# DBs
chinook =  r"C:\Chinook_Sqlite.sqlite"
library = r"C:\books\creating_tuis\code\20_sqlite_client\original_version\library.db"
pim = r"C:\Users\wheifrd\.local\share\pim\game_data.sqlite"

print(f"Schema for: {chinook}")
db = sqlite_utils.Database(chinook)
schema = db.schema
print(schema)


def parse_out_fields(schema: str):
    for line in schema.split("\n")[1:]:
        field_schema = line.strip()
        field_schema = field_schema.replace("[", '"')
        field_schema = field_schema.replace("]", '"')
        field_schema = field_schema.replace(",", "")

        line = line.strip()
        if not line:
            continue
        items = [i.strip() for i in line.split(",") if i]
        if line.endswith(",") and line.count(",") == 1:
            # Clean line
            line = line.replace("[", "")
            line = line.replace("]", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.replace(",", "")
            # End of field
            field_name, field_type, *_ = line.split()
        print(f"{field_name=}    {field_type}")

def parse_schema(db_path):

    sql = "SELECT * FROM sqlite_master;"
    conn = sqlite3.connect(chinook)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for item in result:
        _, table_name, _, _, schema = item
        print("\n" + ("#" * 80))
        print(f"{table_name = }\n\n{schema}")

        if "CREATE TABLE" in schema:
            parse_out_fields(schema)

parse_schema(chinook)

#sql = "SELECT * FROM sqlite_master;"
#conn = sqlite3.connect(pim)
#cursor = conn.cursor()
#cursor.execute(sql)
#result = cursor.fetchall()
#print("\n" + ("#" * 80))
#print(result[0])

#print("#" * 80)
#print(f"Schema for: {library}")
#db = sqlite_utils.Database(library)
#schema = db.schema
#print(schema)

#print("#" * 80)
#print(f"Schema for: {pim}")
#db = sqlite_utils.Database(pim)
#schema = db.schema
#print(schema)


