weight = 80
height = 1.83
body_mass_index = weight/height**2
index_check = 18.5 < body_mass_index < 25
print('Your BMI is normal:', index_check, end='\n\n\n')


phone_number = '380686435755'
lengths = len(phone_number) != 12
first_three_symbols_check = phone_number[0:3] != '380'
only_numbers_check = phone_number.isdigit() != 1
valid_check = lengths + first_three_symbols_check + only_numbers_check == 0
print('Phone number is valid:', valid_check)
