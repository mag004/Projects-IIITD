'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions. 

- You MUST complete the functions defined below, except the ones that are already defined. 
'''
item_lst=['Tshirt','Trousers','Scarf','Smartphone','iPad','Laptop','Eggs','Chocolate','Juice','Milk']
item_cost=[500,600,250,20000,30000,50000,5,10,100,45]
quantities =[0,0,0,0,0,0,0,0,0,0]

def show_menu():
	'''
	Description: Prints the menu as shown in the PDF
	
	Parameters: No paramters
	
	Returns: No return value
	'''
	print(("=")*50)
	print(" "*20 + "My Bazaar")
	print(("=")*50)
	print("Hello! Welcome to my grocery store!\n"
		  "Following are the products available in the shop\n\n:" )
	print("-"*50)
	print("CODE  |  DESCRIPTION  |  CATEGORY    |  COST  (Rs)")
	print("-"*50)
	print("0     |  Tshirt       |  Apparels    |  500\n"
		  "1     |  Trousers     |  Apparels    |  600\n"
		  "2     |  Scarf        |  Apparels    |  250\n"
		  "3     |  Smartphone   |  Electronics |  20,000\n"
		  "4     |  iPad         |  Electronics |  30,000\n"
		  "5     |  Laptop       |  Electronics |  50,000\n"
		  "6     |  Eggs         |  Eatables    |  5\n"
		  "7     |  Chocolate    |  Eatables    |  10\n"
		  "8     |  Juice        |  Eatables    |  100\n"
		  "9     |  Milk         |  Eatables    |  45\n")
	print("-"*50)
	
	


def get_regular_input():
	'''
	Description: Takes space separated item codes (only integers allowed). 
	Include appropriate print statements to match the output with the 
	screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i. 
	'''
	global quantities
	print("-"*50)
	print("ENTER ITEMS YOU WISH TO BUY ")
	print("-"*50)

	item_codes = []
	item_codes = input("Enter the item codes (space-separated):").split()
	
	for i in range (0,10):
		quantities[i]=(item_codes.count(str(i)))
	return quantities
	


def get_bulk_input():
	'''
	Description: Takes inputs (only integers allowed) from a bulk buyer. 
	For details, refer PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	'''
	global item_lst
	global quantities
	
	print("-"*50)
	print("ENTER ITEM AND QUANTITIES")
	print("-"*50)
	
	
	while(1):
		print("Enter code and quantity (leave blank to stop):")
		code=input()
		if(len(code)>0):
			try:
				code, gg= code.split()
				if int(code)>9 or int(code) <0:
					if int(gg)<0:
						print("Invalid code and quantity. Try again.")
					else:
						print("Invalid code. Try again.")
				elif int(gg)<0:
					print("Invalid quantity. Try again.")
				else:
					print("You added "+gg+" "+item_lst[int(code)])
					quantities[int(code)]+=int(gg)
			except Exception:
				print("Invalid Input. Try Again.")
				continue
		else:
			break
	return quantities
		


	


def print_order_details(quantities):
	'''
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: No return value
	'''
	global item_lst
	global item_cost
	print('-'*50)
	print("ORDER DETAILS")
	print("-"*50)
	cnt=1
	for i in range (10):
		if (quantities[i]!=0):
			print(f"[{cnt}] {item_lst[i]} x {quantities[i]} = Rs {item_cost[i]} * {quantities[i]} = Rs {item_cost[i]*quantities[i]}")
			cnt += 1
		else:
			continue


	


def calculate_category_wise_cost(quantities):
	'''
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: A 3-tuple of integers in the following format: 
	(apparels_cost, electronics_cost, eatables_cost)
	'''
	global item_cost
	global apparels_cost
	global electronics_cost
	global eatables_cost
	print("-"*50)
	print("CATEGORY-WISE COST")
	print("-"*50)
	apparels_cost=0
	electronics_cost=0
	eatables_cost=0
	for i in range(3):
		apparels_cost += (item_cost[i]*quantities[i])
	print(f"Apparels = Rs {apparels_cost}")
	for i in range (3,6):
		electronics_cost += (item_cost[i]*quantities[i])
	print(f"Electronics = Rs {electronics_cost}")
	for i in range (6,10):
		eatables_cost += (item_cost[i]*quantities[i])
	print(f"Eatables = Rs {eatables_cost}")

	return (apparels_cost,electronics_cost,eatables_cost)

	


def get_discount(cost, discount_rate):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the discounted category-wise price, if applicable. 
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	
	Returns: A 3-tuple of integers in the following format: 
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
	'''
	global discounted_apparels_cost
	global discounted_electronics_cost
	global discounted_eatables_cost
	print("-"*50)
	print("DISCOUNTS")
	print("-"*50)
	
	
	
	if apparels_cost >= 2000:
		discounted_apparels_cost=(apparels_cost-get_discount(apparels_cost , 0.1))
		print(f"[APPAREL] Rs {apparels_cost} - Rs {get_discount(apparels_cost , 0.1)} = Rs {discounted_apparels_cost}")
	else:
		discounted_apparels_cost = apparels_cost
	if (electronics_cost >= 25000):
		discounted_electronics_cost=(electronics_cost-get_discount(electronics_cost , 0.1))
		print(f"[ELECTRONICS] Rs {electronics_cost} - Rs {get_discount(electronics_cost, 0.1)} = Rs {discounted_electronics_cost}")
	else:
		discounted_electronics_cost = electronics_cost
	if (int(eatables_cost) >= 500):
		discounted_eatables_cost=(eatables_cost-get_discount(eatables_cost , 0.1))
		print(f"[EATABLES] Rs {eatables_cost} - Rs {get_discount(eatables_cost , 0.1)} = Rs {discounted_eatables_cost}")
	else:
		discounted_eatables_cost = eatables_cost
	print(f"TOTAL DISCOUNT = Rs {(apparels_cost/10)+(electronics_cost/10)+(eatables_cost/10)}")
	print(f"TOTAL COST = Rs {(discounted_eatables_cost + discounted_electronics_cost + discounted_apparels_cost)}")

	return (discounted_apparels_cost , discounted_electronics_cost , discounted_eatables_cost)
	


