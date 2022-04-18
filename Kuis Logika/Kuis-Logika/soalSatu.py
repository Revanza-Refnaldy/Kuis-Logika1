
"""
SOAL :
1. Mana Yang Lebih Besar?
Akan diberikan dua angka, silahkan tentukan angka mana yang lebih besar
Cth input : 6, 7
Cth output : 7
Cth input : 1, 10000
Cth output : 10000
"""

if __name__ == "__main__":
    print("SOAL 1")
    while True:
        try:
            #extract the input into array
            arr = input("Masukkan angka : ").split(", ")
            #print the max value 
            print("Yang lebih besar adalah : ", max(arr))
        except KeyboardInterrupt:
            print("stopping")
            exit()
    