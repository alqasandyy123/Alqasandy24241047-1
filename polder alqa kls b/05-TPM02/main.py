PI = 3.14159

# Mengecek bilangan genap atau ganjil
angka = int(input("Masukkan sebuah angka: "))

if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap.")
else:
    print(f"{angka} adalah bilangan ganjil.")

# Mengonversi suhu dari Fahrenheit ke Celcius
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

celcius = (fahrenheit - 32) * 5.0 / 9.0
print(f"Suhu dalam Celcius: {celcius:.2f}")

# Menghitung luas lingkaran
radius = float(input("Masukkan jari-jari lingkaran: "))

luas_lingkaran = PI * radius * radius
print(f"Luas lingkaran dengan jari-jari {radius} adalah: {luas_lingkaran:.2f}")
