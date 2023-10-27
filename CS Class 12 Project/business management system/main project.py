import bill_management
import stock_management
import customer_details
import profit
import os
f=open('authentication.txt','r')
data=f.read()
list=data.split()
print('----------------------------------- Sign In ------------------\
------------------')
while True:
    username=input('Enter User Name: ')
    if username==list[0]:
        break
    else:
        print('Invalid User Name')
while True:
    password=input('Enter The Password: ')
    if password==list[1]:
        break
    else:
        print('Incorrect Password!!!')
f.close()
print('*********************** WELCOME TO BUSINESS MANAGEMENT SYSTEM*\
*****************')
print('')
print('--------------------------------------------------------------\
-------------------')
print('')
print('                                  WELCOME',username)
print('')
print('                              WHAT WOULD YOU LIKE TO DO TODAY ')
print('')
while True:
    print('1: Bill Management')
    print('2: Stock Management')
    print('3: Customer Details')
    print('4: Sales and Profit')
    print('5: Change Username/Password')
    print('6: To Quit')
    check=True
    while check==True:
        try:
            choice=int(input('Enter Your Choice : '))
            check=False
        except:
            print('Wrong Input!!!!')
    if choice==1:
        print('1: Generate Bill')
        print('2: Delete A Bill')
        print('3: Display A Bill')
        print('4: Quit To Main Menu')
        while True:
            check=True
            while check==True:
                try:
                    choice1=int(input('Enter Your Choice : '))
                    check=False
                except:
                    print('Wrong Input!!!!')
            if choice1==1:
                bill_management.bill()
            elif choice1==2:
                bill_management.delete()
            elif choice1==3:
                bill_management.display()
            elif choice1==4:
                while True:
                    found=0
                    ch=input('Do You Want To Go To Main Menu?(y/n) ')
                    if ch in ('y','Y','N','n'):
                        if ch in ('y','Y'):
                            found=1
                        break
                    else:
                        print('Wrong Input!!!!')
                if found==1:
                    break
            else:
                print('Wrong Input!!!!')
    elif choice==2:
        print('1: New Stock')
        print('2: Update Stock Details')
        print('3: Check Details Of A Particular Product')
        print('4: Display The Stock List')
        print('5: Add A New Product')
        print('6: Delete A Particular Item')
        print('7: Quit To Main Menu')
        while True:
            check=True
            while check==True:
                try:
                    choice2=int(input('Enter your choice : '))
                    check=False
                except:
                    print('Wrong Input!!!!')
            if choice2==1:
                stock_management.add()
            elif choice2==2:
                stock_management.updation_of_stock()
            elif choice2==3:
                stock_management.specific()
            elif choice2==4:
                stock_management.printtable()
            elif choice2==5:
                stock_management.new_product()
            elif choice2==6:
                stock_management.delete()
            elif choice2==7:
                while True:
                    found=0
                    ch=input('Do You Want To Go To Main Menu?(y/n) ')
                    if ch in ('y','Y','N','n'):
                        if ch in ('y','Y'):
                            found=1
                        break
                    else:
                        print('Wrong Input!!!!')
                if found==1:
                    break
            else:
                print('Wrong Input!!!!')
    elif choice==3:
        print('1: Add Details')
        print('2: Check Balance')
        print('3: Display Details')
        print('4: Add A New Customer')
        print('5: Delete A Record')
        print('6: Delete A Customer')
        print('7: Quit To Main Menu')
        while True:
            check=True
            while check==True:
                try:
                    choice3=int(input('Enter Your Choice : '))
                    check=False
                except:
                    print('Wrong Input!!!!')
            if choice3==1:
                customer_details.customerid()
            elif choice3==2:
                customer_details.totalbalance()
            elif choice3==3:
                customer_details.display_details()
            elif choice3==4:
                customer_details.addcustomer()
            elif choice3==5:
                customer_details.deleterecord()
            elif choice3==6:
                customer_details.deletecustomer()
            elif choice3==7:
                while True:
                    found=0
                    ch=input('Do You Want To Go To Main Menu?(y/n) ')
                    if ch in ('y','Y','N','n'):
                        if ch in ('y','Y'):
                            found=1
                        break
                    else:
                        print('Wrong Input!!!!')
                if found==1:
                    break
            else:
                print('Wrong Input!!!!')
    elif choice==4:
        while True:
            print('1: Display Monthly Sales')
            print('2: Display Monthly Purchases')
            print('3: New Payment')
            print('4: Monthly Profit')
            print('5: Monthly Profit Percentage')
            print('6: Update The Amount Of Any Payment')
            print('7: Check Daily Sale/Payment')
            print('8: Quit To Main Menu')
            check=True
            while check==True:
                try:
                    choice4=int(input('Enter Your Choice : '))
                    check=False
                except:
                    print('Wrong Input!!!!')
            if choice4==1:
                profit.amountpurchased()
            elif choice4==2:
                profit.amountspent()
            elif choice4==3:
                profit.append()
            elif choice4==4:
                profit.profit()
            elif choice4==5:
                profit.profitpercentage()
            elif choice4==6:
                profit.update()
            elif choice4==7:
                profit.display()
            elif choice4==8:
                while True:
                    found=0
                    ch=input('Do You Want To Go To Main Menu?(y/n) ')
                    if ch in ('y','Y','N','n'):
                        if ch in ('y','Y'):
                            found=1
                        break
                    else:
                        print('Wrong Input!!!!')
                if found==1:
                    break
            else:
                print('Wrong Input!!!!')
    elif choice==5:
        while True:
            f1=open('authentication.txt','r')
            data=f1.read()
            list=data.split()
            print('1: Change User Name')
            print('2: Change Password')
            print('3: Quit To Main Menu')
            choice5=input('Enter Your Choice: ')
            if choice5=='1':
                password=input('Enter Your Password: ')
                if password==list[1]:
                    f2=open('change.txt','w')
                    user_name=input('Enter Your New User Name: ')
                    f2.write(user_name+' '+password)
                    f2.close()
                    f1.close()
                    os.remove('authentication.txt')
                    os.rename('change.txt','authentication.txt')
                    print('User Name successfully changed !')
                else:
                    print("Password didn't match")
            elif choice5=='2':
                password=input('Enter Your Password: ')
                if password==list[1]:
                    f2=open('change.txt','w')
                    new_password=input('Enter Your New Password: ')
                    f2.write(list[0]+' '+new_password)
                    f1.close()
                    f2.close()
                    os.remove('authentication.txt')
                    os.rename('change.txt','authentication.txt')
                    print('Password successfully changed')
                else:
                    print("Password didn't match")
            elif choice5=='3':
                while True:
                    found=0
                    ch=input('Do You Want To Go To Main Menu?(y/n) ')
                    if ch in ('y','Y','N','n'):
                        if ch in ('y','Y'):
                            found=1
                        break
                    else:
                        print('Wrong Input!!!!')
                if found==1:
                    break
            else:
                print('Wrong Input!!!!')
    elif choice==6:
        while True:
            flag=0
            ch=input('Do You Really Want To Exit?(y/n) ')
            if ch in ('y','Y','N','n'):
                if ch in ('y','Y'):
                    flag=1
                break
            else:
                print('Wrong Input!!!!')
        if flag==1:
                break
    else:
        print('Wrong Input!!!!')
    
    
        
                
            
