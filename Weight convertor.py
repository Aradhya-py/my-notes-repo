Kg_or_lb = input("Is your weight in Kg or Lb: ").lower()

if Kg_or_lb == "kg":
    Weight_in_Kg = float(input("Enter your weight in Kg: "))
    Pounds = Weight_in_Kg * 2.20462
    print(f'Your weight in Pounds is : {Pounds}')

elif Kg_or_lb == "lb":
    Weight_in_Lb = float(input("Enter your weight in Lb: "))
    Kilogram = Weight_in_Lb / 2.20462
    print(f'(Your weight in Kg is : {Kilogram}')

else:
    print("Please enter kg or lb")
