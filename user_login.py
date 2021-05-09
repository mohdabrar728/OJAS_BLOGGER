import pymysql
row = ()
dicter = {}
class login():
    def __init__(self, name, password):
        self.username = name
        self.password = password
    def check(self, dicter):
        if self.username in dicter.keys() and self.password == dicter[self.username]:
            return "login successful!!!!.."
        elif self.username in dicter.keys() and self.password != dicter[self.username]:
            return "you entered a wrong password"
        elif self.username not in dicter.keys():
            return "user not exists "

def usercall(x, y):
    conn= pymysql.connect(host="localhost", user="root", passwd="Root@123")
    c = conn.cursor()
    usedb = c.execute('use ojasblog')
    table = c.execute('select username,password from userregistraction')
    row = c.fetchone()
    while row is not None:
        dicter[row[0]] = row[1]
        row = c.fetchone()
    #print(x, y)
    #print(dicter)
    obj = login(x, y)
    temp = obj.check(dicter)
    return temp