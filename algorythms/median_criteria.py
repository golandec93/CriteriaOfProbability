import csv


data = []
with open('../data/plane1.csv') as file:
    data1 = csv.reader(file)
    for row in data1:
        data.append(int(row[0]))

data_sorted = sorted(data)
x_med = 0
if len(data) % 2 != 0:
    x_med = data_sorted(int(len(data) / 2))
else:
    i = int(len(data_sorted) / 2) - 1
    x_med = (data_sorted[i]+data_sorted[i+1])/2
print('Median: ' + str(x_med))

delta = []
for a in data:
    delta.append(a-x_med)

max_series = 0
series = 0
series_number = 1
old_sign = delta[0] > 0
print(delta)
for a in delta:
    new_sign = a > 0
    if new_sign == old_sign:
        series += 1
    else:
        max_series = max(series, max_series)
        series = 0
        series_number += 1
        old_sign = new_sign
print(series_number)