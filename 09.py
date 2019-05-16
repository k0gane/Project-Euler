for i in range(3, 300):
    for j in range(4, 401):
        k = pow((i * i) + (j * j), 0.5)
        if k == int(pow((i * i) + (j * j), 0.5)) and (i + j + k == 1000):
            print(int(i*j*k))       