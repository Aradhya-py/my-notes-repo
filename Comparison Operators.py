'''
Operator's :-
A > B = A is greater than B
A < B = A is smaller than B
A <= B = A is smaller than or equal to B
A >= B = A is greater than or equal to B 
A = B = A is equal to B or we setting the value equal to B 
A == B = It's like when A reaches the value of B 
A != B = A is not equal to B 
'''



temperature = int(input("Enter Temprature: "))

if temperature > 30 :
    print("It's a hot day ")

elif temperature < 20 :
    print("It's a cold day")

else :
    print("It's neither hot nor cold")


name = input("Enter your name: ")

if len(name) <= 3 :
    print("Name is too short")

elif len(name) >= 50 :
    print("Name is too long")

else:
    print("Name looks good")