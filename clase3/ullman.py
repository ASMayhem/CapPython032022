def ullman(num):
    while num!=1:
        if num%2==0:
            num = num//2
        else:
            num = num*3+1
        print(num)

num = 5006337
ullman(num)