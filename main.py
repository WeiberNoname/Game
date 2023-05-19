money = input("SALE")
key = input("a,b,c")
ggg = int(money) / 1
if key == " a" :
    print("well")
    ggg = int(money) / 2000
else :
    print("nnnnn")
if int(money) <= 100 :
    print("Well%5.2f" % ggg)
elif int(money)> 100:
    ggg = ggg / 1.1
    print("%5.2f" % ggg)
    
    



