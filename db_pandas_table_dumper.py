import sqlite3


with sqlite3.connect(r"PATH/TO/DB") as db:
    table_paths = []
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        print(table_name)

for path in table_paths:
    with open(path) as f:
        print(f.read())

