w=float(input("Enter the wieght in kg : "))
h=float(input("Enter the hieght in m : "))
bmi=w//h**2
print("Healthy" if (bmi>=19 and bmi<=25) else "Overwieght" if (bmi>25) else  "Underwieght")