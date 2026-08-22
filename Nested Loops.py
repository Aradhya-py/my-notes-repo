for x in range(2):
    for y in range(2): # New loop or Inner loop where y resets to 0 
        print(f'({x},{y})') 


numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''

    for count in range(x_count):
        output +='x'

        print(output)