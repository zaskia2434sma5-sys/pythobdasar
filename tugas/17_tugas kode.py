baris = int(input("Masukkan jumlah baris: "))

for i in range(baris, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()