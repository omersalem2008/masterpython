# --------------------------------------------------------
# -- Databases => SQLite => Very Important Informations --
# --------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

my_tuple = ('Pascal', '65', 4)

# Inserting Data
cr.execute("insert into skills values(?, ?, ?)", my_tuple) #inserting data
#into the skills table so the values are passed as a tuple and this method
# is used to insert data into the table to prevent sql injection attacks

# Fetch Data From Database
cr.execute("select * from skills order by name limit 3 offset 2")
#order by name is used to sort the data in ascending order
# and limit 3 is used to limit the number of rows returned to 3
# and offset 2 is used to skip the first 2 rows
# asc is used to sort the data in ascending order
# and desc is used to sort the data in descending order

# if you want to learn mysql which is similar to sqlite3 go to here
# https://www.youtube.com/watch?v=DftlOK7fCtc&list=PLDoPjvoNmBAz6DT8SzQ1CODJTH-NIA7R9

# cr.execute("select * from skills where user_id > 1")
cr.execute("select * from skills where user_id not in(1, 2, 3)")
# here it will select all the rows from the skills table where 
# the user_id is not in the list of user_ids (1, 2, 3)

# Assign Data To Variable
results = cr.fetchall()

# Loop On Results
for row in results:

  print(f"Skill Name => {row[0]},", end=" ")
  print(f"Skill Progress => {row[1]},", end=" ")
  print(f"User ID => {row[2]}")

# Save (Commit) Changes
db.commit()

# Close Database
db.close()