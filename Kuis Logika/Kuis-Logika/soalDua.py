

"""
SOAL 
Akan diberikan sebuah angka, silahkan tentukan apakah angka tersebut ganjil atau
genap.
Cth input : 6
Cth output : Genap
Cth input : 5
Cth output : Ganjil
"""
if __name__ == "__main__":
    print("SOAL 2")
    while True:
        try:
            #extract the input into var
            angka = int(input("Masukkan angka : "))
            #print the max value 
            if angka % 2 == 0:
                print("Genap")
            else:
                print("Ganjil")
        except KeyboardInterrupt:
            print("stopping")
            exit()