year = input("Tahun lahir : ")
print(type(year)) # melihat tipe data

year = int(year) # function mengubah  integer
print(type(year)) # melihat tipe data

age = 2022 - year
# print(age)

age = str(age) # function mengubah menjadi string
print("umur kamu = " + age)