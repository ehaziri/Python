
def draw_stars(x):
    for k in x:
        print(k * '*')
    print('\n')


a = [4, 6, 1, 3, 5, 7, 25]
b = draw_stars(a)


def draw_stars1(x):
    for k in x:
        if(type(k) is int):
            print(k * '*')
        else:
            str_length = len(k)
            first_char = k[0]
            print(str_length * first_char.lower())



x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
d = draw_stars1(x)
