#                              u1 has lost laptopbag-FIR,status checking
username1 = "Arun"            #username1 be username of USER   (u1)
password1 = "12345"           #password1 be password of USER  (pwd1)
caseno = "0000"

adminusername = "Admin"       #adminusername be username of ADMIN  (u2)
adminpassword = "6789"        #adminpassword be password of ADMIN (pwd2)

robinfo = '''Arun was walking home back from the office at midnight.
He was on the way to home from the railway station.
Someone took his laptop bag from him and ran away.
 The thief is identified to have 150cm of height.'''
robstatus = "Pending"

s = {'Robbery':367,'Crime':432,'Cyber':212}       # s be criminal list of Thrissur
q = {'Robbery':289,'Crime':398,'Cyber':278}       # s be criminal list of Trivandrum
w = {'Robbery':349,'Crime':299,'Cyber':211}       # s be criminal list of Calicut
e = {'Robbery':97,'Crime':105,'Cyber':199}       # s be criminal list of Wayanad
r = {'Robbery':189,'Crime':172,'Cyber':276}       # s be criminal list of Kottayam


print(" ONLINE CRIME REPORTING SYSTEM  ")
print("")

print(" Choose 1 for user login")
print(" Choose 2 for admin login")
print("")

n = int(input("Choose your option :"))
print(n, "is your choice")   
print("")                         

if (n == 1):
   print("")
   print("-----------WELCOME USER-----------")
   print("")
   u1 = input("Enter username :")
   pwd1 = input("Enterthe password :")
   print("")

   if u1 == username1 and pwd1 == password1:
     print("LOGIN SUCCESSFULLY AS USER")
     print("USER HAS TWO OPTIONS")           #User has got two options  (1)my coplaints (2) register a new complaint
     print("")

     print("Choose A for MY COMPLAINTS")
     print("Chosse B for NEW COMPLAINT")
     print("")

     x = input("Choose A or B : ")

     if x == "A" :                           # if MY COMPLAINTS is selected
  
         print("OPENING MY COMPLAINTS")
         print("")
         print("Choose 1 for CHECKING STATUS")
         print("Choose 2 for CASE INFO")
         print("")
  

         y = int(input("Enter your choice :"))

         if y == 1:
           print(robstatus)
         else:
           print(robinfo)  

     elif x == "B":                        # if NEW COMPLAINT is selected

        print("OPENING NEW COMPLAINT" )
        print("")

        print("Select complaint type")
        print("Choose A for Robbery")
        print("Choose B for Crime")
        print("Choose C for Cyber")
        print("")

        a = input("Choose your complaint type:")
        print("COLLECTING INFORMATION")
        print("")

        if a == "A":
          print("YOUR COMPLAINT TYPE IS ROBBERY")
          print("Please fill the below asked questions")
          print("")
          Name = input("Name of the complainant: ")
          Date = input("Date of incident: ")
          Place = input("Place of incident: ")
          Lost = input("Lost property: ") 
    



        elif a == "B":
          print("YOUR COMPLAINT TYPE IS CRIME") 
          print("") 
          print("Please fill the below asked questions")
          Name = input("Name of the complainant: ")
          Date = input("Date of incident: ")
          Description = input("Give a small decription: ") 
    
    


        elif a == "C":
          print("YOUR COMPLAINT TYPE IS CYBER")  
          print("")
          print("Please fill the below asked questions")
          Name = input("Name of the complainant: ")
          Date = input("Date of incident: ")
          Description = input("Give a small decription: ")
          

   else:
     print("Invalid username and password")
     
                             

    #####ADMIN########



elif (n == 2):
  print("")
  print("-----------WELCOME ADMIN-----------")
  print("")
  u2 = input("Enter username :")
  pwd2 = input("Enterthe password :")
  if u2 == adminusername and pwd2 == adminpassword:
     print("LOGIN SUCCESSFULLY AS ADMIN") 
     print("")

     
     print("Choose A for Status Updation")
     print("Choose B for Criminal list")
     print("Choose C for no. of cases in each section")
     print("")

     x = input("Choose A or B or C :")
     print("")

     if x == "A" :                                     # if STATUS UPDATION is selected
       print("YOU HAVE CHOSEN FOR STATUS UPDATION")
       c = input("ENTER CASE NO: ")                    # C = caseno.
       print("")
       if c == "0000":
         print("You can make the updation here ")
         t = input("Please update:  ")

     elif x == "C":
       print("YOU HAVE CHOSEN FOR NO. OF CASES IN EACH SECTION")
       print("")
       print("CHOOSE THE SECTION")
       print("1 for Robbery")
       print("2 for Crime")
       print("3 for Cyber")
       print("")
       

       b =input("ENTER YOUR SECTION:  ") 
       print("")

       if b == "1":
        c = 0
        for row in myTable:
         row.border = False
         row.header = False
         if row.get_string(fields=["Offense details"]).strip() == "Robbery":
          c += 1

        print('count of robbery :', c)   
       elif b == "2":
        c = 0
        for row in myTable:
         row.border = False
         row.header = False
         if row.get_string(fields=["Offense details"]).strip() == "Crime":
          c += 1

        print('count of crime :', c)
         
       elif b =="3":
        c = 0
        for row in myTable:
         row.border = False
         row.header = False
         if row.get_string(fields=["Offense details"]).strip() == "Cyber":
          c += 1

        print('count of cyber :', c)

       exit
          
               
          
     elif x == "B":                                       # YOU HAVE CHOSEN FOR CRIMINAL LIST
       print("YOU HAVE CHOSEN FOR CRIMINAL LIST")
       from prettytable import PrettyTable                # pip install prettytable
       myTable = PrettyTable(["Sl No", "Name", "Age","Gender", "City Of Residence","Offense details"])
       myTable.add_row(["1", "Murali", "46", "Male","Kochi","Robbery"])
       myTable.add_row(["2", "Raghu", "52", "Male","Trivandrum","Cyber"])
       myTable.add_row(["3", "Deepthi", "40", "Female","Kottayam","Cyber"])
       myTable.add_row(["4", "Babu", "39", "Male","Thrissur","Crime"])
       myTable.add_row(["5", "Sindhu", "48", "Male","Wayanad","Robbery"])
       print(myTable)
       print("")



  
          
 
     else:
       print("Invalid option..") 
       print("TRY AGAIN")
       exit

  else:
    print("Invalid username and password")



