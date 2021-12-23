def dive(file_in):
    with open(file_in) as f:
        commands = f.readlines();
    h = 0
    d = 0
    for c in commands:
        c = c.strip().split(' ')
        if c[0] == 'forward':
            h += int(c[1])
        elif c[0] == 'down':
            d += int(c[1])
        else:
            d -= int(c[1])
    print(h * d)

def aim_and_dive(file_in):
    with open(file_in) as f:
        commands = f.readlines();
    h = 0
    d = 0
    a = 0
    for c in commands:
        c = c.strip().split(' ')
        x = int(c[1])
        if c[0] == 'forward':
            h += x
            d += a * x
        elif c[0] == 'down':
            a += x
        else:
            a -= x
    print(h * d)

dive('input.txt')
aim_and_dive('input.txt')
