import pymysql


def my_sql_connect():
    """

    Returns:

    """
    connection = None
    try:
        connection = pymysql.connect(host='localhost',
                                     database='narayan',
                                     user='root',
                                     password="Narayan@15")

        cursor = connection.cursor()
        cursor.execute("select @@version")
        output = cursor.fetchall()
        print(output)

    except pymysql.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        # if connection.is_connected():
        # cursor.close()
        connection.close()
        print("MySQL connection is closed")


# Driver Code
if __name__ == "__main__":
    my_sql_connect()
