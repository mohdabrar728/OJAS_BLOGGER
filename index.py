import eel
import pymysql
eel.init('web')
data = []
@eel.expose
def handleinput(x):
    data.append(x)
    print(x)
    print(data)
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Root@123"
   )
eel.start('admin.html')
mycursor = mydb.cursor()
database = mycursor.execute("create database if not exists sample1")
useddb = mycursor.execute("use sample1")
table = mycursor.execute("create table if not exists Python301(name varchar(30),id int(10))")
dup = mycursor.execute( "SELECT DISTINCT name, id FROM Python301 ORDER BY name")
insert = mycursor.execute(f"INSERT INTO Python301( name, id) VALUES('{data[0]}', '{data[1]}');")
print(dup)
mydb.commit()