import sqlite3
from sqlite_emp import Employee

db_conn = sqlite3.connect(':memory:') # gives a db that lives in ram. Useful for testing coz we can have a fresh db for every run
# db_conn = sqlite3.connect('sqlite_emp.db')

# cursor object to execute queries
curs = db_conn.cursor()

'''
# create emp table
curs.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
                )""")

# curs.execute("INSERT INTO employees VALUES ('John', 'Smith', '50000')")

# curs.execute("INSERT INTO employees VALUES ('Ann', 'Smith', '70000')")
#
# db_conn.commit()

# curs.execute("SELECT * FROM employees WHERE last = 'Rogers'") # returns an iterable
# curs.execute("SELECT * FROM employees WHERE last = 'Smith'") # will do an auto-commit of the insert above

# print(curs.fetchone()) # gets the next row in the result and returns only that row. And if no more rows are available then just returns None

# print(curs.fetchall())

# curs.fetchmany(5) # takes an arg of numbers and returns that many rows of results and list. returns an empty list if no more rows are available

# curs.fetchall() #gets the rem rows and returns as list. returns empty list if no more rows

emp1 = Employee('John', 'Doe', 70000)
emp2 = Employee('Jane', 'Doe', 90000)

# print(emp1.first, emp1.last, emp1.pay)

""" Pass variables to DB"""
# curs.execute("INSERT INTO employees VALUES ('{}', '{}', '{}')".format(emp1.first, emp1.last, emp1.pay))
curs.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp1.first, emp1.last, emp1.pay)) # even if there's one value, it needs to passed as a tuple
db_conn.commit()

curs.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp1.first, 'last': emp1.last, 'pay': emp1.pay})
db_conn.commit()

""" Use variables to query data"""
curs.execute("SELECT * FROM employees WHERE last=?", ('Smith',))
print(curs.fetchall())

curs.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
print(curs.fetchall())

# commits the current transaction
db_conn.commit()

db_conn.close()'''

curs.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
                )""")


def insert_emp(emp):
    with db_conn:
        curs.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                    {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    curs.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return curs.fetchall()


def update_pay(emp, pay):
    with db_conn:
        curs.execute("""UPDATE employees SET pay = :pay
                        WHERE first = :first AND last = :last""",
                     {'first': emp.first, 'last': emp.last, 'pay':pay})


def remove_emp(emp):
    with db_conn:
        curs.execute("DELETE from employees WHERE first = :first AND last = :last",
                     {'first': emp.first, 'last': emp.last})


emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp1)
insert_emp(emp2)

emps1 = get_emps_by_name('Doe')
# emps2= get_emps_by_name(emp1.last)

print(emps1)
# print(emps2)

update_pay(emp2, 95000)
remove_emp(emp1)

emps = get_emps_by_name('Doe')
print(emps)

db_conn.close()
