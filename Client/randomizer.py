import random

def randomizer(panjang_digit, jumlah=3):
    if panjang_digit <= 0 or panjang_digit > 3:
        raise ValueError("Panjang digit harus antara 1 dan 3")
    
    max_value = 10**panjang_digit - 1
    min_value = 0

    if jumlah > (max_value - min_value + 1):
        raise ValueError(f"Jumlah maksimum untuk panjang digit {panjang_digit} adalah {(max_value - min_value + 1)}")

    random_numbers = random.sample(range(min_value, max_value + 1), jumlah)
    random_strings = [str(num).zfill(panjang_digit) for num in random_numbers]
    
    return random_strings
