
"""
SOAL
Akan diberikan sebuah angka. sebut saja angka ini N.
Hitunglah total penjumlahan dari angka 1 sampai N.
Cth input : 2
Cth output : 1 + 2 = 3
Cth input : 5
Cth output : 1 + 2 + 3 + 4 + 5 = 15
"""

if __name__ == "__main__":
    print("SOAL 3")
    a = 0
    while True:
        try:
            N = int(input("Masukkan angka : "))
            for i in range(N+1):
                a += i
            print("Total penjumlahan dari 1 sampai {} adalah {}".format(N, a))
            a=0
        except KeyboardInterrupt:
            print("stopping")
            exit()