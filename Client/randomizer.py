import random


class Randomizer:
    def __init__(self, start_num, end_num):
        self._start_num = start_num
        self._end_num = end_num
        self.generated_numbers = set()

    @property
    def start_num(self):
        return self._start_num

    @start_num.setter
    def start_num(self, value):
        self._start_num = value

    @property
    def end_num(self):
        return self._end_num

    @end_num.setter
    def end_num(self, value):
        self._end_num = value

    def randomize(self, min_value, max_value, jumlah_angka_return=1):
        if min_value >= max_value:
            print(min_value, max_value)
            raise ValueError("min_value harus lebih kecil dari max_value")

        total_possible_numbers = max_value - min_value + 1

        if jumlah_angka_return > total_possible_numbers:
            print(
                f"Jumlah maksimum untuk rentang {min_value} hingga {max_value} adalah {total_possible_numbers}")
            return [-1]

        if jumlah_angka_return > total_possible_numbers - len(self.generated_numbers):
            print("Tidak cukup angka yang unik tersedia.")
            return [-1]

        random_numbers = []
        while len(random_numbers) < jumlah_angka_return:
            num = random.randint(min_value, max_value)
            if num not in self.generated_numbers:
                self.generated_numbers.add(num)
                random_numbers.append(num)

        return random_numbers

    def reset(self):
        self.generated_numbers = set()
