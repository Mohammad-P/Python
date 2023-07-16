import mysql.connector
import re
def user_length_check(string):
    if string==[] or len(string)<= 7:
        Valid=False
        return Valid
    else:
        Valid=True
        return Valid
def user_reg(string,Valid):
    if Valid is True:
        if re.fullmatch((regex_email,string)):
            #print('valid username syntax')
            Flag=True
            return Flag
regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_pass=r"^[A-Za-z@0-9._%+-]"
Valid=False
Flag=False
uname=input('Enter username:')
if not user_length_check(uname):
        uname=input('Enter a username with more than seven digits length:')
else:
   # print('Valid username length')
    Valid=True
if Valid:
    if not re.fullmatch(regex_email,uname):
                uname=input('Enter username as experssion@string.string format:')
    else:
     #   print(' Valid regext')
        Flag=True
if Flag==True:
    pasw=input('Enter the password:')
    if not re.match(regex_pass,pasw):
        pasw=input('Enter password as a combination of numbers and chars:')
else: 
    print ('Invalid username and password') #print('connecting to the mydb')
cnx = mysql.connector.connect(user='root', password='*******', host='0.0.0.0', database='employees')
#print('Connected')
cursor=cnx.cursor()
cursor.execute('INSERT INTO userpass VALUES (%s,%s)',(uname,pasw))
cnx.commit()
# query='SELECT * FROM userpass;'
# cursor.execute(query)
# for (u, p) in cursor:
#     print('username is %s, and password is %s.' %(u, p))
cursor.close()
cnx.close()
