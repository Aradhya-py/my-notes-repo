'''
Set Rules like 
if it's hot 
   it's a hot day 
   Drink plenty of water 
otherwise if it's cold day
             it's a cold day      
             wear warm clothes
otherwise it's a lovely day 

'''
is_hot = True
is_cold = False

if is_hot:
    print (" It's a hot day , Drink plenty of water")
elif is_cold :
    print (" It's a cold day , Wear warm clothes")
else :
    print (" It's a lovely day")

'''
Price of House = 1M 
if buyer has good credit 
they need to put down 10 % 
otherwise they need put down 20 % 

'''
Price_house = 1000000   
has_good_credit = True

if has_good_credit:
    Downpayment = Price_house * 0.1
else : 
    Downpayment = Price_house * 0.2 

print(Downpayment)