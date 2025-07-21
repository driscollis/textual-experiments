# Gemini example
from sqlalchemy import create_engine, MetaData, Table, update

# Replace with your actual database URL
engine = create_engine('sqlite:///example.db')

metadata = MetaData()

# Reflect the 'users' table
users_table = Table('users', metadata, autoload_with=engine)

# Update the user with id=1
update_stmt = update(users_table).where(
    # Maybe use getattr() here
    users_table.c.id == 1).values(name='Updated Name', email='updated@example.com')

# Execute the update
with engine.connect() as connection:
    connection.execute(update_stmt)
    connection.commit()

print("User updated successfully.")


# ALTERNATE using dictionary
# https://stackoverflow.com/questions/23152337/how-to-update-sqlalchemy-orm-object-by-a-python-dict

from sqlalchemy import update

stmt = update(User).where(User.name == "john").values(**your_data)
session.execute(stmt)