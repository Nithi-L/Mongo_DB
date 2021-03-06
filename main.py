!pip install dnspython
!pip install pymongo[srv]

import pymongo
import re

client = pymongo.MongoClient("mongodb+srv://nithimani:3008@cluster0.ac6yo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
records = db.task


name = input("Enter Name :")
ph_no = input("Enter Phone Number :")
mail_id = input("Enter Mail Id :")

def validation():
    boolean = True 
    
    #Name Validation
    if(name[0].islower()):
        print("Name should start with Capital letter")
        boolean =False
    
    #Phone Number Validation 
    if(len(ph_no)!=10):
        print("Phone Number Should contain 10 digits")
        boolean = False
    
    #Email Validation 
    regex = "[A-Za-z0-9]{3,}@[A-Za-z]{3,}[.][A-Za-z]{2,}"
    if (not (re.fullmatch(regex,mail_id))):
        print("Enter Valid EmailId")
        boolean = False
     
    for x in records.find():
        if x["Email Id"] == mail_id:
            print("Email Id already exists")
            boolean = False
    
    return boolean

boolean = validation()

new_dict = {"Name":name, "Phone Number":ph_no, "Email Id":mail_id}

try:
    if boolean:
        records.insert_one(new_dict)
        print("Record inserted successfully")
    else:
        raise Exception("Unable to insert record")
    
except Exception as e:
    print(e)
