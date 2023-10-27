def bill_no_generator():
    import pickle
    f=open('bill_no.dat','rb+')
    data=pickle.load(f)
    f.seek(0)
    a=data[0]
    data.pop(0)
    pickle.dump(data,f)
    f.close()
    return a
def bill():
    from tabulate import tabulate
    from datetime import date
    import pickle
    import mysql.connector as sql
    con=sql.connect(host='localhost',user='root',password='sanyam',
                    database='confidential')
    cur=con.cursor()
    while True:
        c_name=input('Enter your name : ')
        bill_no=bill_no_generator()
        check=True
        while check==True:
            try:
                gst_no=int(input('Enter your gst no. : '))
                check=False
            except:
                print('Wrong Input')
        l=[]
        while True:
            while True:
                check=True
                while check==True:
                    try:
                        item=int(input('Enter the item code : '))
                        check=False
                    except:
                        print('Wrong Input')
                cur.execute('select item_code from stock')
                items_available=cur.fetchall()
                if (item,) in items_available:
                    break     
                else:
                    print('Item not available')
            check=True
            while check==True:
                try:
                    quantity=float(input('Enter the quantity of the item : '))
                    check=False
                except:
                    print('Wrong Input')
            cur.execute("select quantity from stock where \
                         item_code={}".format(item))
            quantity_available=cur.fetchone()
            if quantity<quantity_available[0]:
                cur.execute("select name,selling_price,gst from stock \
                             where item_code={}".format(item))
                price=cur.fetchone()
                total=quantity*price[1]
                grandtotal=total+total*price[2]/100
                tup=(item,price[0],quantity,price[1],total,price[2],
                     grandtotal)
                l.append(tup)
                cur.execute('update stock set quantity=quantity-{} \
                             where item_code={}'.format(quantity,item))
                con.commit()
            else:
                print('Quantity not in stock!')
                print(quantity_available[0],'units available')
                print('Please enter the details again')
                continue
            while True:
                found=0
                choice=input('Do you want to add more items(y/n) : ')
                if choice in ('y','Y','n','N'):
                    if choice in ('n','N'):
                        found=1
                    break
                else:
                    print('Wrong Input')
            if found==1:
                break
        check=True
        while check==True:
            try:
                discount=int(input('Enter the discount(%) : '))
                check=False
            except:
                print('Wrong Input')
        amount=0
        for i in l:
            amount+=i[-1]
        date=date.today()
        final_total=amount-amount*discount/100
        while True:
            payment=input('Is the payment cash(press n) or credit(press u)? ')
            if payment in ('n','N','u','U'):
                break
            else:
                print('Wrong Input')
    #generating the bill
        h=['ITEM CODE','ITEM NAME','QUANTITY','PRICE','TOTAL','GST',
           'GRAND TOTAL']
        print('------------------------------------------------------\
---------------------------------------------------------')
        print('                                                VIJAY DYES\
')
        print('\n')
        print('        ',date,'                         GST NO.: 12345678\
               BILL NO.: ',bill_no)
        print('\n')
        print('                    CUSTOMER NAME : ',c_name,
              '                            GST NO. : ',gst_no)
        print('\n')
        print(tabulate(l,headers=h))
        print('')
        print('TOTAL AMOUNT : ',amount)
        print('DISCOUNT : ',discount,'%')
        print('GRAND TOTAL : ',final_total)
        print('------------------------------------------------------\
---------------------------------------------------------')
    #storing bill details
        f=open('bills.dat','rb+')
        d=pickle.load(f)
        item_codes=()
        item_names=()
        quantities=()
        for m in l:
            item_codes+=(m[0],)
            item_names+=(m[1],)
            quantities+=(m[2],)
        if d!={}:
            values=list(d.values())
            date_check=values[-1][0]
            if values!=[]:
                if date!=date_check:
                    count=0
                    for i in values:
                        if i[0]==date_check:
                            if i[-1] in ('n','N'):
                                count=count+i[-2]
                    daily_sales=count
                    cur.execute("insert into sales values(000,'{}',{}\
)".format(date_check,daily_sales))
                    con.commit()
        d[bill_no]=[date,c_name,item_codes,item_names,quantities,
                    final_total,payment]
        f.seek(0)
        pickle.dump(d,f)
        f.close()
        while True:
            found=0
            choice=input('Do you want to generate more bills?(y/n) ')
            if choice in ('n','N','Y','y'):
                if choice in ('n','N'):
                    found=1
                break
            else:
                print('Wrong Input')
        if found==1:
            break
                
def delete():
    import pickle
    f=open('bills.dat','rb+')
    d=pickle.load(f)
    f.seek(0)
    while True:
        while True:
            found=0
            check=True
            while check==True:
                try:
                    bill_no=int(input('Enter the bill no. of the bill\
 whose record is to be deleted : '))
                    check=False
                except:
                    print('Wrong Input')
            if bill_no in d:
                break
            else:
                print('Requested bill not available')
                while True:
                    ch=input('Do you want to exit(y/n)? ')
                    if ch in ('y','Y','n','N'):
                        if ch in ('y','Y'):
                            found=1
                        break
                    else:
                        print('Wrong Input')
                if found==1:
                    found=2
                    break
        if found==2:
            break
        del d[bill_no]
        print('Record deleted')
        while True:
            found=0
            choice=input('Do you want to delete more(y/n)? ')
            if choice in ('n','N','y','Y'):
                if choice in ('n','N'): 
                    found=1
                break
            else:
                print('Wrong Input')
        if found==1:
            break
    pickle.dump(d,f)
    f.close()
def display():
    import pickle
    f=open('bills.dat','rb')
    dictionary=pickle.load(f)
    while True:
        check=True
        while check==True:
            try:
                bill_no=int(input('Enter the bill no. of the bill : '))
                check=False
            except:
                print('Wrong Input')
        if bill_no in dictionary:
            record=dictionary[bill_no]
            print('Bill No. : ',bill_no)
            print('Date : ',record[0])
            print('Customer Name : ',record[1])
            print('Sno.\t','Item\t','     Quantity\t')
            for i in range(len(record[2])):
                print(i+1,'\t',record[3][i],'\t',record[4][i],'\t')
            print('Total Amount : ',record[5])
            while True:
                found=0
                choice=input('Do you want to display more bills(y/n) ? ')
                if choice in ('Y','y','n','N'):
                    if choice in('n','N'):
                        found=1
                    break
                else:
                    print('Wrong Input')
            if found==1:
                break
        else:
            print('Bill not available')
            while True:
                found=0
                choice=input('Do you want to exit(y/n) ? ')
                if choice in ('y','Y','N','n'):
                    if choice in ('y','Y'):
                        found=1
                    break
                else:
                    print('Wrong Input')
            if found==1:
                break
    f.close()        








        
                
    
    

    
    
    
            
        
            
            
    
    
    




