#restroMANAGEMENT by /2529-d4a5a3/ customers_side

import os
from datetime import date as dt
import time
from selenium import webdriver
import json

def restro_management():

    date=dt.today()
    
    




    with open("admin/def_menu.txt","r") as menu_confirm:        #this file tells the program to check for menu change
        menu_confirm=menu_confirm.read()
        
        

    menu_list=[]

    if menu_confirm=="1":  #if 1 then set default menu

        menu={"burger":90,"pizza":99,"coke":30,"sandwitch":50,"cheeseburger":130,"baked-samosa":20,"water":10}
    
    elif menu_confirm=="0": #if zero then change menu
        try:
            with open("admin/new_menu.txt","x") as new_menu:
                pass
        except FileExistsError:
            pass
        
        with open("admin/new_menu.txt","r") as new_menu:
            new_menu=new_menu.read()
            new_menu=new_menu.replace("'","\"")
            print(new_menu)
            new_menu=json.loads(new_menu)
            menu=new_menu


    for i in menu:
        menu_list.append(i) 
#----------------------------------------------------------------------------------------------------------- 

    customer_choices=["1","2","3","4"] #this helps in handling or occuring an error on running the prompts on home menu

    order_list_cust=[]
    order_quan_cust=[]      #empty list to take orders


    total_bill=0            #defined to add total bill of all items
    bill_receipt_saving=""

#taking customers inputs for orders
    os.system('cls')
    print(" CHOOSE OPTIONS ".center(100,"-"))
    time.sleep(0.5)
    cust_input=(input("\n1.MENU \n\n2.ORDER FOOD\n\n3.SEE RESTRO RATINGS\n\n4.CONTACT US\n\n\n--ENTER CHOICE : "))
    
    os.system('cls')

    if cust_input not in customer_choices:
        print("PLEASE GIVE VALID INPUTS".center(100))
        time.sleep(1.5)
        os.system('cls')
        restro_management()

    else:
        
