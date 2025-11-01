def fibonacciSeries(num):
    fibo1 = 0
    fibo2 = 1

    print(fibo1)
    print(fibo2)

    for i in range(num - 2):
        temp = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = temp
        print(temp)


fibonacciSeries(10)
