
# A python code the requests the user to enter a number x to check the numbers that are divisible by 3 and 5

x = input("Enter the number x: ") # Asks the user to enter a number and stores it in x

for x in range(1,int(x)+1,1): # Checks the numbers the numbers from one to x that are divisible by 3 and 5 and prints them
    if(x%3==0 | x%5==0):
        print(x)