"""
SOAL
Akan diberikan sebuah angka N.
Dan akan diberikan N angka.
N = 5
[1,2,3,4,5]
Silahkan tentukan nilai maksimum dari bilangan tersebut.
Cth input : 4, 6, 1, 3, 5
Cth output : 6
"""

if __name__ == "__main__":
    print("SOAL 5")
    arr = []
    while True:
        try:
            #extract the input into var
            N = int(input("Masukkan angka N : "))
            for i in range(N):
                arr.append(int(input("Masukkan angka ke-{} : ".format(i+1))))
            print("Nilai maksimum adalah : ", max(arr) , "\n")
            arr = []
        except KeyboardInterrupt:
            print("stopping")
            exit()