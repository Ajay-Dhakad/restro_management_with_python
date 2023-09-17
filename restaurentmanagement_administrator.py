#restramanagemet 2 THE AMINISTRATOR
#BY 2529 d4a5a3

import os
import time
from datetime import date as dt



   
                    


def cls():  #TO CLEAR THE SCREEN AFTER EACH TASK
    os.system('cls')
    pass

def delay():        #delay or pause in execution
    time.sleep(1)
      
    pass

def auth_admin():        #TO AUTHENTICATE ADMIN 

   
    
    global auth_token   #token for authentication for login security and making it global mean we can excess it in every function
    loop_auth=1
    #admin authentication
    try:
        with open("admin/admin_authentication.txt","x") as d:       #creating a file automatically 
            pass

    except FileExistsError:     #it prevents an error if file already exist
        pass

    finally:
        cls()
        print("ADMIN AUTHENTICATION".center(100,"-"))
        delay()

    with open("admin/admin_authentication.txt","r") as auth_key:
        auth_key=auth_key.read()

    while(True):

        admin_key = input("\nENTER VERIFICATION KEY  : ").lower() #admins input for verification

        if auth_key==str(admin_key):
            auth_token=True     #authentication token will be true  if it is successfull
        
            cls()
            print("AUTHENTICATION SUCCESSFUL".center(100))
            delay()
            cls()
            return  auth_token

        else:
            if loop_auth==3:
                cls()
                print("TOO MANY INVALID ATTEMPS TRY AFTER SOME TIME".center(100,"-"))
                delay()
                cls()
                
                break;

            else:
                auth_token=False
                cls()
                print(f"AUTHENTICATION FAILED TRY AGAIN  |   ATTEMPS LEFT:{3-loop_auth}".center(100))
                loop_auth+=1
                delay()
            
        

    
#==============================================================================================================


# auth_admin()
# if auth_token==True:
#     pass
       #gives auth_token true or false

#==============================================================================================================

def home():
    global home_choices
    cls()    #MAKING A FUNCTION FOR THE HOMEPAGE
    print("WELCOME TO PY'RESTRO (ADMINISTRATION)".center(100,"-"))
    print("\n1.MODIFY MENU\n\n2.CUSTOMER RECORDS\n\n3.REVENUE\n\n4.MAINTENANCE MODE\n\n5.CHANGE PASSWORD")

    home_choices=input("\n\tENTER CHOICE :")
    return home_choices



# home()

def mod_menu():
   
    while(True):
        cls()

        print("MENU MODIFICATIONS".center(100,"-"))
        
        print("\n\n1.SET DEFAULT MENU\n\n2.NEW MENU\n\n3.BACK TO HOME\n\n")

        menu_choice=input("ENTER CHOICE :")
        cls()
        if menu_choice=="1":
            print("--DEFAULT MENU--\n".center(100))

            default_menu={"burger":90,"pizza":99,"coke":30,"sandwitch":50,"cheeseburger":130,"baked-samosa":20,"water":10}

            for i in default_menu:
                print(f"{i}-{default_menu[i]}rs.\n")

            set_defmenu=input("DO YOU WANT TO SET THIS AS TODAYS MENU YES(Y),NO(N) :").lower()

            if set_defmenu=="y":
                try:
                    with open("admin/def_menu.txt","x") as defmenu_file:
                        pass
                except FileExistsError:
                    pass

                with open("admin/def_menu.txt","w") as defmenu_file:
                    defmenu_file.write("1")
                cls()
                print("CHANGES SAVED SUCCESSFULLY !".center(100))
                delay()
                cls()

            else:
                continue
        
        elif menu_choice=="2":
            new_menu={}

            
            while(True):
                cls()
                print("--NEW MENU--".center(100))
                print("\npress x to exit....\n")
                new_menu_food=input("ENTER FOOD NAME :")
                if (new_menu_food=="x"):
                    break;

                try:
                    new_food_price=int(input("ENTER PRICE :"))

                except ValueError:
                    delay()
                    print("INETGERS ONLY....")
                    break;

                


                new_menu[new_menu_food]=new_food_price
            

            for i in new_menu:
                print(f"{i} - {new_menu[i]}rs.")

            set_new_menu=input("\n\nDO YOU WANT TO SET THIS AS TODAYS MENU YES(Y),NO(N) :").lower()


            if set_new_menu=="y":
                
                try:
                    with open("admin/def_menu.txt","x") as def_menu_file:
                        pass
                except FileExistsError:
                    pass
                
                with open('admin/def_menu.txt','w') as def_menu_file:
                    
                    def_menu_file=def_menu_file.write("0")

                try:
                    with open ("admin/new_menu.txt","x") as new_menu_file:   #making new menu in txt to import in cust_panel
                        pass
                except FileExistsError:
                    pass

                with open ("admin/new_menu.txt","w") as new_menu_file:
                    new_menu=str(new_menu)
                    new_menu_file=new_menu_file.write(new_menu)

                print("CHANGES SUCCESSFULLY SAVED...".center(100))
                delay()

            else:
                pass


        elif menu_choice=="3":
        
            break;    

        else:
            
            
            print("INVALID CHOICE !") 
            delay() 
                
                                                            

                    
