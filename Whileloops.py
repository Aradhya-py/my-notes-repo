i = 1
while i <= 5:
    print (i)
    i = i + 1
print ("done")


i = 1
while i <= 5:
    print ('x' * i )
    i = i + 1
print ("done")

# Guessing Game
Guess_number = 9
Guess_count = 0
Guess_limit = 3
while  Guess_count < Guess_limit :
    Guess = int(input(" Guess: "))
    Guess_count += 1 
    if Guess == Guess_number :
        print("You Win") 
        break
else:
    print("You lost")

# Car Game

command = ""
started = False  # Tracks whether the car is running

while True:
    command = input("> ").lower().strip()
    
    if command == "start":    
        if started:
            print("Hey, the car is already started!")
        else:
            started = True
            print("Car started... Ready to go!")
            
    elif command == "stop":
        if not started:
            print("The car is already stopped.")
        else:
            started = False
            print("Car stopped.")
            
    elif command == "help":
        print("""
start - To start the car 
stop  - To stop the car
quit  - To exit the game
        """)
        
    elif command == "quit":
        print("Goodbye!")
        break
        
    else:
        print("Sorry, I don't understand that. Type 'help' for options.")




while False:
    print("Empty")
    