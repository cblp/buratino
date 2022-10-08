
def tree(x):
    SPACE = ' '
    STRAR = '*'

    if __name__ == "__main__":
        rows = x
        spaces = rows - 1
        stars = 1

        for i in range(rows):
            print(
                (SPACE * spaces) +
                (STRAR * stars) +
                (SPACE * spaces)
            )
            stars += 2
            spaces -= 1
print (tree(int(input())))