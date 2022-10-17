num = input ("Enter a number :- ")
dic = {"0" : "Zero" , "1":"One" , "2" : "Two" , "3" : "Three" , "4" : "Four" , "5" : "Five" , "6" : "Six" , "7" : "Seven" , "8" : "Eight" , "9" : "Nine"}
# for i in num :
#      print( dic[ i ], end = " ") 
i=0
while i<1:
    if num in dic:
        print(dic[num])
    i=i+1


