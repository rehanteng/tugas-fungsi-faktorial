def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

print("Menghitung Faktorial")
angka = int(input("Masukkan angka untuk menghitung faktorial: "))

if angka < 0:
    print("Faktorial tidak didefinisikan untuk angka negatif")
else:
    hasil = faktorial(angka)
    print(f"Faktorial dari {angka} adalah {hasil}")
    
# jadi Kode tersebut mendefinisikan sebuah fungsi faktorial yang menghitung faktorial dari sebuah bilangan menggunakan rekursi. Fungsi ini memeriksa apakah bilangan yang diberikan adalah 0 atau 1, dan jika ya, mengembalikan 1. Jika tidak, fungsi mengalikan bilangan tersebut dengan hasil faktorial dari bilangan tersebut dikurangi satu.