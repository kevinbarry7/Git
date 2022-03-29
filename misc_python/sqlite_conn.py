import sqlite3
conn = sqlite3.connect('employee.db')

c = conn.cursor()
# c.execute("""CREATE TABLE employees (
#    first text,
#    last text,
#    pay integer)
#    """)

#c.execute("INSERT INTO employees VALUES ('Kevin', 'Barry', 50005)")
#c.execute("INSERT INTO employees VALUES ('Frank', 'Barry', 70005)")
#conn.commit()

c.execute("SELECT * from employees WHERE last='Barry'")
print(c.fetchall())

conn.commit()
conn.close()
