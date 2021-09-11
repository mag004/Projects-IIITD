# Name - Manas Agarwal
# Roll No - 2020443

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''

from a2 import *
records=read_data_from_file()
print("-"*100)
print("Enter the Value Linked to your desired Function (Integer Only)")
print("-"*100)
print(    "1  -- filter_by_first_name          (Searches the records to find all persons with the given first name (case-insensitive)\n\n"
		  "2  -- filter_by_last_name           (Searches the records to find all persons with the given last name (case-insensitive)\n\n"
		  "3  -- filter_by_full_name           (Searches the records to find all persons with the given full name (case-insensitive)\n\n"
		  "4  -- filter_by_age_range           (Searches the records to find all persons whose age lies in the given age range [min_age, max_age])\n\n"
		  "5  -- count_by_gender               (Counts the number of males and females)\n\n"
		  "6  -- filter_by_address             (Filters the person records whose address matches the given address.)\n\n"
		  "7  -- find_alumni                   (Find all the alumni of the given institute name (case-insensitive).\n\n"
		  "8  -- find_topper_of_each_institute (Find topper of each institute)\n"
		  "9  -- find_blood_donors             (Find all donors who can donate blood to the person with the given receiver ID.)\n\n"
          "10 -- get_common_friends            (Find the common friends of all the people with the given IDs)\n\n"
          "11 -- delete_by_id                  (Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.)\n\n"
          "12 -- add_friend                    (Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.)\n\n"
          "13 -- remove_friend                 ( Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.)\n\n"
          "14 -- add_education                 (Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.)\n\n"
          "15 -- is_related                    (Find all donors who can donate blood to the person with the given receiver ID.)\n\n")
print("-"*100)

while(True):
    n=int(input("Enter the Value Linked to your desired Function (Integer Only) : "))
    if n==-1:
        print("Thank You!!")
        break

    if n==1:
        first_name=input("Enter First Name : ")
        print(filter_by_first_name(records , first_name))
    elif n==2:
        last_name=input("Enter Last Name : ")
        print(filter_by_last_name(records , last_name))
    elif n==3:
        full_name=input("Enter Full Name : ")
        print(filter_by_full_name(records , first_name))
    elif n==4:
        min_age=int(input("Enter the minimum age (inclusive) : "))
        max_age=int(input("Enter the maximum age (inclusive) : "))
        print(filter_by_age_range(records , min_age , max_age))
    elif n==5:
        print(count_by_gender(records))
    elif n==6:
        address = {}
        try:
            address["house_no"]=int(input("Enter House no. (leave blank if not required) :  ")) 
        except:
            address["house_no"]=""
        try:
            address["pincode"]=int(input("Enter Pincode (leave blank if not required) : "))
        except:
            address["pincode"]=""
        address["block"]=input("Enter Block (leave blank if not required) : ")
        address["town"]=input("Enter Town (leave blank if not required) : ")
        address["city"]=input("Enter City  (leave blank if not required) : ")
        address["state"]=input("Enter State  (leave blank if not required) : ")


        if address["house_no"] == "":
            del address["house_no"]
        if address["pincode"] == "":
            del address["pincode"]
        if address["block"] == "":
            del address["block"]
        if address["town"] == "":
            del address["town"]
        if address["city"] == "":
            del address["city"]
        if address["state"] == "":
            del address["state"]
        
        print(filter_by_address(records , address))
    elif n==7:
        institue_name = input("Enter the Name of Institue : ")
        print(find_alumni(records , institue_name))
    elif n==8:
        print(find_topper_of_each_institute(records))
    elif n==9:
        receiver_person_id=int(input("Enter the value of Reciever person ID"))
        print(find_blood_donors(records , receiver_person_id))
    elif n==10:
        lst=[]
        lst=input("Enter the ID's of persons(space separated) whose common friends are to be found : ").split()
        print(get_common_friends(records , lst))
    elif n==11:
        person_id=int(input("Enter the value of person ID , whose record is to be deleted : "))
        print(delete_by_id(records, person_id))
    elif n==12:
        person=int(input("Enter the Value Of person ID : "))
        friend=int(input("Enter the value of friend ID : "))
        print(add_friend(records , person , friend))
    elif n==13:
        persons=int(input("Enter the Value Of person ID : "))
        friends=int(input("Enter the value of friend ID : "))
        print(remove_friend(records , persons , friends))
    elif n==14:
        person_id=int(input("Enter person id (INTEGER) : "))
        institute_name=input("Enter institute name : ")
        ongoing=input("Enter Status of Education (Ongoing), True / False : ")
        if ongoing.lower()=='false':
            ongoing=False
            percentage=float(input("Enter percentage : "))
        elif ongoing=='true':
            ongoing=True
            percentage=None

        print(add_education(records, person_id, institute_name, ongoing, percentage))
    elif n==15:
        person_id_1=int(input("Enter person_id_1 : "))
        person_id_2=int(input("Enter person_id_2 : "))
        print(is_related(records, person_id_1, person_id_2))





# Write the code here for creating an interactive program.