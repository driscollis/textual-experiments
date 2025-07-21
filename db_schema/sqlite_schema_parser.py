import sqlite3


def parse_out_fields(schema: str) -> dict[str, dict[str, str]]:
    fields = {}
    schema = schema.replace("\t", "")

    if "CREATE TABLE" in schema and "(" in schema:
        location = schema.find("(")
        schema2 = schema[location:]
        schema2 = schema2.replace("\n", "")
        lines = [i.strip() for i in schema2.split(",")]

    for line in lines:
        line = line.strip()

        if not line_is_table_field(line):
            continue

        field_schema = parse_field_schema(line)

        if line.endswith(",") and line.count(",") == 1:
            parse_fields(line, fields, field_schema)
        elif line.count(",") == 0:
            parse_fields(line, fields, field_schema)
        elif (line.startswith("(") and line.count(",") >= 1) or line.endswith(")") and line.count(",") >= 1:
            for sub_line in line.split(","):
                sub_line = sub_line.strip()
                if not line_is_table_field(sub_line):
                    continue
                if sub_line:
                    field_schema = parse_field_schema(sub_line)
                    parse_fields(sub_line, fields, field_schema)
        elif line.endswith(","):
            parse_fields(line, fields, field_schema)
        else:
            print(line)
            raise NotImplementedError

    return fields

def line_is_table_field(line: str) -> bool:
    if not line:
        return False

    if len(line) == 1:
        return False

    if line.startswith("FOREIGN KEY") or line.startswith("PRIMARY KEY"):
        return False

    if line.startswith("ON DELETE"):
        return False

    if line.startswith("CONSTRAINT "):
        return False

    return True

def parse_fields(line: str, fields: dict, field_schema: str) -> dict[str, dict[str, str]]:
    # Clean line
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = line.replace("(", "")
    line = line.replace(")", "")
    line = line.replace(",", "")
    # End of field
    try:
        field_name, field_type, *_ = line.split()
    except ValueError:
        field_name = line
        field_type = line

    field_name = field_name.strip()
    if field_name in fields:
        # do not update the fields a second time
        return fields
    fields[field_name] = {}
    fields[field_name]["Type"] = field_type
    fields[field_name]["Schema"] = field_schema
    return fields

def parse_field_schema(line: str) -> str:
    field_schema = line.strip()
    field_schema = field_schema.replace(",", "")
    if field_schema.startswith("("):
        field_schema = field_schema.replace("(", "")
    if ") WITHOUT" in line:
        field_schema = field_schema[:field_schema.find(") WITHOUT")]
    field_name, *parts = field_schema.split()
    field_name = field_name.replace("[", '"')
    field_name = field_name.replace("]", '"')
    field_name = field_name.replace("(", "")
    field_name = field_name.replace(")", "")
    field_name = field_name.replace('"', "")
    field_schema = line.strip()
    field_schema = f'"{field_name}" {" ".join(parts)}'
    field_schema = field_schema.replace(",", "")
    return field_schema

def parse_schema(db_path):

    sql = "SELECT * FROM sqlite_master;"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    tables = {}
    for item in result:
        _, table_name, _, _, schema = item

        if schema is None:
            continue

        if "CREATE TABLE" in schema:
            fields = parse_out_fields(schema)
            tables[table_name] = {}
            tables[table_name]["Schema"] = schema
            tables[table_name]["Fields"] = fields

    return tables



# DBs
chinook =  r"C:\Chinook_Sqlite.sqlite"
library = r"C:\books\creating_tuis\code\20_sqlite_client\original_version\library.db"
pim = r"C:\Users\wheifrd\.local\share\pim\game_data.sqlite"

prefs = r"C:\asql\content-prefs.sqlite"
cookies = r"C:\asql\cookies.sqlite"
domain = r"C:\asql\domain_to_categories.sqlite"

parse_schema(domain)
#parse_out_fields('CREATE TABLE sqlite_sequence(name,seq)')


#schema = ('CREATE TABLE grids (\n'
 #'                game_id INTEGER NOT NULL,\n'
 #'                user_id INTEGER NOT NULL,\n'
 #'                sub_grid_id TEXT NOT NULL,\n'
 #'                grid_data TEXT NOT NULL,\n'
 #'                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE '
 #'CASCADE,\n'
 #'                FOREIGN KEY(game_id) REFERENCES games(id) ON DELETE '
 #'CASCADE,\n'
 #'                PRIMARY KEY (game_id, user_id, sub_grid_id)\n'
 #'            )')
#parse_out_fields(schema)