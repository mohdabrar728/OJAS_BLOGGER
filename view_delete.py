import pymysql

data = pymysql.connect(
    host="localhost",
    user="root",
    passwd="Root@123",
)


class Manage_user:
    def view_user(self):
        lst1 = []
        lst2 = []
        dic = {}
        mycursor = data.cursor()
        mycursor.execute('USE blogger')
        mycursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'blogger'")
        for index, table in enumerate([tables[0] for tables in mycursor.fetchall()]):
            lst1.append(index)
            lst2.append(table)
        for i, j in zip(lst1, lst2):
            dic[i + 1] = j
        print(dic)
        return dic


class Selecting_user:
    def __init__(self, user):
        self.user = user

    def enteruser(self):
        dic = {}
        mycursor = data.cursor()
        mycursor.execute('USE blogger')
        print(self.user)
        mycursor.execute(f"select * from {self.user}")
        res = mycursor.fetchall()
        for j in res:
            dic[j[0]] = j[1]
        print(dic)
        data.commit()
        return dic


class Deleting_user:

    def __init__(self, user, title):
        self.user = user
        self.title = title

    def deleteuser(self):
        try:
            dic = {}
            mycursor = data.cursor()
            mycursor.execute('USE blogger')
            mycursor.execute(f"DELETE FROM {self.user} WHERE title = '{self.title}'")
            mycursor.execute(f"select * from {self.user}")
            res = mycursor.fetchall()
            for j in res:
                dic[j[0]] = j[1]
            print(dic)
            data.commit()
            return True
        except:
            return False