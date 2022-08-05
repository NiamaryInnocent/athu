1	#                              u1 has lost laptopbag-FIR,status checking
2	username1 = "Arun"            #username1 be username of USER   (u1)
3	password1 = "12345"           #password1 be password of USER  (pwd1)
4	caseno = "0000"

5	adminusername = "Admin"       #adminusername be username of ADMIN  (u2)
6	adminpassword = "6789"        #adminpassword be password of ADMIN (pwd2)

7	robinfo = '''Arun was walking home back from the office at midnight.
8	He was on the way to home from the railway station.
9	Someone took his laptop bag from him and ran away.
10	The thief is identified to have 150cm of height.'''
11	robstatus = "Pending"

12	s = {'Robbery':367,'Crime':432,'Cyber':212}       # s be criminal list of Thrissur
13	q = {'Robbery':289,'Crime':398,'Cyber':278}       # s be criminal list of Trivandrum
14	w = {'Robbery':349,'Crime':299,'Cyber':211}       # s be criminal list of Calicut
15	e = {'Robbery':97,'Crime':105,'Cyber':199}       # s be criminal list of Wayanad
16	r = {'Robbery':189,'Crime':172,'Cyber':276}       # s be criminal list of Kottayam
17	

18	print(" ONLINE CRIME REPORTING SYSTEM  ")
19	print("")

20	print(" Choose 1 for user login")
21	print(" Choose 2 for admin login")
22	print("")

23	n = int(input("Choose your option :"))
24	print(n, "is your choice")   
25	print("")                         

26	if (n == 1):
27	print("")
28	print("-----------WELCOME USER-----------")
29	print("")
30	u1 = input("Enter username :")
31	pwd1 = input("Enterthe password :")
32	print("")

33	if u1 == username1 and pwd1 == password1:
34	print("LOGIN SUCCESSFULLY AS USER")
35	print("USER HAS TWO OPTIONS")           #User has got two options  (1)my coplaints (2) register a new complaint
36	print("")

37	print("Choose A for MY COMPLAINTS")
38	print("Chosse B for NEW COMPLAINT")
39	print("")

40	x = input("Choose A or B : ")

41	if x == "A" :                           # if MY COMPLAINTS is selected

42	print("OPENING MY COMPLAINTS")
43	print("")
44	print("Choose 1 for CHECKING STATUS")
45	print("Choose 2 for CASE INFO")
46	print("")


47	y = int(input("Enter your choice :"))

48	if y == 1:
a.	print(robstatus)
49	else:
a.	print(robinfo)  

50	elif x == "B":                        # if NEW COMPLAINT is selected

51	print("OPENING NEW COMPLAINT" )
52	print("")

53	print("Select complaint type")
54	print("Choose A for Robbery")
55	print("Choose B for Crime")
56	print("Choose C for Cyber")
57	print("")

58	a = input("Choose your complaint type:")
59	print("COLLECTING INFORMATION")
60	print("")

61	if a == "A":
62	print("YOUR COMPLAINT TYPE IS ROBBERY")
63	print("Please fill the below asked questions")
64	print("")
65	Name = input("Name of the complainant: ")
66	Date = input("Date of incident: ")
67	Place = input("Place of incident: ")
68	Lost = input("Lost property: ") 

69	


70	elif a == "B":
71	print("YOUR COMPLAINT TYPE IS CRIME") 
72	print("") 
73	print("Please fill the below asked questions")
74	Name = input("Name of the complainant: ")
75	Date = input("Date of incident: ")
76	Description = input("Give a small decription: ") 


77	

78	elif a == "C":
79	print("YOUR COMPLAINT TYPE IS CYBER")  
80	print("")
81	print("Please fill the below asked questions")
82	Name = input("Name of the complainant: ")
83	Date = input("Date of incident: ")
84	Description = input("Give a small decription: ")


85	else:
86	print("Invalid username and password")



87	#####ADMIN########
88	


89	elif (n == 2):
90	print("")
91	print("-----------WELCOME ADMIN-----------")
92	print("")
93	u2 = input("Enter username :")
94	pwd2 = input("Enterthe password :")
95	if u2 == adminusername and pwd2 == adminpassword:
96	print("LOGIN SUCCESSFULLY AS ADMIN") 
97	print("")


98	print("Choose A for Status Updation")
99	print("Choose B for Criminal list")
100	print("Choose C for no. of cases in each section")
101	print("")

102	x = input("Choose A or B or C :")
103	print("")

104	if x == "A" :                                     # if STATUS UPDATION is selected
105	print("YOU HAVE CHOSEN FOR STATUS UPDATION")
106	c = input("ENTER CASE NO: ")                    # C = caseno.
107	print("")
108	if c == "0000":
109	print("You can make the updation here ")
110	t = input("Please update:  ")

111	elif x == "C":
112	print("YOU HAVE CHOSEN FOR NO. OF CASES IN EACH SECTION")
113	print("")
114	print("CHOOSE THE SECTION")
115	print("1 for Robbery")
116	print("2 for Crime")
117	print("3 for Cyber")
118	print("")


119	b =input("ENTER YOUR SECTION:  ") 
120	print("")

121	if b == "1":
122	c = 0
123	for row in myTable:
124	row.border = False
125	row.header = False
126	if row.get_string(fields=["Offense details"]).strip() == "Robbery":
127	c += 1

128	print('count of robbery :', c)   
129	elif b == "2":
130	c = 0
131	for row in myTable:
132	row.border = False
133	row.header = False
134	if row.get_string(fields=["Offense details"]).strip() == "Crime":
135	c += 1

136	print('count of crime :', c)

137	elif b =="3":
138	c = 0
139	for row in myTable:
140	row.border = False
141	row.header = False
142	if row.get_string(fields=["Offense details"]).strip() == "Cyber":
143	c += 1

144	print('count of cyber :', c)

145	exit



146	elif x == "B":                                       # YOU HAVE CHOSEN FOR CRIMINAL LIST
147	print("YOU HAVE CHOSEN FOR CRIMINAL LIST")
148	from prettytable import PrettyTable                # pip install prettytable
149	myTable = PrettyTable(["Sl No", "Name", "Age","Gender", "City Of Residence","Offense details"])
150	myTable.add_row(["1", "Murali", "46", "Male","Kochi","Robbery"])
151	myTable.add_row(["2", "Raghu", "52", "Male","Trivandrum","Cyber"])
152	myTable.add_row(["3", "Deepthi", "40", "Female","Kottayam","Cyber"])
153	myTable.add_row(["4", "Babu", "39", "Male","Thrissur","Crime"])
154	myTable.add_row(["5", "Sindhu", "48", "Male","Wayanad","Robbery"])
155	print(myTable)
156	print("")
157	





158	else:
159	print("Invalid option..") 
160	print("TRY AGAIN")
161	exit

162	else:
163	print("Invalid username and password")

