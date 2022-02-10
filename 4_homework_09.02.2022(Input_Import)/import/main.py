from converter.converter import white, red, green, blue

cyan = float(input('Enter cyan: '))
magenta = float(input('Enter magenta: '))
yellow = float(input('Enter yellow: '))
black = float(input('Enter black: '))

print(f' white = {white(black)}\n',
      f'red = {red(cyan, black)}\n',
      f'green = {green(magenta, black)}\n',
      f'blue = {blue(yellow, black)}\n')
