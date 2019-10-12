import sqlite3
from employee import Employee
#creates employee.db file to connect to
conn = sqlite3.connect('employee.db')   # for in memory connect(':memory:') database in ram, starts fresh

#cursor allows to execute sql commands
c = conn.cursor()
# """ """ -> doc strings, allows to write string that is multiple lines
#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            pay integer
#            )""")

def insert_emp(emp):
    with conn: #context managaer, dont need commit if use this
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn: 
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn: 
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 80000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

####c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")
#### ? to prevent sql injection, then pass in tuple ......first way
#c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
#conn.commit()

####second way with dictionary
#c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
#conn.commit()


#c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))#comma needed at end cause one value but tuple
####fetchone returns next row, fetchmany returns specified rows in list,
####fetchall return remaining in list // returns none or empty list if not found
#print(c.fetchall())

#c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
#print(c.fetchall())

#### commits current transaction
#conn.commit()

conn.close()
