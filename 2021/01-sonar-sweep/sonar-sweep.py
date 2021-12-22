def sonar_sweep(file_in):
    with open(file_in) as f:
        measurements = f.readlines()
    inc = 0
    for i in range(len(measurements)):
        m = int(measurements[i])
        measurements[i] = m
        if i > 0 and m > measurements[i-1]:
            inc += 1
        i += 1
    print(inc)

def sliding_window(file_in):
    with open(file_in) as f:
        measurements = f.readlines()
    inc = 0
    windows = []
    for i in range(len(measurements)):
        m = int(measurements[i])
        measurements[i] = m
        if i > 1:
            windows.append(m + measurements[i - 1] + measurements[i - 2])
            if i > 2:
                if windows[i - 2] > windows[i - 3]:
                    inc += 1
        i += 1
    print(inc)

sonar_sweep('input.txt')
sliding_window('input.txt')
