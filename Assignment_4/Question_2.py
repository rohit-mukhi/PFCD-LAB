# Left rotation by 1 step

def rotate(a, b, c):
    return (c, b, a)

a, b, c = 'Tony', 21, 1991
for _ in range(3):
    a, b, c = rotate(a, b, c)
    print(a, b, c)
