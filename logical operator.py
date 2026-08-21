'''
Logical Operatiors 
AND = Both Conditions True  as in Example 2
OR = at least one 
NOT = Inverses bullian value as in Example 1 


'''


# Example 1
Has_good_Credit = True
Has_criminal_record = False

if Has_good_Credit and not Has_criminal_record : 
    print("Eligible for Loan")

# Example 2
Has_good_credit = True 
Has_high_income = False 

if Has_high_income and Has_good_Credit :
    print("Eligible for Loan")

# Example 3 
Has_good_credit = True 
Has_high_income = False 

if Has_high_income or Has_good_Credit : # Similar to AND but one At least one value true 
    print("Eligible for Loan")

