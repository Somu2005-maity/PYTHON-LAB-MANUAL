class Demo:
    def add(self, a=None, b=None, c=None):
        if a and b and c:
            print(a + b + c)
        elif a and b:
            print(a + b)
        else:
            print("Invalid")

obj = Demo()
obj.add(10, 20)
obj.add(10, 20, 30)
