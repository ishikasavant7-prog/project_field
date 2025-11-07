# Write a program to find the factorial of a number using a loop
a=int(input("enter the number="))
factorial=1
for i in range(1,a+1):
    factorial*=i
    print(factorial)