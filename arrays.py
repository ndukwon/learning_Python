# Python3

array_test = range(1, 20)
print(array_test)            # range(1, 20)
print(*array_test)           # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
print(array_test.start)      # 1
print(array_test.stop)       # 20
print(array_test.__len__())  # 19
print(len(array_test))       # 19
print(array_test[2:4])       # range(3, 5)
print(*array_test[2:4])      # 3 4
print(*array_test[2:])       # 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
print(*array_test[:2])       # 1 2
print(*array_test[:])        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
print(*array_test[:-1])      # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
# array_test.append(3)
# array_test[1:3] = [9,8]

print(*array_test)

a = [9, 8, 7, 6, 5]
b = [4, 3, 2, 1, 0]
print(*(a + b))             # 9 8 7 6 5 4 3 2 1 0

# b = range(10)
# print(b)            # range(0, 10)
# print(*b)           # 0 1 2 3 4 5 6 7 8 9
# print(b.start)      # 0
# print(b.stop)       # 10
# print(b.__len__())  # 10
