import pymysql

from src.python_database.python_mysql_connect import my_sql_connect


def insert_employee(data):
    """

    Returns:

    """
    sql_insert_query = """ INSERT INTO employee
                               (name, email, age) VALUES (%s,%s,%s)"""
    print(data)
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

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        # if connection.is_connected():
        # cursor.close()
        connection.close()
        print("MySQL connection is closed")


def fetch_all_employees():
    """

    Returns:

    """

    sql_select_query = "SELECT * FROM employee"
    records = None
    try:
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

        #
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        for record in records:
            print("Employee Id = ", records[0])
            print("Name = ", records[1])
            print("Email = ", records[2])
            print("Age = ", records[3])

        print("Data fetched successfully from employee table using the prepared statement")

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        # if connection.is_connected():
        # cursor.close()
        connection.close()
        return records
        print("MySQL connection is closed")


def fetch_employee_detail_by_employee_id(employee_id):
    """

    Args:
        employee_id:

    Returns:

    """
    sql_select_query = """select * from employee where employee_id = %s"""
    record = None
    try:
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

        #
        tuple_1 = (employee_id)
        cursor.execute(sql_select_query, tuple_1)
        record = cursor.fetchone()
        print(record)
        print("Employee Id = ", record[0])
        print("Name = ", record[1])
        print("Email = ", record[2])
        print("Age = ", record[3])
        print()

        print("Data fetched successfully from employee table using the prepared statement")

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        # if connection.is_connected():
        # cursor.close()
        connection.close()
        return record
        print("MySQL connection is closed")


def update_employee_email(data):
    """

    Args:
        data:
        email:

    Returns:

    """
    sql_update_query = """UPDATE employee SET email=%s where employee_id=%s"""
    try:
        print(data['email'])
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
        tuple1 = (data['employee_id'], data['email'])
        # tuple2 = ("Harry", "harry.ellison@abzooba.com", 25)
        #
        cursor.execute(sql_update_query, tuple1)
        # cursor.execute(sql_insert_query, tuple2)
        connection.commit()
        print("Data inserted successfully into employee table using the prepared statement")

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        # if connection.is_connected():
        # cursor.close()
        connection.close()
        print("MySQL connection is closed")


# Driver Code
if __name__ == "__main__":
    fetch_employee_detail_by_employee_id(1)
