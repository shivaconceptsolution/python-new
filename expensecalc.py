f = open("expenses.txt","a+")  
def createExpenses():
  
  name = input("enter name")
  amount = input("enter amount")
  f.write("\n" + name + ":" + amount)
def viewReport():
   exp1=0
   exp2=0
   total =0
   f.seek(0)
   data = f.readlines()
   dic = {}
   lst = []
   for d in data:  # file to dictionary
     n=d[:d.find(':')]
     dic.update({n:''})
     #total = total + int(a)
   for l in dic:   # dictionary to list
       lst.append(l)
   for d in data:    # calculate from flle
     n=d[:d.find(':')]
     a=d[d.find(':')+1:]
     total = total + int(a)
     
     if n ==lst[0]:
         exp1 = exp1 + int(a)
     else:
         exp2 = exp2 + int(a)
   #print(total, exp1,exp2)     
   print("Total expenses by " + lst[0] + "is = " + str(exp1-total//2))
   print("Total expenses by " + lst[1] + "is = " + str(exp2-total//2))
   
   f.close()


while True:
    i = input("press 1 for create and 2 for view other for exit")
    if i == "1":
        createExpenses()
    elif i=="2" :
        viewReport()
    else:
        break

        
    

