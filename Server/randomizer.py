import random

class Randomizer:
    def __init__(self, panjang_digit, jumlah=3):
        self.panjang_digit = panjang_digit
        self.jumlah = jumlah

    def generate(self):
        if self.panjang_digit <= 0 or self.panjang_digit > 3:
            raise ValueError("Panjang digit harus antara 1 dan 3")

        max_value = 10**self.panjang_digit - 1
        min_value = 0

        if self.jumlah > (max_value - min_value + 1):
            raise ValueError(f"Jumlah maksimum untuk panjang digit {self.panjang_digit} adalah {(max_value - min_value + 1)}")
        
        # Generate unique random numbers
        random_numbers = set()
        while len(random_numbers) < self.jumlah:
            random_numbers.add(random.randint(min_value, max_value))
        
        # Convert numbers to strings with leading zeros
        random_strings = [str(num).zfill(self.panjang_digit) for num in random_numbers]
        
        return random_strings

# Contoh penggunaan:
randomizer = Randomizer(3, 5)  # Membuat objek Randomizer dengan panjang digit 3 dan jumlah 5
hasil_acak = randomizer.generate()  # Menghasilkan angka acak
print("Angka acak:", hasil_acak)  # Menampilkan hasil angka acak
