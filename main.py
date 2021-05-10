import eel
import pymysql

lister = []
data = pymysql.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database = "ojasblog",
   )

eel.init('web')
#================================================================================================================#
#Admin Login
@eel.expose
def admin(x, y):
    #print(x, y)
    admin_input(x, y)
def admin_input(x, y):
    import admin
    check = admin.admincall(x, y)
    if check == "login successful!!!!..":
        print(check)
        eel.show("admin-manage.html")
    else:
        f = open('web/prompt.html', 'w')
        message = f"""<html>
        <head></head>
        <body><br/><center><H1 style="color:Red">{check}</H1></center</body>
        </html>"""
        f.write(message)
        f.close()
        eel.show("prompt.html")
#================================================================================================================#
#User Login
@eel.expose
def user(userlogin, password):
    global lister
    if userlogin.isalnum():
        lister.append(userlogin)
    user_input(userlogin, password)
def user_input(userlogin, password):
    print(userlogin,password)
    import user_login
    check = user_login.usercall(userlogin, password)
    if check == "login successful!!!!..":
        print(check)
        eel.show("adding-blog.html")
    else:
        f = open('web/prompt.html', 'w')
        message = f"""<html>
        <head></head>
        <body><br/><center><H1 style="color:Red">{check}</H1></center</body>
        </html>"""
        f.write(message)
        f.close()
        eel.show("prompt.html")
#================================================================================================================#
#Forgor pass
@eel.expose
def fpass(userlogin,otp, password):
    forgot_input(userlogin,otp, password)
def genotp():
    import random
    import math
    digits = '0123456789'
    OTP = ''
    length = len(digits)
    for i in range(6):
        OTP = OTP + digits[math.floor(random.random() * length)]
    return OTP
gotp = genotp()
print(gotp)
def forgot_input(userlogin,otp, password):
    import forgot_pass
    check = forgot_pass.forcall(userlogin, otp, password,gotp)
    if check == "update successfully":
        print(check)
        eel.show("user-login.html")
    else:
        f = open('web/prompt.html', 'w')
        message = f"""<html>
        <head></head>
        <body><br/><center><H1 style="color:Red">{check}</H1></center</body>
        </html>"""
        f.write(message)
        f.close()
        eel.show("prompt.html")
#================================================================================================================#
#User Registraction
@eel.expose
def userRegistration(w, x, y, z):
    print(w, x, y, z)
    ur_input(w, x, y, z)
def ur_input(w, x, y, z):
    import user_registration
    urchecck = user_registration.urcall(w, x, y, z)
    if urchecck == True:
        print("Register successful!!!!..")
        eel.show("user-login.html")
    else:
        f = open('web/prompt.html', 'w')
        message = f"""<html>
        <head></head>
        <body><br/><center><H1 style="color:Red">{urchecck}</H1></center</body>
        </html>"""
        f.write(message)
        f.close()
        eel.show("prompt.html")

#================================================================================================================#
#Adding a blog
@eel.expose
def addblog(title, add_blog):
    print(title, add_blog)
    addblog_input(title, add_blog)
@eel.expose
def addblogdetails():
    c = data.cursor()
    c.execute('select name,username,email from userregistraction')
    row = c.fetchall()
    for i in row:
        if lister[-1] in i:
            return list(i)
def addblog_input(title, add_blog):
    adduser = lister[-1]
    import adding_blog
    check = adding_blog.addblogcall(adduser, title, add_blog)
    print(check)
    if check == True:
        f = open('web/prompt.html', 'w')
        message = f"""<html>
                <head></head>
                <body><br/><center><H1 style="color:Green">blog added, Successfully</H1></center</body>
                </html>"""
        f.write(message)
        f.close()
        eel.show("prompt.html")
    else:
        f = open('web/prompt.html', 'w')
        message = f"""<html>
        <head></head>
        <body><br/><center><H1 style="color:Red">blog not added,title already exists or 'single quotes and double quotes are not allowed'</H1></center</body>
        </html>"""
        f.write(message)
        f.close()
        eel.show("prompt.html")

#================================================================================================================#
twister = {}
#view blog
@eel.expose
def viewtb(x):
    global twister
    twister={}
    print(x)
    tester1 = checktb(x)
    print(tester1)
    return tester1

# @eel.expose
# def viewtb1():
#     print("inner",twister)
#     return twister

def checktb(x):
    from adding_blog import EditBlog
    obj = EditBlog()
    checktab = obj.printB(lister[-1])
    print(checktab)
    for key,value in checktab.items():
        print(key)
        print(x)
        if key.lower() == x.lower():
            print(key,value)
            twister[key.title()]=value
            return twister
#================================================================================================================#
#list_of_blog
@eel.expose
def listblog():
    testview = listerblog()
    keyslist = []
    for i in testview.keys():
        keyslist.append(i.title())
    print(keyslist)
    return keyslist
def listerblog():
    import adding_blog
    print(lister[-1])
    sendblog = adding_blog.EditBlog().printB(lister[-1])
    return sendblog
#================================================================================================================#
#Edit blog
@eel.expose
def tcame(title):
    global twister
    twister = {}
    print(title)
    tester1 = edit_input(title)
    print(tester1)
    return tester1
def edit_input(title):
    from adding_blog import EditBlog
    obj = EditBlog()
    checkta = obj.printB(lister[-1])
    print(checkta)
    for key,value in checkta.items():
        print(key)
        print(title)
        if key.lower() == title.lower():
            print(key,value)
            twister[key.title()]=value
            return twister
@eel.expose
def edit_update(title, add_blog):
    #print(title,add_blog)
    adduser = lister[-1]
    import adding_blog
    check = adding_blog.EditBlog().editerBlog(adduser, title.lower(), add_blog)
    if check == True:
        f = open('web/prompt.html', 'w')
        message = f"""<html>
                        <head></head>
                        <body><br/><center><H1 style="color:Green">blog updated, Successfully</H1></center</body>
                        </html>"""
        f.write(message)
        f.close()
        eel.show("prompt.html")
    else:
        f = open('web/prompt.html', 'w')
        message = f"""<html>
                        <head></head>
                        <body><br/><center><H1 style="color:Red">blog not updated, title can't be updated and single and double quotes are not allowed</H1></center</body>
                        </html>"""
        f.write(message)
        f.close()
        eel.show("prompt.html")
#================================================================================================================#
# View and Delete
@eel.expose
def viewuser():
    import view_delete
    userview = view_delete.Manage_user().view_user()
    return userview

@eel.expose
def selectuser(user):
    import view_delete
    userselect = view_delete.Selecting_user(user).enteruser()
    return userselect

@eel.expose
def deleteuser(user,title):
    import view_delete
    userdelete = view_delete.Deleting_user(user,title).deleteuser()
    print(userdelete)
    if userdelete == True:
        f = open('web/prompt.html', 'w')
        message = f"""<html>
                                <head></head>
                                <body><br/><center><H1 style="color:Green">Successfully, Deleted Blog</H1></center</body>
                                </html>"""
        f.write(message)
        f.close()
        eel.show("prompt.html")
    else:
        f = open('web/prompt.html', 'w')
        message = f"""<html>
                                <head></head>
                                <body><br/><center><H1 style="color:Red">blog not delect there may user or title not exists</H1></center</body>
                                </html>"""
        f.write(message)
        f.close()
        eel.show("prompt.html")


eel.start('index.html')
