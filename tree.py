SPACE = ' '
STRAR = '*'

if __name__ == "__main__":
    rows = 1
    spaces = rows-1
    stars = 2

    for i in range(rows):
        print(
            (SPACE*spaces) +
            (STRAR*stars) +
            (SPACE*spaces)
        )
        stars += 2
        spaces -= 1