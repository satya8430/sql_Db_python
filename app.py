from flask import Flask, render_template, request
from SQL_DbOperations import SqlDbManagement

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/showdb", methods=['GET','POST'])
def showDatabases():
  sqlOperation = SqlDbManagement(username="root", password="Satya007")
  results = sqlOperation.getListOfDatabases("SHOW DATABASES")
  return render_template('results.html', results = results)

@app.route("/showtable", methods=['GET','POST'])
def showTables():
  sqlOperation = SqlDbManagement(username="root", password="Satya007")
  db = request.form['db']
  results = sqlOperation.getListOfTables("SHOW TABLES", db)
  return render_template('results.html', results = results)

@app.route("/createdb", methods=['GET','POST'])
def createDatabase():
  sqlOperation = SqlDbManagement(username="root", password="Satya007")
  db_name = request.form['db']
  status = False
  status = sqlOperation.createDatabase(db_name)
  if status:
    return render_template('results.html',message = "Database Created")
  else:
    return render_template('results.html',message = "Database Creation Failed")

@app.route("/createtable", methods=['GET','POST'])
def createTable():
  sqlOperation = SqlDbManagement(username="root", password="Satya007")
  db_name = request.form['db']
  columns = request.form['columns']
  table_name = request.form['table']
  status = sqlOperation.createTable(db_name, columns, table_name)
  if status:
    return render_template('results.html',message = "Table Created")
  else:
    return render_template('results.html',message = "Table Creation Failed")
  
@app.route("/select", methods=['GET','POST'])
def selectQuery():
  sqlOperation = SqlDbManagement(username="root", password="Satya007")
  db_name = request.form['db']
  query = request.form['query']
  table_name = request.form['table']
  if query.split(' ')[1] == '*':
    all_columns = sqlOperation.fetchAllColumnsList(db_name, table_name)
  else:
    all_columns = []
    columns_list = [q for q in query.split(' ')[1].split(',')]
    all_columns.append(columns_list)
  results = sqlOperation.selectQuery(db_name, query)
  return render_template('results.html', results=results, all_columns=all_columns)


if __name__ == "__main__":
  app.run()