n=int(input('Enter a number: '))+1
b=1
for i in range(0,n):
    n=n-1
    for j in range(0,n+1):
        print(' ',end='')
    print(n)