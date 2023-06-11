import mysql.connector
from tabulate import tabulate
mydb=mysql.connector.connect(host='localhost',user='root',password='welcome@12345VIVEK')
mycursor=mydb.cursor()

db=input("enter your database name")
sql="create database if not exists %s" % (db,)
mycursor.execute(sql)
print("database created successfully")

mycursor=mydb.cursor()
mycursor.execute("Use "+db)
print("use added successfully")

TN=input("enter name of table")
query="create table if not exists "+TN+" \
(empno int ,\
Name varchar(15) ,\
Job varchar(15),\
BasicSalary int,\
DA float,\
HRA float,\
GrossSalary float,\
Tax float,\
NetSalary float)"
print("table "+TN+" created successfully...")
mycursor.execute(query)
mydb.commit()

while True:
      print("*******************************************************************")
      print('*                PAYROLL MANAGEMENT SYSTEM                        *')
      print('*******************************************************************')
      print(" => MAIN MENU :- ")
      print("-------------------")
      print("1.About payroll management system")
      print("2.Adding employing records")
      print("3.Displaying records of all the employees")
      print("4.Displaying records for particular employee ")
      print("5.Deleting records  of employees")
      print("6.Modification of records")
      print("7.Display records according to job type")
      print("8.Exist")
      
      choice=int(input("enter your choice"))
      if choice==1:
             a=open("payroll.txt","r")
             b=a.read()
             print(b)
        
      if choice ==2:
             ans="y"
             while ans=="y":
                    print("enter employee information")
                    Empno=int(input("enter employee no:"))
                    name=input("enter employee name:")
                    job=input("enter employee job:")
                    basic=float(input("enter basic salary:"))
                    if job.upper( )=="officer":
                           da=basic*0.5
                           hra=basic*0.35
                           tax=basic*0.2
                    elif job.upper( )=="manager":
                           da=basic*0.45
                           hra=basic*0.25
                           tax=basic*0.1
                    else:
                           da=basic*0.2
                           hra=basic*0.15
                           tax=basic*0.05
                    gross=basic + da +hra
                    net=gross-tax
                    rec=(Empno ,name , job ,basic ,da , hra, gross, tax, net)
                    query="insert into "+TN+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    mycursor.execute(query ,rec)

                    mydb.commit()
                    print("                                ")
                    ans=input("Do you want more records ? (y/n):-")
                    
      if choice==3:
             try:
                    query="select * from "+TN
                    mycursor.execute(query)
                    print(tabulate (mycursor , headers =['empno' , 'Name' , 'Job' , 'Basic Salary' , 'DA' , 'HRA' , 'Gross Salary' , 'Tax' , 'Net Salary'] , tablefmt='fancy_grid'))
                    '''myrecords = mycursor.fetchall()
                    for rec in myrecords :
                           print(rec) '''
             except:
                    print("something went wrong ")
      if choice==4:
             ans="y"
             while ans=="y":
                    try:
                           en=input("enter employee no. of the record to be displayed")
                           query ="select * from " +TN+" where empno="+en
                           mycursor.execute(query)
                           print(tabulate (mycursor , headers =['empno' , 'Name' , 'Job' , 'Basic Salary' , 'DA' , 'HRA' , 'Gross Salary' , 'Tax' , 'Net Salary'] , tablefmt='fancy_grid'))
                           myrecord=mycursor.fetchone()
                           c=mycursor.rowcount
                           if c==-1:
                                  print("nothing to display")
                    except:
                           print("something went wrong")
                    ans=input("Do you want more records? (y/n):-")
      if choice==5:
             ans="y"
             while ans=="y":
                    en=input("enter employee no. of the record to be deleted")
                    query ="delete from  "+TN+" where empno="+en
                    mycursor.execute(query)
                    mydb.commit()
                    c=mycursor.rowcount
                    if c>0:
                           print("Deletion done ")
                    else:
                           print("employee no ",en ,"not found")
                    ans=input("Do you want more records? (y/n):-")
                    query="select * from "+TN
                    mycursor.execute(query)
                    print(tabulate (mycursor , headers =['empno' , 'Name' , 'Job' , 'Basic Salary' , 'DA' , 'HRA' , 'Gross Salary' , 'Tax' , 'Net Salary'] , tablefmt='fancy_grid'))
                    '''myrecords = mycursor.fetchall()
                    for rec in myrecords :
                           print(rec) '''
      if choice==6:
             ans="y"
             while ans=="y":
                    try:
                           en=input("enter employee no. of the record to be modified or update ")
                           query ="select * from " +TN+" where empno="+en
                           mycursor.execute(query)
                           myrecord=mycursor.fetchone()
                           c=mycursor.rowcount
                           if c== -1:
                                  print("emp no " +en+ "does not exist")
                           else:
                                  name=myrecord[1]
                                  job=myrecord[2]
                                  basic=myrecord[3]
                                  print("empno       : " , myrecord[0])
                                  print("name        : " , myrecord[1])
                                  print("job         : " , myrecord[2])
                                  print("basic       : " , myrecord[3])
                                  print("da          : " , myrecord[4])
                                  print("hra         : " , myrecord[5])
                                  print("gross       : " , myrecord[6])
                                  print("tax         : " , myrecord[7])
                                  print("net         : " , myrecord[8])
                                  print("                                                           ")
                                  print("type value to modify or update below or just press enter for no change")
                                  x=input("enter name")
                                  if len(x)>0:
                                         name=x
                                  x=input("enter job")
                                  if len(x)>0:
                                         job=x
                                  x=input("enter basic")
                                  if len(x)>0:
                                         basic=float(x)
                                  query="update "+TN+" set name="+" ' "+name+" ' "+" , "+"job="+" ' "+job+" ' "+" , "+"basicsalary="+" ' "+str(basic)+ " ' " "  where empno=" +en
                                  print(query)
                                  mycursor.execute(query)   
                                  mydb.commit()
                                  print("record modified")
                                  query="select * from "+TN
                                  mycursor.execute(query)
                                  print(tabulate (mycursor , headers =['empno' , 'Name' , 'Job' , 'Basic Salary' , 'DA' , 'HRA' , 'Gross Salary' , 'Tax' , 'Net Salary'] , tablefmt='fancy_grid'))
                                  '''myrecords = mycursor.fetchall()
                                  for rec in myrecords :
                                          print(rec) '''
                    except:
                           print("something went wrong")
                    ans=input("Do you want to  more record modified or updated?(y/n):-")
                    
      if choice==7:
             print("1. officer")
             print("2. manager")
             print("3.  clerk")
             ch=int(input("Which Job Type Data's you want to displayed"))
             
             if ch==1:
                    query="select * from "+TN+ " where job='{}' ".format('officer',)
                    mycursor.execute(query)
                    print(tabulate (mycursor , headers =['empno' , 'Name' , 'Job' , 'Basic Salary' , 'DA' , 'HRA' , 'Gross Salary' , 'Tax' , 'Net Salary'] , tablefmt='fancy_grid'))
             if ch==2:
                    query="select * from "+TN+ " where job='{}' ".format('manager',)
                    mycursor.execute(query)
                    print(tabulate (mycursor , headers =['empno' , 'Name' , 'Job' , 'Basic Salary' , 'DA' , 'HRA' , 'Gross Salary' , 'Tax' , 'Net Salary'] , tablefmt='fancy_grid'))
             if ch==3:
                    query="select * from "+TN+ " where job='{}' ".format('clerk',)
                    mycursor.execute(query)
                    print(tabulate (mycursor , headers =['empno' , 'Name' , 'Job' , 'Basic Salary' , 'DA' , 'HRA' , 'Gross Salary' , 'Tax' , 'Net Salary'] , tablefmt='fancy_grid'))
      if choice==8:
             print("                         EXIST                 ")
