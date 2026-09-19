a=int(input("Enter a number from 1 to 10: "))

if(a<1 or a>10):
    print("Invalid input. Please enter a number between 1 and 10.")
else:
    match a:
        case 1:
            print("You won a car!")
        case 3:
            print("You won a bike!")
        case 7:
         print("You won a scooter!")
        case _:
            print("Sorry, you didn't win anything this time.")