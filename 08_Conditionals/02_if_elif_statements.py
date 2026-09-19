#write elif program that checks the age of a person and prints whether they are a child, teenager, adult, or senior citizen.age = int(input("Enter your age: "))


age = int(input("Enter your age: "))
if(age<13):
    print("you are a child.")
elif(age>=13 and age<20):
    print("you are a teenager.")
elif(age>=20 and age<60):
    print("You are an adult.")
else:
    print("You are a senior citizen.")