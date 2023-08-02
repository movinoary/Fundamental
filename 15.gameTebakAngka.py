trying = 0
secret_numer = 7
limit = 3

while trying < limit:
    guess_number = input("Masukan Angka (0-9): ")
    guess_number = int(guess_number)
    if guess_number == secret_numer:
        print("Selamat Kamu benar")
        break # maksa untuk berhenti
    else:
        print("Silahkan coba lagi")
        trying += 1