# Driver code


# tup = (1, 2, 3, 4, 5, )
# print (tup)
#
# print(type(tup))

# new_diction = {6:4}
# newer_diction = {1:2,3:5}
# newer_diction.update(new_diction)
#
# print(newer_diction)
#
# b = {1:2, 3:4}
# c = b.copy()
# print(c == b)
#
# print(dict.fromkeys(["phone"],(    "default",5)))

b = {
    1: "ONE",
    2: "TWO",
    3: "THREE",
}
#
# print(b.get(0))
#
# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
# inventory['cookie']=5
#
# print(inventory)

# print(playlists[0]['songs'][0]['duration'])
# print({"_abcdefghijklmnopqrstuvwxyz"[k]: k for k in range(1,len("_abcdefghijklmnopqrstuvwxyz"))})

# print({("_abcdefghijklmnopqrstuvwxyz"[num], "vowel" if "_abcdefghijklmnopqrstuvwxyz"[num] in ['a', 'e', 'i', 'o',
#                                                                                               'u'] else "consonant"): "even" if num % 2 == 0 else "odd"
#        for num in range(1, 27)})

# print([num if num == 5 else 3 for num in range(1,6)])
#
# print("This is an escape sequence \n")

# numbers = [1, 2, 3, 4, 6, ]
# #
# # print(numbers[:1:-1])
#
# from random import choice
#
# s = [choice(numbers) for num in numbers]
#
# for i,j in ((1,2),(7,13),(9,11)):
#     print(i,j)
#

s = {1, 2, 2, 3}

l = list({1: 2, 2: 3, 3: 4, })