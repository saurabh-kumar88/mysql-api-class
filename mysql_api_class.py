import mysql.connector

class MySql:
  def __init__(self, host, user, password, database) -> None:
      self.__host = host
      self.__user = user
      self.__password = password
      self.__database = database
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
  
  def cursor(self, query) -> tuple:

    if len(query) == 0:
      raise Exception("Invalid query")

    try:
      self.cur.execute(query)
    except Exception as err:
      print(err)
    finally:
      print('query complete')
    return self.cur
  
  def insertData(self, sql_query):
    self.__sql_query = sql_query
    # ToDo 
    # validation to check sql_query

    try:
      self.cur.execute(sql_query)
      self.con.commit()
      print('Record added!')
    except Exception as err:
      print(err)
    finally:
      self.cur.close()
      self.con.close()
      
  def getdata(self, sql_query):
    self.__sql_query = sql_query
    data: list = []
    try:
      self.cur.execute(self.__sql_query)
      for r in self.cur:
        data.append(r)
    except Exception as err:
      print(err)
    finally:
      self.close_db_connection()
    return data

  def delete_data(self, sql_query) -> bool:
    self.__sql_query = sql_query

    # ToDo
    # Validate sql_query

    try:
      self.cur.execute(self.__sql_query)
      self.con.commit()
      print('record deleted!')
    except Exception as err:
      print(err)
    finally:
      return False
    return True
    
  def close_db_connection(self):
    try:
      self.cur.close()
      self.con.close()
    except Exception as err:
      print(err)
    
obj = MySql(
  'localhost',
  'sau',
  'Imgoingin_2021',
  'testdb'
)



# obj.insertData("INSERT INTO customers VALUES('Anikeit', 'Dilshaad garden')")
# db = obj.getdata("show databases;")
# print(db)


rows = obj.cursor("select * from customers;")
for r in rows:
  print(r)

#obj.delete_data("DELETE FROM customers WHERE name = 'Anikeit'")
obj.close_db_connection()



