import mysql.connector
import datetime
from tabulate import tabulate
def add():
    con=mysql.connector.connect(host="localhost",user="root",
                                password="sanyam",
                                database="confidential")
    cur=con.cursor()
    Q=int(input("Enter the bill no: "))
    P=input("Retailer name: ")
    O=0
    d=int(input("Enter the date: "))
    m=int(input("Enter the month: "))
    y=int(input("Enter the year: "))
    D=datetime.date(y,m,d)
    while True:
        A=int(input("Enter the item_code: "))
        S=float(input("Enter the product quantity: "))
        cur.execute("update stock set quantity=quantity+{} where \
                     item_code={}".format(S,A))   
        con.commit()
        print('Quantity Updated')
        cur.execute("select cost_price from stock where \
                     item_code={}".format(A))
        N=cur.fetchone()
        X=N[0]*S
        O+=X
        choice=input("Do you want to continue (Y/N) ")
        if choice in ["n","N"]:
            break
    cur.execute("insert into purchase values({},'{}','{}',{})\
".format(Q,P,D,O))
    con.commit()
def delete():
    con=mysql.connector.connect(host="localhost",user="root",
                                password="sanyam",
                                database="confidential")
    cur=con.cursor()
    while True:
        A=int(input("Enter the item code: "))
        cur.execute("delete from stock where item_code={}".format(A))
        con.commit()
        print('Record Successfully Deleted')
        D=input("Do you want to delete another product(y/n): ")
        if D in ["N","n"]:
            break
        elif D in ["y","Y"]:
            continue
        else:
            print("wrong input")
            break
def print_table():
    con=mysql.connector.connect(host="localhost",user="root",
                                password="sanyam",
                                database="confidential")
    cur=con.cursor()
    cur.execute("Select * from stock")
    data=cur.fetchall()
    a=["Item Code","Item Name","Quantity","Cost Price","Selling Price",
       "GST"]
    print(tabulate(data,headers=a))
def specific():
    con=mysql.connector.connect(host="localhost",user="root",
                                password="sanyam",
                                database="confidential")
    cur=con.cursor()
    while True:
        P=int(input("Enter the item code: "))
        cur.execute("Select * from stock where item_code={}\
".format(P))
        data=cur.fetchall()
        a=["Item Code","Item Name","Quantity","Cost Price",
           "Selling Price","GST"]
        print(tabulate(data,headers=a))
        choice=input("Do you want details of other products(Y/N): ")
        if choice in ["N","n"]:
            break
        elif choice in ["Y","y"]:
            continue
        else:
            print("Wrong input")
            break
def updation_of_stock():
    print("1. Update cost price")
    print("2. Update selling price")
    print("3. Update GST")
    con=mysql.connector.connect(host="localhost",user="root",
                                password="sanyam",
                                database="confidential")
    cur=con.cursor()
    while True:
        M=int(input("Enter your choice: "))
        N=int(input("Enter the product code of which the details need\
 to be updated: "))
        if M==1:
            A=int(input("Enter the new cost price: "))
            cur.execute("update stock set cost_price={} where \
item_code={}".format(A,N))
            con.commit()
            print('Record Updated')
        elif M==2:
            B=int(input("Enter the new selling price: "))
            cur.execute("update stock set selling_price={} where \
item_code={}".format(B,N))
            con.commit()
            print('Record Updated')
        elif M==3:
            C=int(input("Enter the new GST: "))
            cur.execute("update stock set GST={} where \
item_code={}".format(C,N))
            con.commit()
            print('Record Updated')
        choice=input("Do You Want To Update More Items(y/n)? ")
        if choice in ["N","n"]:
            break
        elif choice in ["Y","y"]:
            continue
        else:
            print("Wrong input")
            break
def new_product():
    while True:
        item_code=int(input("Enter the item_code: "))
        item_name=input("Enter the item_name: ")
        item_quantity=float(input("Enter the product quantity: "))
        cost_price=int(input("Enter the cost_price: "))
        selling_price=int(input("Enter the selling price: "))
        GST=int(input("Enter the GST: "))
        con=mysql.connector.connect(host="localhost",user="root",
                                    password="sanyam",
                                    database="confidential")
        cur=con.cursor()
        cur.execute("insert into stock values({},'{}',{},{},{},{})\
".format(item_code,item_name,item_quantity,cost_price,selling_price,GST))
        con.commit()
        print('Product Added')
        choice=input("Do you want to add more products(Y/N): ")
        if choice in ["N","n"]:
            break
        elif choice in ["Y","y"]:
            continue
        else:
            print("Wrong input")
            break
        
    
    
        
                














