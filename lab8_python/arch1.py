import mysql.connector
from mysql.connector import Error
import datetime

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

a = '1121'
if a.isdigit():
    print("111")
else:
    print("asss")
#connection = create_connection("localhost", "root", "", "delivery")
#a = (int('66'),)
#cursor = connection.cursor()


#cursor.execute('DELETE FROM supplier WHERE id = %s', a)

#connection.commit()

#print(connection.user)
#with connection.cursor() as cursor:
 #   cursor.execute("UPDATE supplier SET name = 'Жанна', address = 'Улица Роз' WHERE id = 10")
  #  connection.commit()