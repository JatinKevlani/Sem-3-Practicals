data = []
while True:
    name = input("Enter you name : ")
    contNo = int(input("Enter your contact number : "))
    email = input("Enter your email id : ")
    bd = input("Enter your date of birth : ")
    details = {
        "Name" : name,
        "Contact no." : contNo,
        "Email" : email,
        "DOB" : bd
    }
    data.append(details)
    choice = int(input("Do you want to add more information or exit (0 to exit or 1 to continue) : "))
    if choice == 0:
        break
for details in data:
    for key, value in details.items():  
        print(f"{key} : {value}")