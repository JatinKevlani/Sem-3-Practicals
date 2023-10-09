dict1 = {"name" : "ABC", "age" : 17, "gender" : "male"}
print(dict1)
dict1.pop("name")
print(dict1)
print("name" in dict1)
for key, value in dict1.items():
    print(f"{key} : {value}")
dict2 = {"phone" : 1234567890, "email" : "abc@xyz.com"}
dict1.update(dict2)
print(dict1)