#taking action on inputs

        if cust_input=="1":       #customer inputs to perform actions

            indx=1      #for indexing the foods
            print("FOOD ITEMS AVAILABLE\n")
            for food_menu in menu_list:
                                  
                print(f"{indx}.{food_menu}\nprices: {menu[food_menu]}₹\n")
                indx+=1
        

            navhome=(input("--Press Any Key And Hit ENTER For Main Homepage : "))
            navlen=len(navhome)                                                   #length for empty inputs
            os.system('cls')                            #used to clear terminal
            if navlen==0:
                restro_management()
            else:                                                   #managing continuation of code
                restro_management()

        elif cust_input=="2":
                                            #showing menu first then taking orders

            os.system('cls')
            indx=0      #for indexing the foods
            print(f"FOOD ITEMS TO ORDER\n")

            for food_menu in menu_list:
                                  
                print(f"{indx}.{food_menu}\nprices: {menu[food_menu]}₹\n")
                indx+=1

                #ordering food

            for i in menu_list:

                
                order_input=input("\n--ENTER FOOD NAME CORRECTLY(exit=x):").lower()
                

                if order_input=="x" or order_input=="": 
                    os.system('cls')
                    break;     #making an exit point for loop
                elif order_input not in menu_list:
                    os.system('cls')
                    print("--SORRY BUT WE DONT HAVE THAT FOOD TRY SOMETHING ELSE--".center(100))
                    time.sleep(1)
                    break;
                else:
                    order_quantity=int(input("--ENTER QUANTITY(integers) :"))
                    
                
                    

                
                #appending the parameters to the lists

                order_list_cust.append(order_input)
                order_quan_cust.append(order_quantity)


                #making bills

                print(f"\nyour cart:{order_quan_cust}") 
            index=0
            for bill in order_list_cust:
                
                bill_receipt=(f"DISH :{bill} x {order_quan_cust[index]}\nPRICE:{menu[bill]} x {order_quan_cust[index]}={menu[bill]*order_quan_cust[index]}")
                bill_receipt_saving=bill_receipt_saving+str(bill_receipt+"\n")       #save bill as string to save in db  

                total_bill=total_bill+(menu[bill]*order_quan_cust[index])
                
                index=index+1
            
            if str(total_bill)=="0":
                
                os.system('cls')
                time.sleep(2)
                print("#NOT A ITEM OR QUANTITY TO PROCEED FURTHER !".center(100))
                time.sleep(2)
                os.system('cls')
                restro_management()
            else:
                print(bill_receipt_saving)
                print(f"TOTAL AMOUNT TO BE PAID : {total_bill}₹ ") #if order value is 0 then back to home
            

            #
            


                #confirming order ---------------------------------------

                confirming_order=(input("PRESS 1 TO CONFIRM ORDER AND 0 TO CANCEL :"))

                #taking user-info
                os.system("cls")

                if confirming_order=="1" or confirming_order=="":
                
                #MAKING A MECHANISM THAT SAVES TOTAL BILLS 
                    try:
                        with open(f"admin/revenue_bydate/{str(date)}.txt","x"):
                            pass
                    except FileExistsError:
                        pass

                    with open(f"admin/revenue_bydate/{str(date)}.txt","r") as revenue_read:
                        revenue_read=revenue_read.read()
                        revenue_read=str(revenue_read)

                    if len(revenue_read)==0:    #TO ASSIGN A DEFAULT VALUE IF IT IS EMPTY
                        with open(f"admin/revenue_bydate/{str(date)}.txt","w") as def_revenueval:
                            def_revenueval.write("0")
                    else:
                        pass

                    with open(f"admin/revenue_bydate/{str(date)}.txt", "r") as revenue_read2:
                        revenue_read2=revenue_read2.read()
                    
                    with open(f"admin/revenue_bydate/{str(date)}.txt", "w") as revenue_add:
                        total_rev=int(total_bill)+int(revenue_read2) #TOTAL REVENUE WRITING IN FILE
                        total_rev=str(total_rev)
                        revenue_add.write(total_rev)







                #--------------------------------------------------------------------------------------------------

                    try:
                        with open("admin/total_visits.txt","x") as tot_visits:
                            pass
                            
                    except FileExistsError:
                        pass

                    with open("admin/total_visits.txt","r") as tot_visits:
                        tot_visits=tot_visits.read()
                        tot_visits=int(tot_visits)+1
                        
                    with open("admin/total_visits.txt","w") as visits_add:
                        visits_add.write(str(tot_visits))



                    cust_name=input("-PLEASE FILL THE DETAILS TO CONFIRM-\nENTER YOUR NAME :").capitalize()

                #saving customers name in a list of txt
                    try:
                        with open("admin/customers_name.txt","x") as cust_name_saving:
                            pass
                    except FileExistsError:
                        pass

                    with open("admin/customers_name.txt","a") as cust_name_saving:
                        cust_name_saving.writelines(f"{cust_name}\n")



                    cust_address=input("\nPLEASE ENTER DELIEVERY ADDRESS :").capitalize()
                    os.system('cls')
                    print(f"----ONE THE WAY----".center(100))
                    time.sleep(2)
                    print(f"{cust_name},Your Order Willbe Delievered To {cust_address} Instantly...".center(100))
                    time.sleep(3)
                    os.system('cls')

                #collecting ratings

                    cust_rating_inp=int(input("RATE OUR SERVICES YES(1),NO(0) :"))
                
                    if cust_rating_inp==1:

                        rating_value=int(input("PLEASE RATE US OUT OF 5 :"))
                        os.system('cls')

                                #taking invalid input errors out of way

                        if rating_value<1 or rating_value>5:
                            os.system('cls')
                            print("INVALID RATINGS.COME AGAIN LATER...")
                            os.system('cls')
                            time.sleep(1)
                            restro_management()

                        elif rating_value>=1 or rating_value>=5:
                            print(f"\nYOU VOTED {rating_value} OUT OF 5\n\n".center(100))

                            time.sleep(1.2)

                            print("THANKS COME AGAIN LATER...".center(100))

                        #reading the existing count and adding new ratings in it
                        

                            with open(f"totalratings/total_ratings.txt","r") as a:
                                totalrat_txt=int(a.read())
                            
                            
                            with open(f"totalratings/total_ratings.txt","w") as b:
                                b.write(f"{rating_value+totalrat_txt}")
                                                             #creating database file
                           

                        #storing customer cout who did feedback to txt as database
                        
                            with open(f"usercountratings/usercountratings.txt","r") as c:
                                totalusercount_txt=int(c.read())
                           
                            with open(f"usercountratings/usercountratings.txt","w") as e:
                                e.write(f"{totalusercount_txt+1}")

                            backhome=(input("\nPRESS ENTER TO GO BACK TO HOME :"))
                            os.system('cls')

                            if backhome=="" or backhome=="0":
                                restro_management()
                            else:
                                print("PLEASE PROVIDE VALID VALUES")
                                time.sleep(2)

                                os.system('cls')

                
                                restro_management
                    else:
                        os.system('cls')
                        print("--------THANKS FOR VISITING COME AGAIN LATER---------".center(100))
                        time.sleep(2)
                        os.system('cls')
                        restro_management()


                elif confirming_order=="0":
                    os.system('cls')
                    print("ORDER CANCELLED SUCCESSFULLY...".center(100))
                    time.sleep(2)
                    os.system('cls')
                    restro_management()

                else:
                    os.system('cls')
                    print("INVALID INPUT RECEIVED TRY AGAIN !".center(100))
                    time.sleep(2)
                    os.system('cls')
                    restro_management()
        #NOW WE ARE SHOWING THE RATINGS THAT THIS RESTRO HAVE WITH NUMBER OF CUSTOMERS WHO RATED...


        elif cust_input=="3":
            #storing total ratings in a variable
            with open("totalratings/total_ratings.txt","r") as sr:
                tot_rating=int(sr.read())

                #storing number of customers who rated

            with open("usercountratings/usercountratings.txt","r") as uc:
                tot_users=int(uc.read())

                #NOW SHOWING AVERAGE RATINGS FROM ALL USERS
            os.system('cls')
            average_ratings=tot_rating/tot_users
            print(f"RATING : {average_ratings:.1f} OUT OF 5.".center(100))
            print(f"RATED BY OUR {tot_users} TRUSTED CUSTOMERS".center(100))

            rating2home=input("\n\nHIT ENTER TO GO BACK TO HOME :")

            if rating2home=="":
                os.system('cls')
                restro_management()
            else:
                os.system('cls')
                restro_management()


        #now we are creating a page thru which a person can contact the administrator 

        elif cust_input=="4":
            os.system('cls')   
            print("IF YOU HAVE ANY QUERRY ABOUT OUR SERVICES FEEL FREE TO CONTACT US:".center(110)) 

            contact_input=(input("\n#1)CONTACT US ON MAIL(1)\n\n#2)CONTACT US ON WHATSAPP(2)\n\n--ENTER CHOICE :"))       
            
            #now we are providing the contacts on user inputs by using some web  automation\

            if contact_input=="1" or contact_input=="":
                options=webdriver.ChromeOptions()
                options.add_experimental_option("detach",True)
                cont_medium=webdriver.Chrome(options=options)
                cont_medium.get("mailto:adhakad036@gmai.coml?subject=PYRESTRO_customer")
                time.sleep(2)
                cont_medium.quit()
                os.system('cls')
                print(" THANKS FOR CONTACTING US WE'LL RESOLVE ISSUES ASAP ! ".center(100,"-"))
                
                    #taking customer back 2 hOme

                cont2home=input("\n\nENTER ANY KEY TO GO BACK HOMEPAGE :")
                if cont2home!="error":
                    restro_management()

            elif contact_input=="2":
                options=webdriver.ChromeOptions()
                options.add_experimental_option("detach",True)
                cont_medium=webdriver.Chrome(options=options)
                cont_medium.get("https://wa.me/916562236906")
                time.sleep(2)
                cont_medium.quit()
                os.system('cls')
                print(" THANKS FOR CONTACTING US WE'LL RESOLVE ISSUES ASAP ! ".center(100,"-"))

            else:
                os.system('cls')

                print("SOMETHING WENT WRONG TRY AGAIN".center(100))
                time.sleep(2)
                os.system('cls')
                restro_management()
                
#===============================================================================================================


                                            #GREETINGS

def greeting():
    
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
    

        os.system('cls')
        print(" HELLO,".center(100,"-"))
        time.sleep(1)
        os.system('cls')
        print("  WELCOME TO PY-RESTRO !  ".center(100,"-"))
        time.sleep(1)
        os.system('cls')         
        restro_management()

    else:
        os.system('cls')
        print("\n\n\n")
        print("THE SYSTEM IS IN MAINTENANCE PLEASE TRY AFTER SOME TIME".center(100,"-"))
        time.sleep(3)
        os.system('cls')

        


#===================================================================================================================       
                            
greeting()

                         

                        



                   
            

            
            # restro_management()
         




