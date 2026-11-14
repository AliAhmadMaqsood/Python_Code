                     # First ten number
                                         
number = 1

while number <= 10:
    print(number)
    number += 1

                   # Print 1 to 10  even number
                   
number = 2

while number <= 10:
    print(number)
    number += 2
       
                 # print 1 to 20 even number
                 
number = 2

while number <= 20:
    print(number)
    number += 2
     
                # Sum of first ten numbers
                
number = 1
sum = 0

while number <= 10:
    sum += number
    number += 1
print(sum)

              # Factioral of 5
number = 5
factioral = 1

while number > 0:
    factioral = factioral * number
    number = number -1
    
print("Factorial value of a number is: " , factioral)

            # Count a number in a digit
            


word = input("Enter any string: ")

reverse_str = ""
index = len(word) - 1

while index >= 0:
    reverse_str += word[index]
    index -= 1

print("Reversed string:", reverse_str)


          # palindrome number or not

number = 121
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print(original, "is a palindrome number")
else:
    print(original, "is not a palindrome number")

    
