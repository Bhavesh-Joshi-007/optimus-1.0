import sqlite3
import csv

conn = sqlite3.connect("optimus.db", check_same_thread=False)
cursor = conn.cursor()

# query = '''
#     CREATE TABLE IF NOT EXISTS contacts (
#     id integer primary key, 
#     name VARCHAR(200), 
#     mobile_no VARCHAR(200),
#     email VARCHAR(200) NULL
#     )
# '''

# cursor.execute(query)


# desired_column_indices = [0, 18]

# with open('contacts.csv', 'r', encoding='utf-8') as csvFile:
#     csvReader = csv.reader(csvFile)
#     for row in csvReader:
#         selecter_data = [row[i] for i in desired_column_indices]
#         cursor.execute('''
#             INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);
#         ''',
#         tuple(selecter_data))

# conn.commit()
# conn.close()

# query = 'Bhavesh'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])