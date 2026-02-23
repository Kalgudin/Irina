# d = [1, 3, 5, 8, 11]
#
# flfind = False
# i = 0
# while i < len(d):
#     flfind = d[i] % 2 == 0
#     i += 1
#     if flfind:
#         break
# print(i)

d = 1
s = 0

while d != 0:
    d = int(input('input '))
    if d % 2 == 0:
        continue
    s += d
    print(f's = {s}')