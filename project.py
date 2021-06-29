import requests,json,mysql.connector as conn
from tabulate import tabulate

marks=0
username=input("Enter Username : ")
password=input("Enter Password : ")

mydb=conn.connect(host="Your Host Name",user="Your Username",password="Your Password",database="Your Database")
myconn=mydb.cursor()

myconn.execute("SELECT * FROM quiz")
all_quiz = myconn.fetchall()

myconn.execute("SELECT * FROM users WHERE username='"+username+"' and password='"+password+"'")
user_data = myconn.fetchone()


if myconn.rowcount==1 :
    print("===== Welcome, "+user_data[1]+"=======\n")
    print("1. Start Quiz\n2. See Results")
    first=input("Choose: ")
    if first=='1':
        print("\n==== Select Your Quiz ====\n")
        for x in range(len(all_quiz)):
            print(str(x+1)+". "+all_quiz[x][1]+"")
        quiz_n=input("Enter Your Choice (Quiz Name):")
        
        r=requests.get("http://your_domain/"+quiz_n+".json")
        b=r.json()
        for i in range(len(b["quiz"])) :
            print("\n")
            print("Q"+str(i+1)+". "+b["quiz"][i]["name"])
            print("\t1."+b["quiz"][i]["1"])
            print("\t2."+b["quiz"][i]["2"])
            print("\t3."+b["quiz"][i]["3"])       
            print("\t4."+b["quiz"][i]["4"])
            ans=input("Enter Your Choose Answer No.: ")
            if ans==b["quiz"][i]["answer"] :
                print("    Answer is Correct")
                marks=marks+1
            else :
                print("    Answer is Not Correct:")
                total=marks*100/len(b["quiz"])
                print("\nPercenatge is: "+str(total)+"%")
                print("Total Marks is: "+str(marks)+" By "+str(len(b["quiz"]))+"")
                myconn.execute("INSERT INTO marks(quiz,marks,user_id) VALUES('"+b["name"]+"','"+str(marks)+"','"+str(user_data[0])+"')")
                mydb.commit()
    else:
        myconn.execute("SELECT quiz,marks,date_time FROM marks WHERE user_id='"+str(user_data[0])+"'")
        result_data = myconn.fetchall()
        print(tabulate(result_data, headers=["Quiz","Marks","Quiz Time"], tablefmt="pretty")) 
else :
    print("Wrong Username & Password")
  
  
  




























