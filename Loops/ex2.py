#Write a program that reads two integer numerical values and performs the addition, if the result is greater than 10, print it.

i1 = int(input("Enter the first integer: "))
i2 = int(input("Enter the second integer: "))
addition = i1 + i2
if addition > 10:
    print(f"The addition is {addition}")
else:
    print("The addition is less than 10")    