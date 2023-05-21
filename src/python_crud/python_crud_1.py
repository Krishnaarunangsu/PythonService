import pymysql

from src.python_database.python_mysql_connect import my_sql_connect


def insert_employee(data):
    """

    Returns:

    """
    sql_insert_query = """ INSERT INTO employee
                               (name, email, age) VALUES (%s,%s,%s)"""
    print(data)
    id = 0
    try:
        print(data['name'])
        print(1)
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")
        print(2)
        cursor = connection.cursor()
        # print(cursor)
        # # cursor.execute("select @@version")
        # # output = cursor.fetchall()
        # # print(output)
        tuple1 = (data['name'], data['email'], data['age'])
        # tuple2 = ("Harry", "harry.ellison@abzooba.com", 25)
        #
        cursor.execute(sql_insert_query, tuple1)
        # cursor.execute(sql_insert_query, tuple2)
        connection.commit()
        print("Data inserted successfully into employee table using the prepared statement")
        # response = jsonify(message='User added successfully.', id=cursor.lastrowid)
        id = cursor.lastrowid
        message = f'User added successfully.'

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
        # id = cursor.lastrowid
        message = f'User cannot be added.'
    finally:
        # if connection.is_connected():
        cursor.close()
        connection.close()
        return id, message
        # print("MySQL connection is closed")


def fetch_all_employees():
    """

    Returns:

    """

    sql_select_query = "SELECT * FROM employee"
    records = None
    message = None
    try:
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")
        cursor = connection.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        emp_records = []
        for row in records:
            # print(row[0], '-', row[1], '-', row[2], '-', row[3])
            record = dict(employee_id=row[0], name=row[1], email=row[2], age=row[3])
            print(record)
            emp_records.append(record)
        # for record in records:
        #     print("Employee Id = ", record[0])
        #     print("Name = ", record[1])
        #     print("Email = ", record[2])
        #     print("Age = ", record[3])

        # message = f'Total {records.count()} have been fetched successfully'
        # print("Data fetched successfully from employee table using the prepared statement")

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
        # message = f'Some Problems. No records are fetched'
    finally:
        # if connection.is_connected():
        # cursor.close()
        connection.close()
        return emp_records
        print("MySQL connection is closed")


def fetch_employee_detail_by_employee_id(employee_id):
    """

    Args:
        employee_id:

    Returns:

    """
    sql_select_query = """select * from employee where employee_id = %s"""
    connection = None
    emp_record = None
    row_fetched = None
    try:
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")
        cursor = connection.cursor()
        # print(cursor)
        # # cursor.execute("select @@version")
        # # output = cursor.fetchall()
        # # print(output)

        #
        print(f'Employee Id:{employee_id}')
        tuple_1 = (employee_id)
        row_fetched = cursor.execute(sql_select_query, tuple_1)
        print(f'Row Fetched:{row_fetched}')
        record = cursor.fetchone()
        # print(record)
        # print("Employee Id = ", record[0])
        # print("Name = ", record[1])
        # print("Email = ", record[2])
        # print("Age = ", record[3])
        print('Coming Here')
        if row_fetched == 1:
            emp_record = dict(employee_id=record[0], name=record[1], email=record[2], age=record[3])
            print(f'Employee:{emp_record}')
        elif row_fetched == 0:
            pass
        print('Coming Here')

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
        # message = f'No record cannot be fetched for the specified employee id:{employee_id}'
    finally:
        # if connection.is_connected():
        # cursor.close()
        if connection is not None:
            connection.close()
        print(f'Row Fetched:{row_fetched}')
        return row_fetched, emp_record
        print("MySQL connection is closed")


def update_employee_email(data):
    """

    Args:
        data:

    Returns:

    """
    sql_update_query = """UPDATE employee SET email=%s where employee_id=%s"""
    connection = None
    cursor = None
    row_count = None
    try:
        print(data['email'])
        print(1)
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")
        cursor = connection.cursor()
        # print(cursor)
        # # cursor.execute("select @@version")
        # # output = cursor.fetchall()
        # # print(output)
        tuple1 = (data['email'], data['employee_id'])
        # tuple1 = ('abc.xyz@abz.com', 4)
        # tuple2 = ("Harry", "harry.ellison@abzooba.com", 25)
        #
        row_count = cursor.execute(sql_update_query, tuple1)
        # cursor.execute(sql_insert_query, tuple2)
        connection.commit()
        # print("Data updated successfully into employee table using the prepared statement")

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
        # print("MySQL connection is closed")
        return row_count


def delete_employee(data):
    """

    Args:
        data:

    Returns:

    """
    sql_delete_query = """DELETE FROM employee WHERE employee_id=%s"""
    connection = None
    cursor = None
    row_count = None
    try:
        print(data['employee_id'])
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")
        cursor = connection.cursor()
        # print(cursor)
        # # cursor.execute("select @@version")
        # # output = cursor.fetchall()
        # # print(output)
        tuple1 = (data['employee_id'])
        # tuple1 = (5)
        # tuple2 = ("Harry", "harry.ellison@abzooba.com", 25)
        #
        row_count = cursor.execute(sql_delete_query, tuple1)
        # cursor.execute(sql_insert_query, tuple2)
        connection.commit()
        print("Data deleted successfully")

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
        return row_count
        # print("MySQL connection is closed")


# Driver Code
if __name__ == "__main__":
    # fetch_employee_detail_by_employee_id(5)
    # data = {'employee_id': 3, 'email': 'krishna.kumar@abzooba.com'}
    # update_employee_email(data)
    data = {'employee_id': 6}
    count = delete_employee(data)
    print(count)
    # delete_employee()
    # fetch_all_employees()
