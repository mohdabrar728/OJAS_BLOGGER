import pymysql
dicter = {}
conn = pymysql.connect(host="localhost", user="root", passwd="Root@123")
c = conn.cursor()
usedb = c.execute('use ojasblog')
table = c.execute('select username,password from userregistraction')
row = c.fetchone()
while row is not None:
    dicter[row[0]] = row[1]
    row = c.fetchone()
def recoverpassword(username,otp,update_password,str):
    #print("otp",otp)
    #print('gotp',str)
    if username in dicter:
        #print('username',username)
        #print('update_password',update_password)
        if int(otp) == int(str):
            c.execute(f"update userregistraction set password='{update_password}' where username='{username}'")
            conn.commit()
            return "update successfully"
        else:
            return "please enter correct otp"
    else:
        return "user not exists"
#print(dicter)
def forcall(username,otp,npass,gotp):
    take = recoverpassword(username, otp, npass,gotp)
    return take