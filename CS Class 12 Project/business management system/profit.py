def amountpurchased():
    import mysql.connector
    m=int(input("Enter Month: "))
    o=int(input("Enter Year: "))
    a = mysql.connector.connect(host="localhost",database="confidential",
                                user="root",password="sanyam")
    cur=a.cursor()
    cur.execute("select sum(amount) from sales where month(date)={} and\
                year(date)={}".format(m,o))
    result = cur.fetchone() 
    x=0
    for i in result:
        x=x+i
    print('The total amount received from customers is',x)
def amountspent():   
    import mysql.connector
    m=int(input("Enter Month: "))
    o=int(input("Enter Year: "))
    a = mysql.connector.connect(host="localhost",database="confidential",
                                user="root",password="sanyam")
    cur=a.cursor()
    cur.execute("select sum(amount) from purchase where month(date)={} \
                 and year(date)={}".format(m,o))
    result = cur.fetchone() 
    x=0
    for i in result:
        x=x+i
    print('The total amount purchased is',x)
def profit():
    import mysql.connector
    m=int(input("Enter Month: "))
    o=int(input("Enter Year: "))
    a = mysql.connector.connect(host="localhost",database="confidential",
                                user="root",password="sanyam")
    cur=a.cursor()
    cur.execute("select sum(amount) from sales where month(date)={} and\
                year(date)={}".format(m,o))
    result = cur.fetchone() 
    x=0
    for i in result:
        x=x+i  
    cur.execute("select sum(amount) from purchase where month(date)={}\
                 and year(date)={}".format(m,o))
    result = cur.fetchone() 
    y=0
    for i in result:
        y=y+i
    print("Total Profit is",x-y)
def profitpercentage():
    import mysql.connector
    m=int(input("Enter Month: "))
    o=int(input("Enter Year: "))
    a = mysql.connector.connect(host="localhost",database="confidential",
                                user="root",password="sanyam")
    cur=a.cursor()
    cur.execute("select sum(amount) from sales where month(date)={} and\
                 year(date)={}".format(m,o))
    result = cur.fetchone() 
    x=0
    for i in result:
        x=x+i
    cur.execute("select sum(amount) from purchase where month(date)={}\
                 and year(date)={}".format(m,o))
    result = cur.fetchone() 
    y=0
    for i in result:
        y=y+i
    print("Total Profit is",x-y)
    print("Total Profit Percentage is",((x-y)/y)*100)
def append():
    import mysql.connector
    import pickle
    f=open('shop.dat','rb+')
    data=pickle.load(f)
    f.seek(0)
    c=int(input("Enter customer id: "))
    amount=int(input("Enter amount: "))
    m=int(input("Enter month: "))
    y=int(input("Enter year: "))
    d=int(input("Enter day: "))
    import datetime
    x = datetime.datetime(y, m, d)
    for i in data:
        if i==c:
            data[i][-1][-1]=data[i][-1][-1]-amount
    a = mysql.connector.connect(host="localhost",database="confidential",
                                user="root",password="sanyam")
    cur=a.cursor()
    cur.execute("insert into sales values({},'{}',{})".format(c,x,amount))
    pickle.dump(data,f)
    a.commit()
def update():
    import mysql.connector
    c=int(input("Enter customer id: "))
    a=int(input("Enter amount: "))
    m=int(input("Enter month: "))
    o=int(input("Enter year: "))
    con = mysql.connector.connect(host="localhost",database="confidential",
                                  user="root",password="sanyam")
    cur=con.cursor()
    cur.execute("update sales set amount={} where c_id={}".format(a,c))
    con.commit()
def display():
    from tabulate import tabulate
    import mysql.connector as sql
    import datetime
    con=sql.connect(host="localhost",database="confidential",user="root",
                    password="sanyam")
    cur=con.cursor()
    while True:
        print('Press 1 To check details of payments of a month of a customer')
        print('Press 2 to check daily sale of day')
        check=True
        while check==True:
            try:
                choice=int(input('Enter your choice: '))
                check=False
            except:
                print('Wrong Input')
        if choice==1:
            while True:
                check=True
                while check==True:
                    try:
                        c_id=int(input('Enter the Customer ID : '))
                        check=False
                    except:
                        print('Wrong Input')
                cur.execute('select c_id from sales')
                d=cur.fetchall()
                if (c_id,) in d:
                    check=True
                    while check==True:
                        try:
                            month=int(input('Enter the month : '))
                            year=int(input('Enter the year : '))
                            check=False
                        except:
                            print('Wrong Input')
                    cur.execute('select date,amount from sales where \
                                c_id={} and month(date)={} and \
                                year(date)={}'.format(c_id,month,year))
                    data=cur.fetchall()
                    print('Customer ID:',c_id)
                    print(tabulate(data,headers=['DATE','AMOUNT']))
                else:
                    print('Customer id not available')
                break
        elif choice==2:
            check=True
            while check==True:
                try:
                    day=int(input('Enter the day: '))
                    month=int(input('Enter the month: '))
                    year=int(input('Enter the year: '))
                    check=False
                except:
                    print('Wrong Input')
            date=datetime.date(year,month,day)
            cur.execute("select date,amount from sales where c_id=0 and\
                        date='{}'".format(date))
            data=cur.fetchone()
            print('Date\t','Amount\t')
            for i in data:
                print(i,end='\t')
        else:
            print('Wrong Input')
        while True:
            found=0
            ch=input('Do you want to exit(y/n) ? ')
            if ch in ('y','Y','N','n'):
                if ch in ('y','Y'):
                    found=1
                break
            else:
                print('Wrong Input')
        if found==1:
            break
        
        
        
        
        
    
    
    

        
        
    

    

       

    
    







