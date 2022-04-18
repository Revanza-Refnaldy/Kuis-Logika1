"""
SOAL 
Bayangkan anda memiliki sebuah array.
Array ini adalah array angka, dan anda ingin tau apakah ada nilai yang sama di dalam
nya.

Silahkan tentukan apakah ada nilai yang sama di dalam array yang diberikan.
Cth input : N = 5, array = [4, 3, 6, 7, 1]
Cth output : TIDAK ADA
Cth input : N = 5,array = [4, 1, 8, 7, 1]
Cth output : ADA
"""

if __name__ == "__main__":
    try:
        N = int(input("Masukkan nilai N : "))
        arr = []
        for i in range(N):
            arr.append(int(input("Masukkan angka ke-{} : ".format(i+1))))
        # check if there is any duplicate
        for i in range(N):
            for j in range(i+1, N):
                if arr[i] == arr[j]:
                    print("ADA")
                    exit()
        print("TIDAK ADA")
    except KeyboardInterrupt:
        print("stopping")
        exit()