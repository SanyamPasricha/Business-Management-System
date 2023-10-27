def customerid():
    import pickle
    f=open("bills.dat","rb+")
    f1=open("shop.dat","rb+")
    z=pickle.load(f)
    a=pickle.load(f1)
    f1.seek(0)
    while True:
        customerid=int(input("Enter Customer ID: "))
        billno=int(input("Enter Bill No.: "))
        balance=int(input("Enter Balance: "))
        l=z[billno]
        b=[billno,l[0],l[1],l[2],l[3],l[4],l[5],balance]
        a[customerid].append(b)
        print("Do you want to enter more(y/n)")
        choice=str(input("Enter choice: "))
        if choice in ("n","N"):
            break
    pickle.dump(a,f1)
    f.close()
    f1.close()
        
def deletecustomer():
    import pickle
    f1=open("shop.dat","rb+")
    z=pickle.load(f1)
    f1.seek(0)
    while True:
        customerid=int(input("Enter customer ID whose record is to be\
 deleted: "))

        if customerid in z:
            z.pop(customerid)
            print("The Record Has Been Deleted!")
        else:
            print("ID not found")
        print("Do you want to delete more(y/n)")
        choice=str(input("Enter Choice: "))
        if choice in ("n","N"):
            break
    pickle.dump(z,f1)
    f1.close()
def deleterecord():
    import pickle
    f1=open("shop.dat","rb+")
    z=pickle.load(f1)
    f1.seek(0)
    while True:
        customerid=int(input("Enter customer ID whose record is to be\
 deleted: "))
        if customerid in z:
            billno=int(input("Enter bill no.: "))
            for i in z[customerid]:
                if i[0]==billno:
                    z[customerid].remove(i)
        else:
            continue
        n=str(input("Do you want to continue(y/n): "))
        if n in ("y","Y"):
            continue
        else:
            break
    pickle.dump(z,f1)
    f1.close()
                
def totalbalance():
    import pickle
    f1=open("shop.dat","rb+")
    z=pickle.load(f1)
    while True:
        a=int(input("Enter customer ID: "))
        if a in z:
            print(z[a][-1][7])
        choice=input('Do You Want To Exit(y/n)? ')
        if choice in ('Y','y'):
            break
def addcustomer():
    import pickle
    f1=open("shop.dat","rb+")
    f=open("bills.dat","rb+")
    z=pickle.load(f1)
    y=pickle.load(f)
    f1.seek(0)
    while True:
        customerid=int(input("Enter Customer ID: "))
        billno=int(input("Enter Bill No.: "))
        balance=int(input("Enter Balance: "))
        l=y[billno]
        b=[billno,l[0],l[1],l[2],l[3],l[4],l[5],balance]
        z[customerid]=[b]
        print('Customer Added!')
        print("Do you want to enter more(y/n)")
        choice=str(input("Enter Choice: "))
        if choice in ("n","N"):
            break
    pickle.dump(z,f1)
    f.close()
def display_details():
    from tabulate import tabulate
    from datetime import datetime
    import pickle
    f=open('shop.dat','rb')
    data=pickle.load(f)
    while True:
        print('Press 1 to display monthly details of the customer')
        print('Press 2 to display a specific record')
        choice=int(input('Enter your choice : '))
        if choice==1:
            check=True
            while check==True:
                try:
                    c_id=int(input('Enter the customer id : '))
                    check=False
                except:
                    print('Wrong Input')
            if c_id in data:
                if data[c_id]!=[]:
                    l=[]
                    check=True
                    while check==True:
                        try:
                            month1=int(input('Enter the month : '))
                            year1=int(input('Enter the year : '))
                            if (month1 in (1,2,3,4,5,6,7,8,9,10,11,12)
                            and year1>2000 and year1<=datetime.now().year):
                                check=False
                            else:
                                print('Wrong Input')
                                print('Please enter again')
                        except:
                            print('Wrong Input') 
                    for i in data[c_id]:
                        if i[1].month==month1 and i[1].year==year1:
                            buying=''
                            for j in range(len(i[3])):
                                buying=buying+i[4][j]+':'+str(i[5][j])+'kg,'
                            tup=i[:2]+[buying[:-1]]+i[-2:]    
                            l.append(tup)
                    if l!=[]:
                        print('Customer name : ',data[c_id][0][2])
                        print(tabulate(l,headers=['BILL NO.','DATE','SALE',
                                                  'TOTAL','BALANCE']))
                    else:
                        print('No Record available of this month')
                else:
                    print('Record is Empty')
            else:
                print('Customer Details Not Available')
        elif choice==2:
            check=True
            while check==True:
                try:
                    c_id=int(input('Enter the customer id : '))
                    check=False
                except:
                    print('Wrong Input')
            if c_id in data:
                if data[c_id]!=[]:
                    check=True
                    while check==True:
                        try:
                            bill_no=int(input('Enter the bill no. of \
the record : '))
                            check=False
                        except:
                            print('Wrong Input')
                    found=0
                    for i in data[c_id]:
                        if i[0]==bill_no:
                            file=i
                            found=1
                            break
                    if found==1:
                        buying=''
                        for j in range(len(file[3])):
                            buying=buying+file[4][j]+':'+str(file[5][j])+'kg,'
                        rec=file[:2]+[buying[:-1]]+file[-2:]
                        print('CUSTOMER NAME : ',file[2])
                        print(tabulate([rec],headers=['BILL NO.','DATE','SALE',
                                                      'TOTAL','BALANCE']))
                    else:
                        print('Record Not Found')
                else:
                    print('Record Empty')
            else:
                print('Customer details not available')
        else:
            print('Wrong Input')
        while True:
                found=0
                ch=input(('Do you want to exit?(y/n) '))
                if ch in ('y','Y','N','n'):
                    if ch in ('y','Y'):
                        found=1
                    break
                else:
                    print('Wrong Input')
        if found==1:
            break
    f.close()
    

    
    
    
    



    


    
    
    
    
    
    
    
