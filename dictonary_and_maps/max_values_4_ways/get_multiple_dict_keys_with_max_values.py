ages = {"Matt": 30, 'Katie': 29, 'Nik': 31, 'Jack': 43, 'Alison': 43}

max_keys = [key for key, values in ages.items() if values == max(ages.values())]
print(*max_keys)

