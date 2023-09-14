# f = open("mydata", "r")

# print(f.read())
# print(f.readline(), end="")
# print(f.readline())

# f1 = open("abc", "w")
# f1.write("apple")
# f1.write("banana")

# f1 = open("abc", "a")
# f1.write("apple")

# f1 = open("abc", "w")

# To read all the data from mydata
# for data in f:
#     print(data)

# To copy data from mydata to abc
# for data in f:
#     f1.write(data)

# To open an image file in python (rb for binary file)
f = open("yellow.jpg", "rb")
# print(f.read())
f2 = open("mypic.JPG", "wb")
for data in f:
    f2.write(data)