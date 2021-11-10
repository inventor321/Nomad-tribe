prime_numbers = [3, 2, 6, 7, 11, 15, 1, 14, 10, 13, 9, 0, 8, 4, 5, 12]

# sort the list
prime_numbers.sort()

for i in range(len(prime_numbers)):
    if i - prime_numbers[i] == 0:
        pass
    else:
        print("error")
print("check done")
print(prime_numbers)

# Output: [2, 3, 5, 7, 11]