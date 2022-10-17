sum=0
def ram(a):
    global sum
    if a==0:
        return 1
    else:
        sum+=a
        print(sum)
    ram(a-1)
ram(int(input("enter the number..")))