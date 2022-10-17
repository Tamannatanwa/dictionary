# class DemoCalss:
#     a=10
#     b=20
#     c=a+b
# demoobject=DemoCalss()
# demoobject1=DemoCalss()
# print(demoobject.a)
# print(demoobject1.c)



# class DemoCalss:
#     a=10
#     def sum(self):
#         print(20+30)
# demoobject=DemoCalss()
# demoobject1=DemoCalss()
# print(demoobject.a)
# print(demoobject1.a)
# demoobject.sum();




# class Phone:
#     def make_call(self):
#         print("making phone call")
#     def play_game(self):
#         print("playing game")
# p1=Phone()
# p1.make_call()




class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("making phone call")
    def play_game(self):
        print("playing game")
p2=Phone()
p2.set_color("blue")
p2.set_cost(5000)
p2.show_color()
p2.show_cost()
p1=Phone()
p2.make_call()
p2.play_game()

