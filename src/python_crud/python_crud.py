import pymysql

from src.python_database.python_mysql_connect import my_sql_connect


def insert_employee():
    """

    Returns:

    """
    sql_insert_query = """ INSERT INTO employee
                               (name, email, age) VALUES (%s,%s,%s)"""
    print(0)
    try:
        print(1)
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")
        print(2)
        cursor = connection.cursor()
        print(cursor)
        # cursor.execute("select @@version")
        # output = cursor.fetchall()
        # print(output)
        tuple1 = ("Json", "json.herbart@abzooba.com", 27)
        tuple2 = ("Harry", "harry.ellison@abzooba.com", 25)

        cursor.execute(sql_insert_query, tuple1)
        cursor.execute(sql_insert_query, tuple2)
        connection.commit()

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        # if connection.is_connected():
        # cursor.close()
        connection.close()
        print("MySQL connection is closed")


# Driver Code
if __name__ == "__main__":
    insert_employee()
