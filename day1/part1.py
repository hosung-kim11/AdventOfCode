import os

col1 = []
col2 = []

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, "r") as file:
    for line in file:
        parts = line.strip().split()

        if len(parts) >= 2:
            col1.append(int(parts[0]))
            col2.append(int(parts[1]))

col1.sort()
col2.sort()
differences = [abs(a - b) for a, b in zip(col1, col2)]
print(sum(differences))