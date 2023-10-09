week_days = {"Monday" : 40, "Tuesday" : 30, "Wednesday" : 32, "Thursday" : 50, "Friday" : 34, "Saturday" : 38, "Sunday" : 45}
for key, value in week_days.items():
    if value >= 40 and value <= 50:
        print(f"{key} : {value}")