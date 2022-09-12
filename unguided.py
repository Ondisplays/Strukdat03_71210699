n=str(input("Masukan kalimat: "))
kata = str(input("Masukan kata yang dicari: "))
n = n.lower().split()
kata = kata.lower()

jumlah_kata = 0
for i in n:
    if i == kata:
        jumlah_kata += 1

print(jumlah_kata)