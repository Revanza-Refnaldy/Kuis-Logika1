
"""
SOAL
Akan diberikan sebuah angka N.
Dan akan diberikan N angka.
N = 5
[4, 6, 1, 3, 5]
Silahkan tentukan satu persatu apakah bilangan di array tersebut ganjil atau genap.
Cth input : [4, 6, 1, 3, 5]
Cth output : [genap, genap, ganjil, ganjil, ganjil]
"""

from numpy import append


if __name__ == "__main__":
    print("SOAL 4")
    arrHasil = []
    arr = []
    while True:
        try:
            #extract the input into var
            N = int(input("Masukkan angka N : "))
            
            for i in range(N):
                arr.append(int(input("Masukkan angka ke-{} : ".format(i+1))))
            for i in range(N):
                if arr[i] % 2 == 0:
                    arrHasil.append("Genap")
                else:
                    arrHasil.append("Ganjil")
            print(arrHasil)
            arrHasil = []
            arr = []
        except KeyboardInterrupt:
            print("stopping")
            exit()