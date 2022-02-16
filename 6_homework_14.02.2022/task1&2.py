# task1

a_string = input("Write smth: ")
split_string = a_string.split()
new_dict = {}
occurrences_counter = 0
for i in split_string:
    occurrences_counter += 1
    new_dict[i] = occurrences_counter
print(new_dict)

# task2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock_list = []
prices_list = []
total_price = 0
for i in stock.values():
    stock_list += [i]
for j in prices.values():
    prices_list += [j]
for k in range(0, len(stock_list)):
    total_price += stock_list[k] * prices_list[k]
print(total_price)

