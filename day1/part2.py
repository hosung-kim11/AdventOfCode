import os

col1 = []
col2 = []
dict = {}

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, "r") as file:
    for line in file:
        parts = line.strip().split()

        if len(parts) >= 2:
            col1.append(int(parts[0]))
            col2.append(int(parts[1]))

total = 0
for num in col1:
    if num in dict:
        total += dict[num]
    else:
        count = col2.count(num) * num
        dict[num] = count
        total += count


print(total)
