def kali(angka_1, angka_2):
    angka_kali = angka_1
    if angka_2 == 0:
        angka_1 = 0
    else:
        for i in range(1, angka_2):
            angka_1 += angka_kali
    print(f"Hasil kali adalah = {angka_1}")


def bagi(angka_1, angka_2):
    i = 0
    while angka_1 > 0:
        angka_1 -= angka_2
        i += 1
    if angka_1 < 0:
        i -= 1
    print(f"Hasil bagi adalah = {i}")


def input_int(perintah):
    while True:
        try:
            hasil = int(input(perintah))
            return hasil
        except ValueError:
            print("Pilih angka integer!")


def main():
    """Buatlah Program untuk dapat melakukan perhitungan perkalian dan pembagian
    dengan menggunakan teknik Looping. Program akan berjalan secara berkelanjutan
    selama pengguna menekan tombol huruf ’y’ pada keyboard."""

    print("-- Soal 1: Program Perhitungan Perkalian dan Pembagian mengggunakan teknik Looping. --")

    while True:
        while True:
            pilihan = input("Pilih operator perhitungan [kali/bagi]: ")
            if pilihan == 'kali' or pilihan == 'bagi':
                break
            else:
                print("Pilih antara bagi atau kali!")

        angka_1 = input_int("Masukkan angka pertama: ")
        angka_2 = input_int("Masukkan angka kedua: ")

        if pilihan == 'kali':
            kali(angka_1, angka_2)
        elif pilihan == 'bagi':
            bagi(angka_1, angka_2)

        pilihan = input("Apakah anda ingin melakukan perhitungan lagi? [y]: ")
        if pilihan.lower() != 'y':
            break


if __name__ == '__main__':
    main()
