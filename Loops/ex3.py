#Make a program that reads two integer values and performs the addition. If the summed value is greater than 20, it must be presented by adding to it plus 8, if the summed value is less than or equal to 20, it must be presented by subtracting 5.
i1 = int(input("Enter the first integer: "))
i2 = int(input("Enter the second integer: "))
addition = i1 + i2
if addition <= 20:
    print(f"The result is {addition-5}")
else:
    print(f"The result is {addition+8}")        