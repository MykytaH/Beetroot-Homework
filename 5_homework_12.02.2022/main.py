import random

# task1
list_of_random_num = []
i = 0
while i < 10:
    list_of_random_num += [random.randint(1, 1264)]
    i += 1
print(max(list_of_random_num))

# task2

list_1 = []
list_2 = []
i = 0
while i < 10:
    list_1 += [random.randint(1, 10)]
    list_2 += [random.randint(1, 10)]
    i += 1
common_list = set(list_1).intersection(list_2)
print(common_list)

# task3

my_list = list(range(1, 101))
new_list = []
counter = 0
while counter < len(my_list):
    if my_list[counter] % 7 == 0 and my_list[counter] % 5 != 0:
        new_list += [my_list[counter]]
        counter += 1
    else:
        counter += 1
print(new_list)
