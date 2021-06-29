import os,mysql.connector as conn
from tabulate import tabulate

username=input("Enter Username : ")
password=input("Enter Password : ")

mydb=conn.connect(host="Your Host Name",user="Your Username",password="Your Password",database="Your Database")
myconn=mydb.cursor()
myconn.execute("SELECT * FROM admin WHERE username='"+username+"' and password='"+password+"'")
admin_data=myconn.fetchone()
if myconn.rowcount==1 :
    print("\n\n===== Welcome, "+admin_data[1]+"=======")
    print("---------------------------\n")
    print("1. Add User\n2. Delete User\n3. See User Result\n4. Add Quiz\n5. Delete Quiz\n")
    first=input("Choose: ")
    if first=='1':
        print("\n===== Add User =======")
        user_name=input("Enter Name: ")
        user_un=input("Enter Username: ")
        user_pass=input("Enter Password: ")
        myconn.execute("INSERT INTO users(name,username,password) VALUES('"+user_name+"','"+user_un+"','"+user_pass+"')")
        mydb.commit()
        print("Inserted")
    elif first=='2':
        print("\n===== Delete User =======")
        user_id=input("Enter User's ID : ")
        myconn.execute("DELETE FROM users WHERE id='"+user_id+"'")
        mydb.commit()
        print("Deleted")
    elif first=='3':
        print("\n============= User Results =============\n")
        myconn.execute("SELECT name,quiz,marks,date_time FROM users,marks WHERE users.id=marks.user_id")
        result=myconn.fetchall()
        print(tabulate(result, headers=["Name","Quiz","Marks","Quiz Time"], tablefmt="pretty"))
    elif first=='4':
        print("\n===== Add Quiz =======")
        quiz_name=input("Enter Quiz Name : ")
        f=open(quiz_name+".json","w")
        x='{"name":"'+quiz_name+'","quiz":[]}'
        f.write(x)
        f.close()
        myconn.execute("INSERT INTO quiz(quiz_name,file) VALUES('"+quiz_name+"','"+quiz_name+".json')")
        mydb.commit()
        print("Inserted") 
    elif first=='5':
        print("\n===== Delete Quiz =======")
        quiz_n=input("Enter Quiz's Name : ")
        os.remove(quiz_n+'.json')
        myconn.execute("DELETE FROM quiz WHERE quiz_name='"+quiz_n+"'")
        mydb.commit()
        print("Deleted")   
    else:
        pass
else:
    print("Wrong Username & Password")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    