#=======================================================================================================      

#defining a function for customer records

def cust_rec():
    while(True):

        cls()
        print("CUSTOMER RECORDS".center(100,"-")) 

        print("\n\n1.TOTAL ORDERS COMPLETED \n\n2.LIST OF VISITED CUSTOMERS\n\n3.BACK TO HOME\n\n") 

        cust_rec_choice=input("ENTER CHOICE :") 

        if cust_rec_choice=="1":
            cls()
            print("--ORDERS COMPLETED--".center(100,"-"))
            
            with open("admin/total_visits.txt","r") as total_visits:
                total_visits=total_visits.read()

            print(f"\n\n>TOTAL NUMBER OF FOOD ORDERS COMPLETED : {total_visits}")

            input("\n\nPRESS ANY KEY TO GO BACK :")


        elif cust_rec_choice=="2":
            cls()
            print("--VISITED CUSTOMERS--".center(100,"-"))

            try:
                with open("admin/customers_name.txt","x") as cust_names:
                    pass
            except FileExistsError:
                    pass

            with open("admin/customers_name.txt","r") as cust_names:
                cust_names=cust_names.readlines()
                indx=1

                print("\n")
                for i in cust_names:
                    i=i.strip()
                    print(f"{indx}.{i}\n")
                    indx+=1
            
            input("\n\nPRESS ANY KEY TO GO BACK :")


        elif cust_rec_choice=="3":
            cls()
            break;




#============================================================================
#making a function for revenue records

def revenue():
    
    

    while(True):
        cls()
        print("REVENUE RECORDS".center(100,"-"))
        print("\n\n1.TODAYS TOTAL EARNINGS\n\n2.INCOME AMOUNTS BY DATE\n\n3.BACK TO HOME\n\n")
        revenue_choice=input("ENTER CHOICE :")

        if revenue_choice=="1":
            cls()
            print("TODAYS EARNING RECORDS".center(100,"-"))
            
            #getting the total earnings of today from file and printing it out to user

            date=dt.today()
            try:
                with open(f"admin/revenue_bydate/{str(date)}.txt","r") as todays_revenue:
                    todays_revenue=todays_revenue.read()
                    print(f"\n\nTOTAL EARNINGS FOR TODAY IS : {str(todays_revenue)}")
                    input("\nENTER TO GO BACK :")
            except FileNotFoundError:
                cls()
                print("\n\n\n")
                print("NO REVENUE RECORDS FOR TODAY".center(100))
                input("\n\nENTER TO GO BACK :")

        elif revenue_choice=="2":
            cls()
            print("GET INCOME STATS BY DATE".center(100,"-"))

            rev_chdate=input("\n\nENTER DAY(01-31) :") 
            rev_chmonth=input("\nENTER MONTH(01-12) :")
            rev_chyear=input("\nENTER YEAR(2023) :")

            try:
                
                transform=f"{int(rev_chyear)}-{int(rev_chmonth)}-{int(rev_chdate)}"
                try:
                    with open(f"admin/revenue_bydate/{transform}.txt") as revby_date:
                        revby_date=revby_date.read()
                        print(f"\nTOTAL REVENUE FOR THE DATE IS : {str(revby_date)}rs")
                        input("\nENTER TO FO BACK :")
                except FileNotFoundError:
                    cls()
                    print(f"NO RECORDS FOUND FOR {transform}".center(100))
                    input("\nENTER TO FO BACK :")
                
            except ValueError:
                print("\nINVALID INPUT, PLEASE ENTER VALID DATA.".center(100))
                input("ENTER TO GO BACK :")


        elif revenue_choice=="3":
            cls()
            break;



