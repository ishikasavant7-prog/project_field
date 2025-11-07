#Write a program to input marks and display grade according to the following rules: Marks >= 90:
# A, Marks >= 80: B, Marks >= 70: C, Marks >= 60: D, else: Fail. (if-else ladder)
marks=int(input("enter the marks"))

if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("fail")
    