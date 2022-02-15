
# 1.
# Інтерпритована, з динамічною типізацією.Має багато бібліотек.

# 2.
# Не повинна починатися великої літери або цифри, без пробілів, підкреслювання замість пробілів.

# 3.

major_version = 3
minor_version = .9
version = major_version + minor_version
language = 'Python'
language_version = language + ' ' + str(version)

# 4.

numbers = 0
desired_numbers_sum = 0
while numbers <= 100:
    if numbers % 3 == 0 and numbers % 5 == 0:
        desired_numbers_sum += numbers
        numbers += 1
    else:
        numbers += 1

# 5.

surname = 'Havrilenko'
sur_length = len(surname)
counter = 1
factorial = 1
while counter <= sur_length:
    factorial *= counter
    counter += 1
print(str(sur_length) + '! = ', str(factorial))

# 6.

string = 'This is Sparta'
while len(string) >= 1:
    print(string)
    string = string[0:len(string) - 1]
else:
    print("Nothing's left here")

# Просунутий рівень

# 1.
# Швидкість виконання програми в інтерпитованій мові набагато менша ніж в компільованій. Перевагою є те,
# що код становиться "чистим", та простим для написання і сприйняття

# 2.
# Мутабельні типи допускають зміну своїх властивостей, імутабельні ні


# 3.

number = 1787
counter = 1
while counter <= number:
    if 1 < counter < number and number % counter == 0:
        print("It's not a prime number")
        break
    elif counter == number:
        print("It's a prime number")
        break
    else:
        counter += 1

# 4.

fibonacci_num_1 = 0
fibonacci_num_2 = 1
negative_fibo_num_sum = 0
while fibonacci_num_1 <= 100000:
    fibonacci_num_2 += fibonacci_num_1
    fibonacci_num_1 += fibonacci_num_2
    if fibonacci_num_1 % 2 != 0:
        negative_fibo_num_sum += fibonacci_num_1
        print(negative_fibo_num_sum)
    if fibonacci_num_2 % 2 != 0:
        negative_fibo_num_sum += fibonacci_num_2
        print(negative_fibo_num_sum)
