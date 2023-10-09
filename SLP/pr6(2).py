nums = []
sum = 0
print("Enter numbers (type \"exit\" to exit) : ")
while True:
    n = input()
    if n.lower() == "exit":
        break
    sum += int(n)
    nums.append(int(n))
posNums = 0
negNums = 0
zeros = 0
oddNums = 0
evenNums = 0
avg = sum / len(nums)
for num in nums:
    if num >= 0:
        posNums += 1
    else:
        negNums += 1
    if num == 0:
        zeros += 1
    if num % 2 == 0:
        evenNums += 1
    else:
        oddNums += 1
print(f"Number of positive numbers : {posNums}")
print(f"Number of negative numbers : {negNums}")
print(f"Number of zeros : {zeros}")
print(f"Number of odd numbers : {oddNums}")
print(f"Number of even numbers : {evenNums}")
print(f"Average of all numbers : {avg}")