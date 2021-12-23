def binary_diagnostic(file_in):
    with open(file_in) as f:
        data = f.readlines()
    counts = [0] * len(data[0].strip())
    for line in data:
        l = line.strip()
        i = 0
        for d in l:
            if d == '0':
                counts[i] -= 1
            else:
                counts[i] += 1
            i += 1
    gamma = epsilon = ''
    for c in counts:
        if c > 0:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    power = int(gamma, 2) * int(epsilon, 2)
    print(power)

def oxygen_generator_rating(file_in):
    with open(file_in) as f:
        data = f.readlines()
    count = 0
    list0 = []
    list1 = []
    i = 0
    while len(data) > 1 and i < len(data[0]):
        for line in data:
            l = line.strip()
            if l[i] == '0':
                list0.append(l)
                count -= 1
            else:
                list1.append(l)
                count += 1
        data = list0 if count < 0 else list1
        list0 = []
        list1 = []
        count = 0
        i += 1
    ogr = int(data[0], 2)
    return ogr

def c02_scrubber_rating(file_in):
    with open(file_in) as f:
        data = f.readlines()
    count = 0
    list0 = []
    list1 = []
    i = 0
    while len(data) > 1 and i < len(data[0]):
        for line in data:
            l = line.strip()
            if l[i] == '0':
                list0.append(l)
                count -= 1
            else:
                list1.append(l)
                count += 1
        data = list1 if count < 0 else list0
        list0 = []
        list1 = []
        count = 0
        i += 1
    csr = int(data[0], 2)
    return csr

binary_diagnostic('input.txt')
lsr = oxygen_generator_rating('input.txt') * c02_scrubber_rating('input.txt')
print(lsr)
