d1 = {'Andhra Pradesh': 'Amaravati', 'Arunachal Pradesh': 'Itanagar', 'Assam': 'Dispur', 'Bihar': 'Patna', 'Chhattisgarh': 'Raipur', 'Goa': 'Panaji', 'Gujarat': 'Gandhinagar', 'Haryana': 'Chandigarh', 'Himachal Pradesh': 'Shimla', 'Jharkhand': 'Ranchi', 'Karnataka': 'Bengaluru', 'Kerala': 'Thiruvananthapuram', 'Madhya Pradesh': 'Bhopal', 'Maharashtra': 'Mumbai', 'Manipur': 'Imphal', 'Meghalaya': 'Shillong', 'Mizoram': 'Aizawl', 'Nagaland': 'Kohima', 'Odisha': 'Bhubaneswar', 'Punjab': 'Chandigarh', 'Rajasthan': 'Jaipur', 'Sikkim': 'Gangtok', 'Tamil Nadu': 'Chennai', 'Telangana': 'Hyderabad', 'Tripura': 'Agartala', 'Uttar Pradesh': 'Lucknow', 'Uttarakhand': 'Dehradun', 'West Bengal': 'Kolkata'}

for key, value in d1.items():
    capital = input(f"Enter capital of {key} : ")
    if capital.lower() == "exit":
        break
    if capital.lower() == value.lower():
        print("Correct")
    else:
        print("Incorrect")