                #  Change Age Group 

age = int(input("Please enter your age: "))

if age < 13:
    print("You are a child")
    
elif age < 20:
    print("You are a Teenager")
    
elif age < 60:
    print("You are a Adult")
    
else:
    print("You are a Senior")      
    
    
        #  Movie Ticket Pricing
        
Hum_age = int(input("Please enter age the person: "))
day = "Wednesday"

price = 12 if Hum_age >= 18 else 8

if day == "Wednesday":
    price-= 2
    
print("Ticket price for you in $",price)

   
            # Grade Calculator
import sys
        
score = int(input("Enter your Grade: "))

if score >= 101:
    print("Please verify your grade again")
    sys.exit()

if score >= 90:
    print(" You Achieve A grade")
            
elif score >= 80:
    print("You Achieve B grade")
    
elif score >= 70:
    print(" You Achieve C grade")
    
elif score >= 60:
    print("You Achieve D grade")
    
else:
    print("You Achieve F grade")
    
print("Grade",score)
 
 
                    # Fruit Ripe Cracker
                    
fruit = input("Enter any fruit name: ")
color = input("Enter any color name:")

if fruit == "Banana" and color == "Green":
    print("UnRipe")
    
elif color == "Yellow":
    print("Ripe")
    
elif color == "Brown":
    print("OverRipe")
    
else:
    print("No Information")
    
                    # Weather Acitvity Suggestion
                    
weather = input("Enter the weather Suggestion: ")

if weather == "Sunny":
    print("Go for a Walk")
    
elif weather == "Rainy":
    print("Read a Book")
    
elif weather == "Snowy":
    print("Built a SnowMan")
    
else:
    print("Please Enter a Valid Suggestion")
    
                 # Transportation mode Selection
                 
distance = int(input("Enter the Distance: "))

if distance < 3:
    transport = "Go to Walk"
    
elif distance <= 15:
     transport = "Move in Bike"
     
else:
    transport = "Move in Car"
    
print("AI recommends you the transport of: ",transport)

                # order of Coffee
                
coffee_size = input("Enter the Coffee Size: ")

extra_shot = True

if extra_shot:
    coffee = coffee_size + " coffee with an extra shot"
    

    
else:
    coffee = coffee_size + "Coffee"
    
print("Order: ",coffee)

               # Password Checker 
               
passsword = input("Enter the Password: ")

if len(passsword) < 6:
    print("Weak")
    
elif len(passsword) <= 10:
    print("Medium")
    
else:
    print("Strong")
    
             #  Leap Year checker
             
year = int(input("Enter the Leap year: "))
    
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year ,"is a Leap year")
    
else:
    print(year,"is not a Leap year")
    
            # Pet Food Recommendation

                 # InComplete
   
pet_name = input("Enter pet name: ")

pet_age = int(input("Enter pet age: "))

if (pet_name == "Dog" or pet_name == "Cat") and pet_age < 2:
    print("Puppy food")

elif (pet_name == "Dog" or pet_name == "Cat") and pet_age < 5:
    print("Adult food")

else:
    print("Senior food")

    