def get_tax(cost, tax):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the total cost including taxes.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables' 
	
	Returns: A 2-tuple of integers in the following format: 
	(total_cost_including_tax, total_tax)
	'''
	global total_cost_including_tax
	global total_tax
	print("-"*50)
	print("TAX")
	print("-"*50)
	total_tax = (get_tax(discounted_apparels_cost , 0.10) + get_tax(discounted_electronics_cost , 0.15) + get_tax(discounted_eatables_cost , 0.05))

	total_cost_including_tax = (discounted_apparels_cost + discounted_eatables_cost + discounted_electronics_cost + total_tax)

	print(f"[APPAREL] Rs {discounted_apparels_cost} * 0.10 = Rs {get_tax(discounted_apparels_cost , 0.10)}")
	print(f"[ELECTRONICS] Rs {discounted_electronics_cost} * 0.15 = Rs {get_tax(discounted_electronics_cost , 0.15)}")
	print(f"[EATABLES] Rs {discounted_eatables_cost} * 0.05 = Rs {get_tax(discounted_eatables_cost , 0.05)}")

	print(f"TOTAL TAX = Rs {total_tax}")
	print(f"TOTAL COST = Rs {total_cost_including_tax}")
	total_cost_including_tax = (discounted_apparels_cost + discounted_eatables_cost + discounted_electronics_cost + total_tax)
	return (total_cost_including_tax, total_tax)
	


def apply_coupon_code(total_cost_including_tax):
	'''
	Description: Takes the coupon code from the user as input (case-sensitive). 
	For details, refer the PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: The total cost (integer) on which the coupon is to be applied.
	
	Returns: A 2-tuple of integers:
	(total_cost_after_coupon_discount, total_coupon_discount)
	'''
	global total_cost_after_coupon_discount
	global total_coupon_discount
	
	print("-"*50)
	print("COUPON CODE")
	print("-"*50)

	while(1):
		print("Enter coupon code (else leave blank):")
		coupon_code=input()
		if (len(coupon_code)>0):
			try:
				if (coupon_code=='HELLE25'):
					if (total_cost_including_tax >= 25000):
						print(f"[HELLE25] min(5000, Rs {total_cost_including_tax} * 0.25 = Rs {min(5000, get_discount(total_cost_including_tax , 0.25))}")
						total_coupon_discount = min(5000, get_discount(total_cost_including_tax , 0.25))
						break
					else:
						total_coupon_discount = 0
						break
				elif (coupon_code == 'CHILL50'):
					if (total_cost_including_tax >= 50000):
						print(f"[CHILL50] min(10000, Rs {total_cost_including_tax} * 0.50 = Rs {min(10000, get_discount(total_cost_including_tax , 0.50))}")
						total_coupon_discount = min(10000, get_discount(total_cost_including_tax , 0.50))
						break
					else:
						total_coupon_discount = 0
						break
				else:
					print("Invalid coupon code. Try again.")
					continue
				
			except Exception:
				print("Invalid Input . Try Again.")
				
				continue
		else:
			print("No coupon code applied.")
			total_coupon_discount = 0
			break
	print(f"TOTAL COUPON DISCOUNT = Rs {total_coupon_discount}")
	total_cost_after_coupon_discount = (total_cost_including_tax - total_coupon_discount)
	print(f"TOTAL COST = Rs {total_cost_after_coupon_discount}")

	return (total_cost_after_coupon_discount , total_coupon_discount)


	


def main():
	'''
	Description: This is the main function. All production level codes usually
	have this function. This function will call the functions you have written
	above to design the logic. You will see how splitting your code into specialised
	functions makes the code easier to read, write and debug. Include appropriate 
	print statements to match the output with the screenshots provided in the PDF.
	
	Parameters: No parameters
	
	Returns: No return value
	'''

	show_menu()
	def bulk_or_not():
		global a
		a=input("Would you like to buy in bulk? (y or Y / n or N) :\n")
		if ((a == 'y') or (a=='Y') or (a=='n') or (a=='N')):
			return a
		else:
			print("invalid")
			return bulk_or_not()
	bulk_or_not()
	if ((a == 'y') or (a=='Y')):
		get_bulk_input()
	else:
		get_regular_input()

	print_order_details(quantities)
	calculate_category_wise_cost(quantities)
	calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost)
	calculate_tax(discounted_apparels_cost,discounted_electronics_cost,discounted_eatables_cost)
	apply_coupon_code(total_cost_including_tax)

	print("Thank you for visiting!")
	


if __name__ == '__main__':
	main()
