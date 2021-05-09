import pymysql

class UserRegister:
    def __init__(self,name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
    def register(self):
        #print(self.name, self.email, self.username, self.password)
        try:
            data = pymysql.connect(host="localhost", user="root", passwd="Root@123")
            mycursor = data.cursor()
            mycursor.execute("CREATE DATABASE if not exists ojasblog")
            mycursor.execute("use ojasblog")
            mycursor.execute("CREATE TABLE if not exists userregistraction (name varchar(30), email VARCHAR(100),username VARCHAR(100), password VARCHAR(100),PRIMARY KEY (`username`, `email`))")
            insert = "INSERT INTO userregistraction(name, email,username,password) VALUES(%s,%s,%s,%s)"
            student = [(self.name, self.email, self.username, self.password), ]
            mycursor.executemany(insert, student)
            data.commit()
            return True
        except:
            return False
import re
def urcall(name, email, username, password):
    #print(name, email, username, password)
    chunk = [re.fullmatch(r'^[A-Za-z\s]+$', name),re.fullmatch(r'^[A-Za-z0-9-_]+@[a-zA-z]+.[a-z]+$', email),
           re.fullmatch(r'^[A-Za-z0-9-_]+$', username),re.fullmatch(r'^[\w@-_]+$', password)]
    if all(chunk):
        obj = UserRegister(name, email, username, password)
        temp = obj.register()
        return True
    else:
        lst = ['name', 'email', 'username', 'password']
        lst_chunk = [bool(i) for i in chunk]
        lester = ""
        for j in range(len(lst_chunk)):
            if lst_chunk[j] is False:
                lester += lst[j]+" is not valid "
        return lester