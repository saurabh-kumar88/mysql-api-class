import mysql.connector
from mysql.connector.connection import MySQLConnection

class MySql:
  def __init__(self, host, user, password, database) -> None:
      self.__host = host
      self.__user = user
      self.__password = password
      self.__database = database
      
  
  def create_connection(self) -> MySQLConnection:
    try:
        self.con = mysql.connector.connect(
          host = self.__host,
          user = self.__user,
          password = self.__password,
          database = self.__database
        )
        self.cur = self.con.cursor()
    except Exception as err:
      print(err)
    return self.con

  def execute_query(self, query) -> tuple:
    """"Read only queries, does not change state of records"""
    records: list = []
    if len(query) == 0:
      raise Exception("Invalid query")

    con = self.create_connection()
    cur = con.cursor()

    try:
      cur.execute(query)
      print('query completed!')
      for r in cur.fetchall():
        records.append(r)
    except Exception as err:
      print(err)
    return records
  
  def insert_record(self, sql_query):
    """Changes state"""
    self.__sql_query = sql_query
    # ToDo 
    # validation to check sql_query

    con = self.create_connection()
    cur = con.cursor()
    try:
      cur.execute(sql_query)
      con.commit()
      print('Record added!')
    except Exception as err:
      print(err)
  
      
  def delete_record(self, sql_query):
    """Changes state"""
    self.__sql_query = sql_query

    # ToDo
    # Validate sql_query
    con = self.create_connection()
    cur = con.cursor()
    try:
      cur.execute(self.__sql_query)
      con.commit()
      print('record deleted!')
    except Exception as err:
      print(err)
    cur.close()
    con.close()
  
  def update_record(self,sql_query) -> None:
    self.__sql_query = sql_query

    # ToDo
    # Validate sql_query

    con = self.create_connection()
    cur = con.cursor()
    try:
      cur.execute(self.__sql_query)
      con.commit()
      print('record updated!')
    except Exception as err:
      print(err)
    cur.close()
    con.close()

    
db1 = MySql(
  'localhost',
  'sau',
  'Imgoingin_2021',
  'testdb'
)




# db1.insert_record("INSERT INTO customers VALUES ('saurabh', 'DIZ Area')")
# db1.insert_record("INSERT INTO customers VALUES ('prashant', 'uttam nagar')")
db1.update_record("UPDATE customers SET address='r.k ashram marg' WHERE name='saurabh'")
print(db1.execute_query("select * from customers"))








