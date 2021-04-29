import pymysql
import index
data = index.data
print(data)
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Root@123"
   )
mycursor = mydb.cursor()
database = mycursor.execute("create database if not exists ojasblog")
useddb = mycursor.execute("use ojasblog")
table = mycursor.execute("create table if not exists userreg(email varchar(50),username varchar(25),password varchar(25))")
dup = mycursor.execute( "SELECT DISTINCT name, id FROM userreg ORDER BY email")
insert = mycursor.execute(f"INSERT INTO userreg( email, username,password) VALUES('{data[1]}', '{data[2]},{data[3]}');")
print(dup)
mydb.commit()