marks = []
print("Enter 5 subjects marks :")
for i in range(5):
    marks.append(int(input(f"Subject {i + 1} : ")))
print("Total :", sum(marks))
print("Average :", sum(marks) / 5)