import mysql.connector as connection

class SqlDbManagement:
    def __init__(self, username, password):
        try:
            self.username = username
            self.password = password
            
            self.host = "localhost"
        except Exception as e:
            raise Exception(f"(__init__): Something went wrong on initiation of SqlDbManagement\n" + str(e))
    
    def getSqlConnection(self):
        try:
            myDb = connection.connect(host=self.host, user=self.username, passwd=self.password, use_pure=True)
            return myDb
        except Exception as e:
            raise Exception(f"(getSqlConnection): problem ocurred when connecting with database\n" + str(e))

    def getListOfDatabases(self, query):
        try:
            myDb = self.getSqlConnection()
            cursor = myDb.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            raise Exception(f"(getFromShowQuery): show databases query failed to exceute query\n" + str(e))
    
    def getListOfTables(self, query, db):
        try:
            myDb = self.getSqlConnection()
            cursor = myDb.cursor()
            cursor.execute("USE " +db)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            raise Exception(f"(getListOfTables): show tables query failed to execute query\n" + str(e))

    def createDatabase(self, db_name):
        try:
            myDb = self.getSqlConnection()
            query = "CREATE DATABASE IF NOT EXISTS " + db_name
            cursor = myDb.cursor()
            cursor.execute(query)
            return True
        except Exception as e:
            raise Exception(f"(createDatabase): failed to create database " + str(db_name) + "\n" + str(e))

    def createTable(self, db_name, columns, table_name):
        try:
            myDb = self.getSqlConnection()
            cursor = myDb.cursor()
            cursor.execute("use " + db_name)
            cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + "(" + columns + ");")
            return True
        except Exception as e:
            raise Exception(f"(createTable): failed to create table " + str(table_name) + "\n" + str(e))
    
    def selectQuery(self, db_name, query):
        try:
            myDb = self.getSqlConnection()
            cursor = myDb.cursor()
            cursor.execute("use " + db_name)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            raise Exception(f"(selectQuery): failed to execute the select query\n" + str(e))

    def fetchAllColumnsList(self, db_name, table_name):
        try:
            myDb = self.getSqlConnection()
            cursor = myDb.cursor()
            cursor.execute("use " + db_name)
            cursor.execute("select column_name from INFORMATION_SCHEMA.COLUMNS where table_name = '" + table_name + "' order by ordinal_position")
            return cursor.fetchall()
        except Exception as e:
            raise Exception(f"(fetchAllColumnsList): failed to fetch all columns\n" + str(e))

    def insertDataIntoTable(self, db_name, table_name, columns, values):
        try:
            myDb = self.getSqlConnection()
            cursor = myDb.cursor()
            cursor.execute("use " + db_name)
            cursor.execute("INSERT INTO "+ table_name + columns + " VALUES("+ values +")")
        except Exception as e:
            raise Exception(f"(insertDataIntoTable): failed to insert data into table\n" + str(e))
