def a(n,k):
    i=0
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    while i<k:
        if n[i].isupper():
            count+=1
        if n[i].islower():
            count1+=1
        if n[i].isdigit():
            count2+=1
        if n[i].isalpha():
            count3+=1
        if n[i].isalnum():
            count4+=1
        if n[i]in "#@$%^&!~*0123456789":
            count5+=1
            
        i=i+1
    if count==k:
        print(True)
    elif count1==k:
        print(False)
    elif count2==k:
        print(True)
    elif count3==k:
        print(False)
    elif count4==k:
        print(False)
    elif count5==k:
        print(True)
    else:
        print(False)
    
n=input("enter the input..")
a(n,len(n))



