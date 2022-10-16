from datetime import datetime
from functools import reduce
from html.entities import name2codepoint


a = ("tuple", "list")
b = ("tuple", "list")

print(b)
print(a)
print(id(b))
print(id(a))


names = ["oliver", "joseph", "faith", "sani"]
names_2 = ["oliver", "joseph", "faith", "sani"]

names.append("chidera")
print(names)
print(names_2)
# is  
#  assertion
#  == is checking value equality
# a == b vs a is b

#  lambda function

# name = "philip"
# x = lambda num : num  * 2

# age = lambda birthyear : 2022 - birthyear


# print(age(2004))

# def greet():
#     return "Hello world"

# greet()

# perimeter = lambda length , breadth : 2 * (length + breadth)

# print(perimeter(20, 40))
# # lambda a, b, c  : a * b
# # lambda parameters : expression

# # def age(birthyear):
# #     return 2022 - birthyear

# # print(age(2004))


# print(x(4))

# def twice(num):
#     return num * 2

# print(twice(4))

# ternary operation

# salary = 50_000

# print('rich') if salary > 30_000 else print('broke')

# if salary > 30_000 :
#     print('rich')
# else:
#     print('poor')

# map
# map is used when you want to ma
# filter
# reduce


transctions = [900, 500, 400, 343, 560, -60, -340]
ages = [7, 8 ,19, 34, 32, 10 , 18]

balance = reduce(lambda a, b: a + b, transctions)
print(balance)
# adder = lambda num : num + 100

# filterer = lambda num : num < 18

# unqualified = filter(filterer, ages)
# print(list(unqualified))

# qualified = []

# for age in ages:
#     if age >= 18:
#         qualified.append(age)
# print(qualified)

# mapper = map(adder, transctions)
# print(list(mapper))

# start = datetime.now()

# new_trans = []
# for trans in transctions:
#     new_item = trans + 100
#     new_trans.append(new_item)

# end = datetime.now()

# print((end - start).total_seconds() * 10**3)

# print(new_trans)






