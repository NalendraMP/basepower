def perpangkatan(base, power):
    return base ** power


base_number = int(input("Masukkan angka awal : "))
exponent = int(input("Masukkan pangkat : "))


result = perpangkatan(base_number, exponent)
print(f"Hasil adalah : {result}")
