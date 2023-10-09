import random

def shuffle(input_list):
    shuffled_list = input_list.copy()
    n = len(shuffled_list)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]
    return shuffled_list

original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle(original_list)
print(shuffled_result)