import csv
import os
import pandas as pd

fn="c:/python/a1.csv"

def addCust():
    
    f=open(fn, "a")
    cw=csv.writer(f)
    list=[]
    cid=input("Enter your customer id")
    list.append(cid)
    name=input("Enter your name")
    list.append(name)
    contact= input("Enter your contact number:")
    list.append(contact)
    addr=input("Enter Address : ")
    list.append(addr)
    email= input("Enter your email-id:")
    list.append(email)
    city= input("Enter the city where you live")
    list.append(city)
    cw.writerow(list)
    f.close()
    
def searchCustByID():
    f=open(fn, "r")
    nr=csv.DictReader(f)
    flag=0
    cid=input("Enter the customer ID to search : ")
    for row in nr:
        if cid == row["CustId"] :
            print("DETAILS FOUND , Given Below ::: ")
            print("Customer ID : ",row["CustId"])
            print("Customer Name : ",row["CustName"])
            flag=1
            break

    if flag==0 :
        print("No such Customer ID ")
        print("Do you want to register yourself ??")
        choice=input("Y OR N")
        if choice =="N":
            print("okay,Thank You")
        elif choice == "Y":
            addCust()
    f.close()

def searchCustByNumber():
    f=open(fn, "r")
    nr=csv.DictReader(f)
    flag=0
    contact=input("Enter the customer's contact number to search : ")
    for row in nr:
        if contact == row["TelNo"] :
            print("DETAILS FOUND , Given Below ::: ")
            print("Customer's Contact-Number : ",row["TelNo"])
            print("Customer Name : ",row["CustName"])
            print("Customer ID : ",row["CustId"])
            flag=1
            break

    if flag==0 :
        print("No such Contact-Number found ")
    f.close()

def update():
    f=open(fn, "r")
    nr=csv.DictReader(f)
    flag,i=0,0
    cid=input("Enter the customer's customer id : ")
    for row in nr:
        i+=1
        if( cid ==row["CustId"]):
            print("DETAILS FOUND , Given Below ::: ")
            print("Customer's Contact-Number : ",row["TelNo"])
            print("Customer Name : ",row["CustName"])
            print("Customer ID : ",row["CustId"])
            print("Contact Number : ",row["TelNo"])
            print("Address : ",row["Address"])
            print("E-Mail : ",row["E-Mail"])
            print("City : ",row["City"])
            flag=1
            break
    if flag==0 :
        print("No such Customer found ")
            

    if flag==1:
        print("Enter 1 to change contact number: , 2 to change Name: , 3 to change address: , 4 to change email: , 5 to change city: ")
        p=int(input("Enter your choice"))
        if p==0 :
            print("No change needed")
            #break
        elif p==1:
            num=int(input("Enter the new number"))
            f.close()
            df= pd.read_csv(fn)
            print(df)
            df.loc[i-1,"TelNo"]=num
            df.to_csv(fn,index=False)
        elif p==2:
            name1=(input("Enter the new name "))
            f.close()
            df= pd.read_csv(fn)
            print(df)
            df.loc[i-1,"CustName"]=name1
            df.to_csv(fn,index=False)
        elif p==3:
            ad=(input("Enter the new address "))
            f.close()
            df= pd.read_csv(fn)
            print(df)
            df.loc[i-1,"Address"]=ad
            df.to_csv(fn,index=False)
        elif p==4:
            em=(input("Enter the new email "))
            f.close()
            df= pd.read_csv(fn)
            print(df)
            df.loc[i-1,"E-Mail"]=em
            df.to_csv(fn,index=False)
        elif p==5:
            ct=(input("Enter the new name "))
            f.close()
            df= pd.read_csv(fn)
            print(df)
            df.loc[i-1,"City"]=ct
            df.to_csv(fn,index=False)

def delete():
    f=open(fn, "r")
    nr=csv.DictReader(f)
    cid=input("Enter the customer's customer id you want to delete:")
    temp,i=0,0
    for row in nr:
        if cid == row["CustId"]:
            temp= 1
            break
        i += 1

    f.close()
    
    if temp == 0:
        print(" Sorry no such contact found in the directory")
    elif temp==1 :
        #cid=input("Enter customer id : ")
        df= pd.read_csv(fn)
        print(df)
        df=df.drop(i)
        df.to_csv(fn,index=False)
       
def delete_all():
    os.remove(fn)
    print("file removed")
              
        
        
        
    
    

#main
while True :
    print("Enter 1 to input new details :, 2 to search Customer By Customer ID: , 3 to search a Customer By Customer's contact number: ,4 to update a contact, 5 to delete an existing contact: , 6 to delete all")
    ch=int(input("Enter choice : "))
    if ch==0 :
        break
    elif ch==1 :
        addCust()
    elif ch==2:
        searchCustByID()
    elif ch==3:
        searchCustByNumber()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    elif ch==6:
        delete_all()
                
        
        


    
    
    
