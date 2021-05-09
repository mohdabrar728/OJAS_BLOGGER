import pymysql

data = pymysql.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="ojasblog",

   )
class AddingBlog:
    def __init__(self, user, title, add_blog):
        self.user = user
        self.title = title
        self.add_blog = add_blog
    def enterField(self):
        try:
            mycursor = data.cursor()
            database = mycursor.execute("create database if not exists blogger")
            useddb = mycursor.execute("use blogger")
            table = mycursor.execute(f"create table if not exists {self.user}(title varchar(255),blog text,primary key(title))")
            insert = mycursor.execute(f'INSERT INTO {self.user}(title, blog) VALUES("{self.title}", "{self.add_blog}")')
            data.commit()
            return 1
        except:
            return 0
class EditBlog:
    def printB(self,user):
        dicter = {}
        mycursor = data.cursor()
        mycursor.execute("use blogger")
        mycursor.execute(f"select * from {user}")
        row = mycursor.fetchone()
        while row is not None:
            dicter[row[0]] = row[1]
            row = mycursor.fetchone()
        return dicter
    def printBlog(self,user):
        dicter = {}
        mycursor = data.cursor()
        mycursor.execute("use blogger")
        mycursor.execute(f"select * from {user}")
        row = mycursor.fetchone()
        while row is not None:
            dicter[row[0]] = row[1]
            row = mycursor.fetchone()
            return
    def editerBlog(self, user,title,blog):
        #print(user,title,blog)
        #try:
        mycursor = data.cursor()
        mycursor.execute("use blogger")
        mainstring = ''
        for i in title:
            if i == "'" or i == '"':
                mainstring += f"\{i}"
            else:
                mainstring += i
        query = r"update {0} set blog='{1}' where title='{2}'".format(user,blog,mainstring)
        #print(query)
        mycursor.execute(query)
        data.commit()
        #return 1
        #except:
        #    return 0

'''
class UserLoginCall():
    def __init__(self, user):
            self.user = user
            print("1 --> Adding a Blog\n2 --> Editing a Blog")
            choice = int(input("Select your choice : "))
            if choice == 1:
                obj = AddingBlog(self.user)
                obj.enterField()
            elif choice == 2:
                obj = EditBlog()
                obj.printBlog(self.user)
'''
def addblogcall(user, title, add_blog):
    print(user, title, add_blog)
    obj = AddingBlog(user, title, add_blog)
    test = obj.enterField()
    return test
'''
def editblogcall(user,title):
    obj = EditBlog()
    temper = obj.printBlog(user,title)
    return temper
'''

'''
user = 'mohdabrar'
title = 'Early  and Risk Analysis of  Diabetes Mellitus Using the Nonlinear Least Absolute Shrinkage and Selection Operator (LASSO) Regression Technique'
add_blog = "Due to its constantly  occurrence, diabetes mellitus is increasingly influencing more and more families. Most diabetics know rarely about their health quality or pre-diagnosis risk factors. Based on this study, we proposed a contemporary model based on Machine Learning techniques for predicting type 2 diabetes mellitus (T2DM) and risk analysis. The key issues we are assessing to overcome are enhancing the prediction model's accuracy and minimize the prediction error. The most aim of this project obtains a subset of predictors reducing prediction that minimizes prediction error for a quantitative response variable. The Least Absolute Shrinkage and Selection Operator (LASSO) do This is by putting a limit on the parameters of the model that causes regression coefficients to shrink to zero for certain variables. Results of the study show that the proposed approach to select the most important characteristics of diabetic data is useful and accurate. This study will help to build a model using the selected features that can predict diabetes using machine learning systems."
addblogcall(user, title, add_blog)
'''