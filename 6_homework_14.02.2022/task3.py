list_i = [i for i in range(1, 11)]
list_j = [i**2 for i in list_i]
new_list = [(i, j) for i, j in zip(list_i, list_j)]
print(new_list)
