# Assignment - 2
# Name - Manas Agarwal
# Roll No - 2020443

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	'''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	ID_FN = []
	for entry in records:
		if entry['first_name'].lower()==first_name.lower() :
			ID_FN.append(entry["id"])
		else:
			continue
			
	return ID_FN
	
#print(filter_by_first_name(read_data_from_file() , "isabella"))

def filter_by_last_name(records, last_name):
	'''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	ID_LN = []
	for entry in records:
		if entry['last_name'].lower()==last_name.lower() :
			ID_LN.append(entry["id"])
		else:
			continue
			
	return ID_LN
#print(filter_by_last_name(read_data_from_file() , 'ramirez'))


def filter_by_full_name(records, full_name):
	'''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	ID_FULLN = []
	for entry in records:
		fulln = str(entry['first_name'].lower()+" "+ entry['last_name'].lower())
		if fulln == full_name.lower() :
			ID_FULLN.append(entry["id"])
		else:
			continue
			
	return ID_FULLN
#print(filter_by_full_name(read_data_from_file() , 'Samesh Nguyen'))


def filter_by_age_range(records, min_age, max_age):
	'''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	ID_AGE = []
	for entry in records:
		if min_age <= entry['age'] and entry['age'] <= max_age:
			ID_AGE.append(entry["id"])
		else:
			continue
			
	return ID_AGE

#print(filter_by_age_range(read_data_from_file(), 40 , 50))

def count_by_gender(records):
	'''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''
	male_no=0
	female_no=0
	for entry in records:
		if entry['gender']=='male':
			male_no += 1
		else:
			female_no += 1
	my_dict = {'male' : male_no , 'female' : female_no}
	return my_dict
#print(count_by_gender(read_data_from_file()))


def filter_by_address(records, address):
	'''
	Description: Filters the person records whose address matches the given address. 

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {} 
				=> All records match this case
			
			Case 2: { "block": "AD", "city": "Delhi" } 
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''
	LST_ADD =[]
	if len(address)==0:
		for entry in records:
			LST_ADD.append({'first_name':entry['first_name'] , 'last_name':entry['last_name']})
	else:
		for i in records:
			matched = True
			for j in address:
				if j=="house_no":
					if address[j]!=i["address"]["house_no"]:
						matched=False
				elif j=="block":
					if address[j].lower()!=i["address"]["block"].lower():
						matched=False
				elif j=="town":
					if address[j].lower()!=i["address"]["town"].lower():
						matched=False
				elif j=="city":
					if address[j].lower()!=i["address"]["city"].lower():
						matched=False
				elif j=="state":
					if address[j].lower()!=i["address"]["state"].lower():
						matched=False
				elif j=="pincode":
					if address[j]!=i["address"]["pincode"]:
						matched=False
			if matched==True:
				LST_ADD.append({'first_name':i['first_name'] , 'last_name':i['last_name']})
	return LST_ADD
#print(filter_by_address(read_data_from_file() , {'house_no' :592}))

	


def find_alumni(records, institute_name):
	'''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''
	LST_AL = []
	for i in records:
		for entry in i['education']:
			if entry["institute"].lower() == institute_name.lower():
				if entry['ongoing']==False:
					LST_AL.append({'first_name':i['first_name'] , 'last_name':i['last_name'] , 'percentage':entry['percentage']})
				else:
					continue
			else:
				continue
	return LST_AL
#print(find_alumni(read_data_from_file() , ""))			
	


def find_topper_of_each_institute(records):
	'''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''
	dict_topper = {}
	dict_final={}
	for entry in records:
		for j in entry['education']:
			if j['ongoing']==False:
				if j['institute'] not in dict_topper:
				
					dict_topper[j['institute']]=[entry['id'], j['percentage']]
				elif j['percentage'] > dict_topper[j['institute']][1]:
					dict_topper[j['institute']]=[entry['id'], j['percentage']]
			else:
				continue
	for i in dict_topper:
		dict_final[i]=dict_topper[i][0]
	return dict_final


#print(find_topper_of_each_institute(read_data_from_file()))




def find_blood_donors(records, receiver_person_id):
	'''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note: 
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''
	dict_donors={}
	for entry in records:
		if entry['id']==receiver_person_id:
			if entry['blood_group']=='A':
				for j in records:
					if j['blood_group']=='A' or j['blood_group']=='O':
						if j['id'] != receiver_person_id:
							dict_donors[j['id']]=j['contacts']
			elif entry['blood_group']=='B':
				for j in records:
					if j['blood_group']=='B' or j['blood_group']=='O':
						if j['id'] != receiver_person_id:
							dict_donors[j['id']]=j['contacts']
			elif entry['blood_group']=='AB':
				for j in records:
					if j['id'] != receiver_person_id:
						dict_donors[j['id']]=j['contacts']
			elif entry['blood_group']=='O':
				for j in records:
					if j['blood_group']=='O':
						if j['id'] != receiver_person_id:
							dict_donors[j['id']]=j['contacts']
	return dict_donors
#print(find_blood_donors(read_data_from_file() , 7))

def get_common_friends(records, list_of_ids):
	'''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''
	lst =[]
	lst1 = []
	for j in range(200):
		lst1.append(j)
	for i in list_of_ids:
		for entry in records:
			
			if entry['id']==i:
				lst = entry['friend_ids']
				lst1 = list(set(lst).intersection(lst1))
			else:
				continue
	return lst1
#print(get_common_friends(read_data_from_file() , [3,4,500]))


def is_related(records, person_id_1, person_id_2):
	'''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
	'''
	if person_id_1==person_id_2:
		return False
	else:
		return True


def delete_by_id(records, person_id):
	'''
	Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	for entry in records:
		if entry['id'] == person_id:
			records.remove(entry)
			for i in records:
				try:
					i['friend_ids'].remove(person_id)
				except:
					continue
		else:
			continue
	return records
#print(delete_by_id(read_data_from_file(), 4))


def add_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	for entry in records:
		if person_id != friend_id:
			if entry['id']==person_id:
				if friend_id not in entry['friend_ids']:
					entry['friend_ids'].append(friend_id)
					entry['friend_ids'].sort()
			elif entry['id']==friend_id:
				if person_id not in entry['friend_ids']:
					entry['friend_ids'].append(person_id)
					entry['friend_ids'].sort()
			else:
				continue
		else:
			continue
	return records
#print(add_friend(read_data_from_file() , 0 , 1))
	


def remove_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	for entry in records:
		if person_id != friend_id:
			if entry['id']==person_id:
				if friend_id in entry['friend_ids']:
					entry['friend_ids'].remove(friend_id)
					
			elif entry['id']==friend_id:
				if person_id in entry['friend_ids']:
					entry['friend_ids'].remove(person_id)
					
			else:
				continue
		else:
			continue
	return records
#print(remove_friend(read_data_from_file() , 0 , 32))


def add_education(records, person_id, institute_name, ongoing, percentage):
	'''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	person_index=None
	for i in range(len(records)):

		if records[i]['id']==person_id:
			person_index=i
			break
	if person_index == None:
		return records
	if ongoing==True:
		records[person_index]["education"].append({"institute":institute_name,"ongoing":ongoing})
	elif ongoing==False:
		records[person_index]["education"].append({"institute":institute_name,"ongoing":ongoing,'percentage':percentage})

	return records

