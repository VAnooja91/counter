def findPrimeNumber(num):
    for n in range(2,num):
        if num % n == 0:
            return False
        return True
      
n=10
for i in range(2, n+1):            
    if(findPrimeNumber(i)):
        print(i)