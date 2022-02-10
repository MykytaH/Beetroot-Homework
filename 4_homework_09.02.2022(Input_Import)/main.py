import random

# task1

number = random.randint(1, 10)
user_number = int(input('Try to guess number between 1 and 10: '))
while True:
    while user_number > 10 or user_number < 1:
        user_number = int(input('BETWEEN 1 AND 10 !!!!: '))
    if number == user_number:
        print('Yeah, you right!')
        break
    while 1 <= user_number <= 10 and user_number != number:
        user_number = int(input('No :( , you can try again: '))

# task2

name = input('Enter your name, please: ')
age = int(input('Now enter your age, please: '))
print('Hello ' + name + ', on your next birthday you’ll be ' + str(age + 1) + ' years!')

# task3

user_string = input('Write smth, please: ')
counter = 1
while counter <= 5:
    counter += 1
    user_str_for_cycle = user_string
    new_string = ''
    while len(user_str_for_cycle) >= 1:
        random_element = random.randint(0, len(user_str_for_cycle) - 1)
        new_string = new_string + user_str_for_cycle[random_element]
        user_str_for_cycle = user_str_for_cycle[:random_element] + user_str_for_cycle[random_element + 1:]
    print(new_string)

# task4

element_1 = random.randint(0, 100)
element_2 = random.randint(0, 100)
operation = random.randint(0, 1)
if operation == 0:
    user_answer = int(input('Solve: ' + str(element_1) + ' + ' + str(element_2) + ' : '))
    right_answer = element_1 + element_2
elif operation == 1:
    user_answer = int(input('Solve: ' + str(element_1) + ' - ' + str(element_2) + ' : '))
    right_answer = element_1 - element_2
if user_answer == right_answer:
    print('You are a great mathematician!')
else:
    print('You are not such a great mathematician(')
