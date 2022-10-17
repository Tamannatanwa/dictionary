



# def ask_question():
#     pass
# print("once")
# i=1
# while(i<=100):
#     ask_question()
#     print("ram")
# i+=1



x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(x)
print('x is now', x)



def distance(kms):
    if kms <= 20:
        print("close")
    elif kms < 50:
        print("far")
    else:
        print("median")
distance(20)



def add_numbers(number_x, number_y):
    number_sum = number_x + number_y
    return number_sum

sum1 = add_numbers(20, 40)
print(sum1)
sum2 = add_numbers(560, 23)
a = 1234
b = 12
sum3 = add_numbers(a, b)
print(sum2)
print(sum3)
number_a = add_numbers(20, 40) / add_numbers(5, 1)
print(number_a)




def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
print(maximum(2, 3))