                             # Counting Postive Number
                             
    
numbers = [ 1, -2 , 3 , -4 , 5 , -6 , 7 , -8 , 9 , 10]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count+=1
print("Final Count of Positive number is", positive_number_count)


                          # Sum of all even numbers
                          
            
n = int(input(" Enter the number: "))
sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even+= 1
        
print("Sum of even number is: ",sum_even)

                            # Muliply table of any numbers 
                            
                    
number = int(input(" Enter the number: "))

for i in range(1,11):
    if i == 5:
        continue
    print(number,'x',i,'=',number * i)
    
                           # Reverse String using Loop


input_str = input("Enter any string: ")
reverse_str = ""

for char in input_str:
    reverse_str = char + reverse_str
    
print(reverse_str)

                       # First non-repeated character in a string
                       
non_repeated_char = input("Enter any string: ")

for char in non_repeated_char:
    print(char)
    if non_repeated_char.count(char) == 1:
        print("Char is: ",char)
        break
    
                      # Factioral Calcuator
                      
number = int(input("Enter the number: "))
factioral = 1

while number > 0:
    factioral = factioral * number
    number = number -1
    
            # or
    # factioral *= number
    #     number -=1
    
print("Factorial vlaue of a number is: " , factioral)


                          # Validate input
                          
while True:
   number = int(input("Enter the number between 1 to 10: "))
   if 1 <= number <= 10:
        print("Valid number") 
        break 
   else:
        print("Invalid number")
        
                       # Prime number checker
                       
prime_number = int(input("Enter the number: "))

is_prime = True

if prime_number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            is_prime = False
            break
        
print(is_prime)


                   # List uniqueness checker
                   
items = ["Apple", "Banana" , "Orange" , "Apple", "Mango"]

uniques_item = set()

for item in items:
    if item in uniques_item:
        print("Dublicate ",item)
        break
    uniques_item.add(item)
    
                   # Exponential Backoff
                   
import time

wait_time = 1
max_retries = 5
attempts =0

while attempts < max_retries:
    print("Attempt",attempts +1, " - wait time" , wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
