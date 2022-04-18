"""
SOAL
Akan diberikan dua angka, N dan K.
Dan akan diberikan array dengan panjang N.
Silahkan tentukan apakah bisa mendapatkan nilai K dengan menjumlahkan 2 angka
dari array yang diberikan.
Cth input : N = 5, K = 10, array = [4, 3, 6, 7, 1]
Cth output : BISA
Cth input : N = 5, K = 10, array = [4, 1, 8, 7, 4]
Cth output : TIDAK BISA
"""

if __name__ == "__main__":
    print("SOAL 6")
    try:
        K = int(input("Masukkan nilai K : "))
        N = int(input("Masukkan nilai N : "))
        arr = []
        for i in range(N):
            arr.append(int(input("Masukkan angka ke-{} : ".format(i+1))))
        for i in range(N):
            for j in range(N):
                if arr[i] + arr[j] == K:
                    print("BISA")
                    exit()
        print("TIDAK BISA")
    except KeyboardInterrupt:
        print("stopping")
        exit()