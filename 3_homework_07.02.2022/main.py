weight = 83
height = 1.83
body_mass_index = weight/height**2
if body_mass_index < 18.5:
    print('Your BMI is below normal')
elif 18.5 <= body_mass_index <= 25.5:
    print('Your BMI is normal')
else:
    print('Your BMI is above normal')

