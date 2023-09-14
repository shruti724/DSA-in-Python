ages = [{"Matt": 30, 'Katie': 29}, {'Nik': 31, 'Jack': 43}, {'Alison': 32}]
max_age = max([max(dict.values()) for dict in ages])
print(max_age)
