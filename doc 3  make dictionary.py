# Q3.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.



x=int(input("enter the number...."))
c={}
i=1
while i<=x:
    c[i]=i*i
    i=i+1
print(c)
