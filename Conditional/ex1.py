#Write a program that reads 3 numbers and prints the largest of them.

larger = 0
for i in range (1,4):
    n = float(input("Enter the number: "))
    if n > larger:
        larger = n
print (f"The largest is {larger}")    
