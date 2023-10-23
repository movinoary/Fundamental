numbers = (1,2,3,5)

# x = numbers[0]
# y = numbers[1]
# z = numbers[2]
# print(x)


x, y, _, c = numbers
x, *c = numbers

print(c)