import pymysql
row = ()
dicter = {}
class login():
    def __init__(self, name, password):
        self.adminname = name
        self.password = password
    def check(self, dicter):
        if self.adminname in dicter.keys() and self.password == dicter[self.adminname]:
            return "login successful!!!!.."
        elif self.adminname in dicter.keys() and self.password != dicter[self.adminname]:
            return "you entered a wrong password"
        elif self.adminname not in dicter.keys():
            return "admin name not exists "

def admincall(x, y):
    conn= pymysql.connect(host="localhost",user="root",passwd="Root@123")
    c = conn.cursor()
    c.execute('use ojasblog')
    c.execute("create database if not exists ojasblog")
    c.execute("create table if not exists admin(name varchar(50),password varchar(45))")
    #c.execute('insert into admin values(\'admin\',\'admin123\')')
    c.execute('select * from admin')
    row = c.fetchone()
    while row is not None:
        dicter[row[0]] = row[1]
        row = c.fetchone()
    #print(x, y)
    #print(dicter)
    obj = login(x, y)
    temp = obj.check(dicter)
    return temp