m = int(input("Enter your marks out of 100 : "))
if m > 100 or m < 0:
    print("Invalid marks")
elif m >= 90:
    print("Grade : A")
elif m < 90 and m >= 80:
    print("Grade : B")
elif m < 80 and m >= 70:
    print("Grade : C")
elif m < 70 and m >= 60:
    print("Grade : D")
elif m < 60 and m >= 50:
    print("Grade : E")
else:
    print("Grade : Fail")