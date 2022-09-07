def writeSwap():
    f = open("swap.txt","w")
    a = input("Enter First Number")
    b = input("Enter second Number")
    f.write(a + ":" + b)
    f.close()
def readSwap():
    f = open("swap.txt","r")
    data = f.readlines()
    for d in data:
     a = d[:d.find(':')]
     b = d[d.find(':')+1:]
    a,b =b,a
    print(a,b)
    f.close()
#writeSwap()
readSwap()

