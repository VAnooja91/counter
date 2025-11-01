def fibonacciSeries(num):
    fibo1 = 0
    fibo2 = 1

    print(fibo1)
    print(fibo2)

    for _ in range(num - 2):   
        fibo1, fibo2 = fibo2, fibo1 + fibo2
        print(fibo2)


fibonacciSeries(10)