def maintanance():
    while(True):
        cls()
        print("MAINTANANCE MODE".center(100,"-"))
        
        #CREATING A FILE THAT TELLS US WHETHER IT IS ON MAINTANANCE OR NOT
        try:
            with open("admin/maintanance.txt","x") as srvrbusy:
                pass
        except FileExistsError:
            pass

        with open("admin/maintanance.txt","r") as srvrbusy:
            srvrbusy=srvrbusy.read()

        if len(str(srvrbusy))==0:
            with open("admin/maintanance.txt","w") as srvrbusy:
                srvrbusy=srvrbusy.write("0")
        else:
            pass
        

        with open("admin/maintanance.txt","r") as srvrbusy: #checking that it is on or not
            srvrbusy=srvrbusy.read()

        if str(srvrbusy)=="0":
        
            maint_choice=input("\n\nPRESS ENTER TO TURN ON MAINTANACE MODE :")


            if maint_choice!="error":

                with open("admin/maintanance.txt","w") as srvrbusy:
                    srvrbusy=srvrbusy.write("1")
                    print("\nMAINTENANCE MODE ENABLED...")
                    input("\nENTER TO GO BACK :")
                    break;
        
    

                    

                    
                    
                    

        elif str(srvrbusy)=="1":

            maint_choice=input("\n\nPRESS ENTER TO TURN OFF MAINTANACE MODE :")

            if maint_choice!="error":

                with open("admin/maintanance.txt","w") as srvrbusy:
                    srvrbusy=srvrbusy.write("0")
                    print("MAINTENANCE MODE DISABLED...")
                    input("\nENTER TO GO BACK :")
                    break;


def change_auth():
    exit=0
    while(True):
        cls()
        if exit==3:
            cls()
            print("TOO MANY ATTEMPS PLEASE TRY AFTER SOME TIME".center(100))
            delay()
            break;
        else:
            pass

        print("CHANGE PASSWORD".center(100,"-"))
        
        with open("admin/admin_authentication.txt","r") as change_auth:
            change_auth=change_auth.read()
        
        print(f"\nATTEMPS LEFT :{3-exit}")

        auth_choice=input("\n\nENTER EXISTING PASSWORD :")

        if (str(change_auth)==str(auth_choice)):

            auth_new=input("\n\n#>ENTER NEW PASSWORD :")
            auth_new_confirm=input("\n#>CONFIRM NEW PASSWORD :")

            if auth_new==auth_new_confirm and len(auth_new_confirm)>0:
                with open("admin/admin_authentication.txt","w")as new_password:
                    new_password.write(auth_new_confirm)
                    cls()
                    print("\nPASSWORD CHANGED SUCCESSFULLY...\n")
                    input("\nENTER TO GO BACK:")
                    break;
            else:
                print("PLEASE MATCH THE PASSWORDS".center(100))
                input("\nENTER TO CONTINUE :")
        else:
            print("WRONG PASSWORD".center(100)) 
            input("\nENTER TO CONTINUE :")  

        exit+=1     


                    



while True:
    if auth_admin():
        while True:
            home()
            if home_choices == "1":
                mod_menu()
            elif home_choices == "2":
                cust_rec()
            elif home_choices == "3":
                revenue()
            elif home_choices == "4":
                maintanance()
            elif home_choices == "5":
                change_auth()
            else:
                print("INVALID CHOICE !")
                delay()

    
    


                






