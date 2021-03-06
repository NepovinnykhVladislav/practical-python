# pcost.py
#
# Exercise 1.27
total_cost = 0

with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    print(f)
    for line in f:
        try:
            row = line.split(',')
            total_cost += int(row[1]) * float(row[2].strip())
        except:
            print('Missing field')

print(f'Total cost {total_cost}')