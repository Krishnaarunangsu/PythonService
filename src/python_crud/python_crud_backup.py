import pymysql

from src.python_database.python_mysql_connect import my_sql_connect


def insert_employee(employee_data: dict):
    """

    Args:
        employee_data:

    Returns:

    """
    sql_insert_query = """ INSERT INTO employee
                               (name, email, age) VALUES (%s,%s,%s)"""
    connection = None
    cursor = None
    row_count = None
    latest_id = 0
    try:
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")
        cursor = connection.cursor()
        tuple1 = (employee_data['name'], employee_data['email'], employee_data['age'])
        row_count = cursor.execute(sql_insert_query, tuple1)
        connection.commit()
        latest_id = cursor.lastrowid
        message = f'User added successfully.'
    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
        message = f'User cannot be added.'
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
        return latest_id, row_count, message


def fetch_all_employees():
    """

    Returns:

    """

    sql_select_query = "SELECT * FROM employee"
    connection = None
    cursor = None
    row_count = None
    emp_records = []
    try:
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")
        cursor = connection.cursor()
        row_count = cursor.execute(sql_select_query)
        records = cursor.fetchall()
        if row_count > 0:
            for row in records:
                record = dict(employee_id=row[0], name=row[1], email=row[2], age=row[3])
                print(record)
                emp_records.append(record)
        elif row_count == 0:
            pass
    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
        return row_count, emp_records


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
        print(f'Employee Id to be updated:{employee_id}')
        tuple_1 = (employee_id)
        row_fetched = cursor.execute(sql_select_query, tuple_1)
        record = cursor.fetchone()
        if row_fetched == 1:
            emp_record = dict(employee_id=record[0], name=record[1], email=record[2], age=record[3])
            print(f'Employee:{emp_record}')
        elif row_fetched == 0:
            pass
    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        if connection is not None:
            connection.close()
        return row_fetched, emp_record


def update_employee_email(employee_data):
    """

    Args:
        employee_data:

    Returns:

    """
    sql_update_query = """UPDATE employee SET email=%s where employee_id=%s"""
    connection = None
    cursor = None
    row_count = None
    try:
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")
        cursor = connection.cursor()
        tuple1 = (employee_data['email'], employee_data['employee_id'])
        row_count = cursor.execute(sql_update_query, tuple1)
        connection.commit()
    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
        return row_count


def delete_employee(employee_data):
    """

    Args:
        employee_data:

    Returns:

    """
    sql_delete_query = """DELETE FROM employee WHERE employee_id=%s"""
    connection = None
    cursor = None
    row_count = None
    try:
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")
        cursor = connection.cursor()
        tuple1 = (employee_data['employee_id'])
        row_count = cursor.execute(sql_delete_query, tuple1)
        connection.commit()
    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
        return row_count


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
