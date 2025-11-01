def fibonacciSeries(num):
    temp1 = 0
    temp2 = 1

    print(temp1)
    print(temp2)

    for i in range(3, num + 1):
        temp = temp1 + temp2
        temp1 = temp2
        temp2 = temp
        print(temp)


fibonacciSeries(10)
