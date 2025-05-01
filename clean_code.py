import mysql.connector
import os
import random
db_config = {
    "host": "localhost",
    "user": "root",  
    "password": "",  
    "database": "Questions"
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()
print("-----CLEANCODE-----") 
while True:
    print("****************")
    print("Press 1 to Login")
    print("Press 2 to Register")
    print("Press 3 to exit")
    print("****************")
    try:
        choice=int(input())
        if choice==3:   
            break
        elif choice==2:
            name=input("Enter name:\n")
            password=input("Enter password:\n")
            confirmpass=input("confirm password\n")
            if password==confirmpass:
                name=name+str(random.randint(1,1000))
                print(f"Username set to {name}")
                cursor.execute("Insert into users(username,passwords) values(%s,%s)",(name,password))
                cursor.execute(f"Create table if not exists {name}(qno varchar(250),attempted_ans LONGBLOB,status varchar(250))")
                print("****************")
                print("user registered")
                print("****************")
                break
            else:
                print("****************")
                print("Password does not match")
        elif choice==1:
            name=input("Enter Username\n")
            cursor.execute("Select * from users where username=%s",(name,))
            data=cursor.fetchone()
            if data:
                name,password=data
                passk=input("Enter Password\n")
                if passk==password:
                    print("****************")
                    print("login successful")
                    print("****************")
                    break
            else:
                print("****************")
                print("Password or username doesnt match")  
    except:
        print("Please put a valid input")
def arg_and_listfunc(i,Qname,pname):
    input("press any key to submit your code\n")
    with open(Qname+".txt", "r") as file:
        methods_code = file.read()
    exec(methods_code,globals())
    cursor.execute("Select Q_testcase,Q_ans from quests where Qno=%s",(i,))
    result=cursor.fetchone()
    Qtest,Qans=result
    Qtest=Qtest.decode("utf-8").split("\n")
    Qans=Qans.decode("Utf-8").split("\n")
    # change testcase remove commas from it passes commas as test case
    anslen=list(map(int, Qans))
    stat="rejected"
    try:
        if i==1 or i==2:
            pointer=0
            flag=1
            for line in Qtest:
                line=line.split("-")
                num=int(line[0])
                int_list=eval(line[1])
                r1=twosum(num,int_list) if i==1 else firstandlast(num,int_list)
                if(r1==anslen[pointer]):
                    pointer+=1
                else:
                    print("testcase failed at",int_list)
                    flag=0
                    break
            if flag:
                print("All testcases passed")
                stat="accepted"
        elif i==3:
            pass
    except(e):
        print(e)
    sql = f"INSERT INTO {pname} (qno, attempted_ans, status) VALUES (%s, %s, %s)"
    cursor.execute(sql, (i, methods_code, stat))
    conn.commit()
    os.remove(Qname+".txt")
    return
def args_as_string(i,Qname,pname):
    input("press any key to submit your code\n")
    with open(Qname+".txt", "r") as file:
        methods_code = file.read()
    exec(methods_code,globals())
    cursor.execute("Select Q_testcase,Q_ans from quests where Qno=%s",(i,))
    result=cursor.fetchone()
    Qtest,Qans=result
    Qtest=Qtest.decode("utf-8").split("\n")
    Qans=Qans.decode("Utf-8").split("\n")
    anslen=list(map(int, Qans))
    stat="rejected"
    try:
        pointer=0
        flag=1
        if i==3:
            for line in Qtest:
                r1=ispalindrome(line)
                if(r1==anslen[pointer]):
                        pointer+=1
                else:
                    print("testcase failed at",line)
                    flag=0
                    break
            if flag:
                    print("All testcases passed")
        else:
            for line in Qtest:
                line=line.split("-")
                r1=isanagaram(line[0],line[1]) if i!=8 else rotate(line[0],line[1])
                if(r1==anslen[pointer]):
                    pointer+=1
                else:
                    print("testcase failed at",line)
                    flag=0
                    break
            if flag:
                    print("All testcases passed")
                    stat="accepted"
    except Exception as e:
        print(e)
    sql = f"INSERT INTO {pname} (qno, attempted_ans, status) VALUES (%s, %s, %s)"
    cursor.execute(sql, (i, methods_code, stat))
    conn.commit()
    os.remove(Qname+".txt")
    return
def listonly(i,Qname,pname):
    input("press any key to submit your code\n")
    with open(Qname+".txt", "r") as file:
        methods_code = file.read()
    exec(methods_code,globals())
    cursor.execute("Select Q_testcase,Q_ans from quests where Qno=%s",(i,))
    result=cursor.fetchone()
    Qtest,Qans=result
    Qtest=Qtest.decode("utf-8").split("\n")
    Qans=Qans.decode("Utf-8").split("\n")
    anslen=list(map(int, Qans))
    stat="rejected"
    if i==7:
        try:
            pointer=0
            flag=1
            qlen=list(map(int,Qtest))
            for q in qlen:
                r1=fibo(q)
                if r1==anslen[pointer]:
                    pointer+=1
                else:
                    print("testcase failed at",q)
                    flag=0
                    break
            if flag:
                print("All testcases passed")
                stat="accepted"  
        except Exception as e:
            print(e)
    else:
        try:
            pointer=0
            flag=1
            for line in Qtest:
                num=eval(line)
                if i==9:
                    r1=finduplicate(num)
                else: 
                    r1=firstmiss(num) if i==5 else smallerafterself(num)
                if(r1==anslen[pointer]):
                        pointer+=1
                else:
                    print("testcase failed at",line)
                    flag=0
                    break
            if flag:
                    print("All testcases passed")
                    stat="accepted"
        except Exception as e:
            print(e)
    sql = f"INSERT INTO {pname} (qno, attempted_ans, status) VALUES (%s, %s, %s)"
    cursor.execute(sql, (i, methods_code, stat))
    conn.commit()
    os.remove(Qname+".txt")
    return 
def selectq(playername):
    while(True):
        print("****************")
        print("0: Press for random question")
        cursor.execute("select Qno,Q_status,Q_name from quests")
        result=cursor.fetchall()
        for r in result:
            print("##############################")
            print(r)
        print("Press 10 to exit")
        print("****************")
        try:
            q1=input("Enter qno\n").strip()
            q1=int(q1)
            if(q1==10):
                break
            if(q1==0):
                q1=random.randint(1,9)
                print("Your are now attempting qno",q1)
            cursor.execute("SELECT Q_name,Q_description FROM quests WHERE Qno=%s",(q1,))
            result = cursor.fetchone()
            Qname,Qdescription=result
            with open(Qname+".txt","w") as file:
                file.write(Qdescription.decode("utf-8"))
            if q1==1 or q1==2:
                arg_and_listfunc(q1,Qname,playername)
            elif q1==3 or q1==4 or q1==8:
                args_as_string(q1,Qname,playername)
            elif q1==5 or q1==6 or q1==7 or q1==9:
                listonly(q1,Qname,playername)
        except Exception as e:
            print(e)
def viewQuestions(name):
    sql=f'select qno,status from {name}'
    cursor.execute(sql)
    rows=cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("You havent attempted any questions")
    try:
        qu=int(input("Enter qno to see last attempted ans/ 0 to exit\n"))
        if qu==0:
            return
        query = f"""SELECT attempted_ans 
        FROM {name}
        WHERE qno = %s 
        ORDER BY attempted_ans DESC
         LIMIT 1
       """  
        cursor.execute(query, (qu,))
        result=cursor.fetchone()
        qu=str(qu)
        if result:
            last_attempt=result[0]
            with open("qno"+qu+"lastattempt"+".txt","w") as file:
                file.write(last_attempt.decode("utf-8"))
    except Exception as e:
        print(e)
def menu(name):
    print("Please write your solution in question txt file itself.")
    print("Please keep in mind the indentation of python code as the txt file doesnt have auto-indent.")
    print("It is recommended that when writing on a new line use tab.")
    print("****************") 
    while True:
        print("Press 1 for questions")
        print("Press 2 to see attempted questions")
        print("Press 3 to exit")
        try:
            choice=int(input("Enter your choice\n"))
            if choice==1:
                selectq(name)
            elif choice==2:
                viewQuestions(name)
            elif choice==3:
                break            
        except Exception as e:
            print(e)
menu(name)   


       
