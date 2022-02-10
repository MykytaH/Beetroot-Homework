def white(black):
    return 1 - black


def red(cyan, black):
    return 255 * (1 - black) * (1 - cyan)


def green(magenta, black):
    return 255 * (1 - black) * (1 - magenta)


def blue(yellow, black):
    return 255 * (1 - black) * (1 - yellow)
