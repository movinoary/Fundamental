course = "bElajar PyHton perTama viNo"
language = "PyHton"
language_ = "pyhton"

length = len(course) # len =mencari ada berapa karakter
course_capital = course.upper()
course_lower = course.lower()
course_capitalize = course.capitalize()
course_title = course.title()
course_replace = course.replace("PyHton", "Javascript")


print(course)
print(length)
print(course_capital)
print(course_lower)
print(course_capitalize)
print(course_title)
print(course_replace)
print(language in course)
print(language_ in course)


# function (len()) = langsung dipanggil tanpa ada objek
# method (couser.upper()) = dipanggil oleh sebuah objek || wajibb ada () untuk memanggil