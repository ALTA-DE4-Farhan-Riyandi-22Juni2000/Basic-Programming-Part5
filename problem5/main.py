def pair_sum(arr, target):
    seen_numbers = {}  # Membuat dictionary untuk menyimpan angka yang sudah dilihat
    for index, value in enumerate(arr):
        difference = target - value
        if difference in seen_numbers:
            return [seen_numbers[difference], index]
        seen_numbers[value] = index
    return None


if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]
    print(pair_sum([1, 2, 3, 4, 6], 11))