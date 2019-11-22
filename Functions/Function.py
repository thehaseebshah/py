# Functions


# def add(a, b):
#     return a + b
#
#
# def sub(a, b, ):
#     return a - b
#
#
# def math(a, b, fn=add):
#     return fn(a, b)
#
#
# print(math(1, 2))
# print(math(a=1, fn=sub, b=2))
#
# def str(s,v):
#     return "the value is {v}. "
#
# k = "the value is {val}. "
# val = 5
# print("the value is {val}. ")
# print(str(k,5))

# tot = 0
#
#
# def glob():
#     global tot
#     tot += 1

# def outer():
#     tot = 0
#     def mid():
#         def inner():
#             print(1)
#             return tot
#         return inner()
#     return mid()

def inner():
    print(1)
    # nonlocal tot
    # return tot

def mid():
    inner()


def outer():
    tot = 0
    mid()

    # return mid()

# print(outer())