operasi = input("Masukan Operasi: ")

if operasi == "+":
    frist_number = input("Masukan Angka Pertama: ")
    second_number = input("Masukan Angka Kedua: ")
    frist_number = int(frist_number)
    second_number = int(second_number)

    output = frist_number + second_number
    message = f"{frist_number} + {second_number} = {output}"
    print(message)
elif operasi == "-":
    frist_number = input("Masukan Angka Pertama: ")
    second_number = input("Masukan Angka Kedua: ")
    frist_number = int(frist_number)
    second_number = int(second_number)

    output = frist_number - second_number
    message = f"{frist_number} - {second_number} = {output}"
    print(message)
elif operasi == "*":
    frist_number = input("Masukan Angka Pertama: ")
    second_number = input("Masukan Angka Kedua: ")
    frist_number = int(frist_number)
    second_number = int(second_number)

    output = frist_number * second_number
    message = f"{frist_number} * {second_number} = {output}"
    print(message)
elif operasi == "/":
    frist_number = input("Masukan Angka Pertama: ")
    second_number = input("Masukan Angka Kedua: ")
    frist_number = int(frist_number)
    second_number = int(second_number)

    output = frist_number // second_number
    message = f"{frist_number} / {second_number} = {output}"
    print(message)
else:
    print("operator tidak diketahui")


