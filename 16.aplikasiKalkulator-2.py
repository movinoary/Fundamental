print("+ untuk penjumlahan")
print("- untuk pengurangan")
print("* untuk perkalian")
print("/ untuk pembagina")
print("exit untuk keluar")

command = ""

while command != "exit":
    command = input("Perintah : ")

    if command == "exit":
        break

    if command != "+" and command != "-" and command != "*" and command != "/":
        print("Perintah tidak dikenali")
        continue

    frist_number = int(input("Masukan Angka Pertama: "))
    second_number = int(input("Masukan Angka Kedua: "))

    if command == "+":
        output = frist_number + second_number
        message = f"{frist_number} + {second_number} = {output}"
        print(message)
    elif command == "-":
        output = frist_number - second_number
        message = f"{frist_number} - {second_number} = {output}"
        print(message)
    elif command == "*":
        output = frist_number * second_number
        message = f"{frist_number} * {second_number} = {output}"
        print(message)
    elif command == "/":
        output = frist_number // second_number
        message = f"{frist_number} / {second_number} = {output}"
        print(message)

print("Terima aksih sudah mengguakan aplikasi kami")