# class Clothes:
#     @classmethod
#     def __init__(cls, sex, size):
#         cls.sex = sex
#         cls.size = size
#
#
# class TShirt(Clothes):
#     def __init__(self, sex, size, color):
#         super().__init__(sex, size)
#         self.color = color
#
#
# cl1 = Clothes("male", 65)
# cl2 = Clothes("female", 54)
# print(cl1.sex, cl1.size)
#
# th1 = TShirt("male", 65, ' asdf')
# th2 = TShirt("female", 54, 'f')
# print(th1.sex, th1.size, th1.color)


a, x, b, y, c = int(input()), int(input()), int(input()), int(input()), int(input())

for i in range(c):
    a += x
    b += y

if a > b:
    print("ИИ")
elif a < b:
    print("ПП")
else:
    print("ОДИНАКОВО")

