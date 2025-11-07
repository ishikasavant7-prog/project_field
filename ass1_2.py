# Write a program to input three numbers and find the greatest among them. 
# (if-else)
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if num1>=num2 and num1>=num3:
    print('num1 is greter')
elif num2>num1 and num2>=num3:
    print('num2 is greter')
else:
    print('num3 is greter')