"""
Perhatikan kasus berikut ini:
Anda sedang berjualan bermacam macam buah, dan anda ingin melihat buah apa yang
paling laris di hari itu.
Anda memiliki data buah dan jumlah penjualan nya dalam kilogram.
Silahkan tentukan buah apa yang paling laris dari data yang telah dimasukkan secara
custom.
Cth input :
Durian, 10
Apel, 10
Mangga, 20
Jeruk, 30
Pepaya, 10
Cth output : Jeruk
"""

if __name__ == "__main__":
    arrBuah = []
    arrJumlah = []
    while True:
        try:
            rawInput = input("Masukkan nama buah dan jumlah penjualan (nama buah dan jumlah dipisahkan koma) : ").split(", ")
            for i in range(len(rawInput)):
                if i % 2 == 0:
                    arrBuah.append(rawInput[i])
                else:
                    arrJumlah.append(int(rawInput[i]))
            print("Buah yang paling laris adalah {}".format(arrBuah[arrJumlah.index(max(arrJumlah))]))
        except KeyboardInterrupt:
            print("stopping")
            exit()
            