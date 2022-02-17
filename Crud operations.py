import sqlite3

from sqlite3 import Error


def sql_connection():
    try:
        conn = sqlite3.connect('test.db')
        return conn
    except Error:
        print(Error)
def sql_table(conn):
    cursorObj = conn.cursor()
     cursorObj.execute("CREATE TABLE employee(emp_id n(5), name char(30), dept char(35));")
    # #  # Insert records
     cursorObj.executescript("""
    
      INSERT INTO employee VALUES(5001,'pranee', 'design');
      INSERT INTO employee VALUES(5002,'prasu', 'testing');
      INSERT INTO employee VALUES(5003,'neeru', 'frontend');
      INSERT INTO employee VALUES(5004,'raja', 'backend');
      INSERT INTO employee VALUES(5005,'rani', 'manager');
     """)
    # conn.commit()
    cursorObj.execute("SELECT * FROM employee")
    rows = cursorObj.fetchall()
    print("Employee details:")
    for row in rows:
        print(row)
    print("\ninsert the employee details:")
    cursorObj = conn.cursor()
    cursorObj.execute('''INSERT INTO employee (emp_id,name,dept)VALUES(5006,'ramu','hr')''')
    cursorObj.execute("SELECT * FROM employee")
    conn.commit()
    rows = cursorObj.fetchall()
    print("Employee details:")
    for row in rows:
        print(row)
    print("update the employee details\n")
    cursorObj = conn.cursor()
    cursorObj.execute('''UPDATE employee SET name='ram',dept='hr' WHERE emp_id=5002''')
    conn.commit()
    cursorObj.execute("SELECT * FROM employee")
    rows = cursorObj.fetchall()
    print("Employee details:")
    for row in rows:
        print(row)
    print("\nDelete the employee details:")
    cursorObj = conn.cursor()
    cursorObj.execute('''DELETE FROM employee WHERE emp_id in (5005)''')
    conn.commit()
    cursorObj.execute("SELECT * FROM employee")
    # conn.commit()
    rows = cursorObj.fetchall()
    print("Employee details:")
    for row in rows:
        print(row)
sqllite_conn = sql_connection() #test.db
sql_table(sqllite_conn) #test.db
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")