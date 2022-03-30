n=100
def me1(n):
    for i in range (1,n+1):
        if(i%15==0):
            print(i,"BizzFuzz")
        elif(i%3==0):
                print(i,"Bizz")
        elif(i%5==0):
                print(i,"Fuzz")

def me2(n):
    for i in range (1,n+1):
        if(i%3==0 and i%5==0):
            print(i,"BizzFuzz")
        elif(i%3==0):
                print(i,"Bizz")
        elif(i%5==0):
                print(i,"Fuzz")
def me3(n):
    for i in range (1,n+1):
        res=""
        if(i%3==0):
            res+="Fizz"
        if(i%5==0):
            res+="Buzz"   
        print(i if (res=="") else i,"",res)  

me3(n)                    